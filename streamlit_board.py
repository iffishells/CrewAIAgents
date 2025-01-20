import streamlit as st
from crewai import Agent, Crew, LLM, Task
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit App Title
st.title("AI Crew Dashboard")
st.write("Enter a query or topic, and let our AI agents do the research and content writing!")

# Sidebar for Parameters
st.sidebar.header("OpenAI Parameters")
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7, step=0.1)
max_tokens = st.sidebar.number_input("Max Tokens", min_value=100, max_value=4000, value=1000, step=50)
top_p = st.sidebar.slider("Top P", 0.0, 1.0, 1.0, step=0.1)
frequency_penalty = st.sidebar.slider("Frequency Penalty", 0.0, 2.0, 0.0, step=0.1)
presence_penalty = st.sidebar.slider("Presence Penalty", 0.0, 2.0, 0.0, step=0.1)

# User Input for Topic
topic = st.text_input("Enter a query or topic:", placeholder="e.g., Generative AI in the Medical Industry")

if topic:
    st.write(f"Selected Topic: **{topic}**")

# Define AI Components
search_tool = SerperDevTool(n=1)  # Search tool
llm = LLM(
    model='gpt-4',
    temperature=temperature,
    max_tokens=max_tokens,
    top_p=top_p,
    frequency_penalty=frequency_penalty,
    presence_penalty=presence_penalty
)  # Configure LLM with sidebar parameters

# Define Agents
senior_research_analyst = Agent(
    role="Senior Research Analyst",
    goal=f"Perform in-depth analysis and provide data-driven insights on {topic}.",
    backstory="A highly skilled research analyst with expertise in industry trends, market analysis, and technical tools.",
    tools=[search_tool],
    llm=llm
)

content_writer = Agent(
    role="Content Writer",
    goal="Create engaging, high-quality written content tailored to the target audience.",
    backstory="A creative content writer skilled in crafting articles, blogs, and marketing materials.",
    allow_delegation=True,
    llm=llm
)

# Define Tasks
research_task = Task(
    description=f"Analyze the applications and impact of Generative AI in {topic}. Identify trends, benefits, challenges, and future opportunities.",
    expected_output="A comprehensive report or insights on the role and influence of Generative AI in the specified industry.",
    agent=senior_research_analyst
)

writing_task = Task(
    description="Write a detailed and engaging article based on the insights obtained from the research.",
    expected_output="A well-structured article highlighting the key applications, benefits, challenges, and future potential.",
    agent=content_writer
)

# Run Crew if button is pressed
if st.button("Run Analysis"):
    with st.spinner("Processing..."):
        crew = Crew(
            agents=[senior_research_analyst, content_writer],
            tasks=[research_task, writing_task],
            verbose=True
        )
        results = crew.kickoff(inputs={"topic": topic})

    # Display Results

    st.success("Analysis Complete!")
    st.write(results["raw"])
    if "research_task" in results:
        st.subheader("Research Insights")
        st.write(results["research_task"])
    if "writing_task" in results:
        st.subheader("Generated Content")
        st.write(results["writing_task"])
