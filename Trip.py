import streamlit as st
from crewai import Agent, Task, Crew

st.title("Travel Itinerary Planner")

# Input for travel destination
destination = st.text_input(label="Enter your travel destination:")
button = st.button("Plan Trip")

if button:
    if destination:
        # Create agents for itinerary planning and local expert advice
        planner = Agent(
            role="Trip Planner",
            goal="Create a detailed travel itinerary based on the destination.",
            backstory="This agent specializes in planning exciting trips.",
            llm="ollama/llama3.2:3b"
        )

        local_expert = Agent(
            role="Local Expert",
            goal="Provide insights and recommendations about the destination.",
            backstory="This agent knows all the best spots in town!",
            llm="ollama/llama3.2:3b"
        )

        # Create tasks for the agents
        create_itinerary = Task(
            description=f"Plan a trip itinerary for {destination}.",
            expected_output="A detailed itinerary including activities and timings.",
            agent=planner
        )

        get_local_insights = Task(
            description=f"Provide local insights about {destination}.",
            expected_output="Recommendations for places to visit and eat.",
            agent=local_expert
        )

        # Create a Crew with the agents and tasks
        trip_crew = Crew(agents=[planner, local_expert], tasks=[create_itinerary, get_local_insights])

        # Execute the crew to plan the trip and get insights
        final_itinerary = trip_crew.kickoff()

        # Display the planned itinerary and local insights
        st.subheader("Planned Itinerary:")
        st.markdown(create_itinerary.output)

        st.subheader("Local Insights:")
        st.markdown(final_itinerary)