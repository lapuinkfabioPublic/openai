#Fabio Leandro Lapuinka
#07/07/2025 Ollama Chat
import streamlit as st
from crewai import Agent, Task, Crew  # Import necessary classes from crewai
# pip install streamlit crewai langchain-community


st.title("Use Local Ollama LLM with CrewAI")


# Input for the prompt
prompt = st.text_area(label="Ask to Asgard:")
button = st.button("Generate")

if button:
    if prompt:
        # Create an agent with role, goal, and backstory
        agent = Agent(
            role="Assistant",
            goal="Provide helpful responses based on user input.",
            backstory="This agent assists users by generating responses using a local Ollama LLM.",
            llm="ollama/llama3.2:3b"  # Use the local LLM
        )

        # Create a task associated with the agent
        task = Task(
            description=f"Generate a response based on user input: {prompt}",
            expected_output="The generated response will be a flat text.",
            agent=agent  # Assign the agent to this task
        )

        # Create a Crew with the agent and task
        crew = Crew(agents=[agent], tasks=[task])

        # Execute the crew to get results
        result = crew.kickoff()

        # Display the generated response
        st.markdown(result)