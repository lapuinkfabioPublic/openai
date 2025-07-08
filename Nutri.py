import streamlit as st
from crewai import Agent, Task, Crew

st.title("Recipe Generator and Nutrition Analyzer")

# Input for recipe prompt
recipe_prompt = st.text_area(label="Enter a recipe idea:")
button = st.button("Generate Recipe")

if button:
    if recipe_prompt:
        # Create agents for recipe generation and nutrition analysis
        chef = Agent(
            role="Chef",
            goal="Generate a creative recipe based on the given idea.",
            backstory="This agent is a skilled chef who loves to create delicious recipes.",
            llm="ollama/llama3.2:3b"
        )

        nutritionist = Agent(
            role="Nutritionist",
            goal="Analyze the generated recipe for nutritional value.",
            backstory="This agent is a nutrition expert who evaluates recipes for health benefits.",
            llm="ollama/llama3.2:3b"
        )

        # Create tasks for the agents
        generate_recipe = Task(
            description=f"Create a recipe based on the idea: {recipe_prompt}",
            expected_output="A detailed recipe with ingredients and instructions.",
            agent=chef
        )

        analyze_nutrition = Task(
            description="Evaluate the nutritional value of the generated recipe.",
            expected_output="Nutritional analysis of the recipe.",
            agent=nutritionist
        )

        # Create a Crew with the agents and tasks
        recipe_crew = Crew(agents=[chef, nutritionist], tasks=[generate_recipe, analyze_nutrition])

        # Execute the crew to generate and analyze the recipe
        final_recipe = recipe_crew.kickoff()

        # Display the generated recipe and nutritional analysis
        st.subheader("Generated Recipe:")
        st.markdown(generate_recipe.output)

        st.subheader("Nutritional Analysis:")
        st.markdown(final_recipe)
