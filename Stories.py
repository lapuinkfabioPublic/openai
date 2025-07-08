import streamlit as st
from crewai import Agent, Task, Crew

st.title("Story Writing with CrewAI and Ollama")

# Input for story prompt
story_prompt = st.text_area(label="Enter a story prompt:")
button = st.button("Generate Story")

if button:
    if story_prompt:

        # Create agents for story generation
        writer = Agent(
            role="Writer",
            goal="Generate a creative story based on the given prompt.",
            backstory="This agent is a skilled writer with a vivid imagination. They will craft an engaging story using the provided prompt as inspiration.",
            llm="ollama/llama3.2:3b"
        )

        editor = Agent(
            role="Editor",
            goal="Review and refine the generated story for clarity, coherence, and flow.",
            backstory="This agent is an experienced editor who will carefully review the story, provide feedback, and make necessary revisions to improve the overall quality.",
            llm="ollama/llama3.2:3b"
        )

        # Create tasks for the agents
        write_story = Task(
            description=f"Write a short story based on the prompt: {story_prompt}",
            expected_output="A creative short story with a beginning, middle, and end.",
            agent=writer
        )
        edit_story = Task(
            description="Review and edit the generated story to enhance clarity, coherence, and flow.",
            expected_output="The edited story with improved quality.",
            agent=editor
        )

        # Create a Crew with the agents and tasks
        story_crew = Crew(agents=[writer, editor], tasks=[write_story, edit_story])

        # Execute the story generation and editing
        final_story = story_crew.kickoff()

        # Display the generated story
        # Create two columns
        col1, col2 = st.columns(2)
        # Input for the first column
        with col1:
            st.header("First Story:")
            st.markdown(write_story.output)

        # Input for the second column
        with col2:
            st.header("Final Story:")
            st.markdown(final_story)


