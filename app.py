from crewai import Agent, Crew, LLM, Task
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define the topic
topic = "Medical Industry using Generative AI"

# Define the search tool and LLM
search_tool = SerperDevTool(n=1)  # Search tool with 1 result limit
llm = LLM(model='gpt-4')  # Use GPT-4 as the language model

# Define the Senior Research Analyst agent
senior_research_analyst = Agent(
    role="Senior Research Analyst",
    goal=f"Perform in-depth analysis and provide data-driven insights on {topic}.",
    backstory="A highly skilled research analyst with expertise in industry trends, market analysis, and technical tools.",
    tools=[search_tool],  # Add the search tool to the agent
    llm=llm  # Attach the language model
)

# Define the Content Writer agent
content_writer = Agent(
    role="Content Writer",
    goal="Create engaging, high-quality written content tailored to the target audience.",
    backstory="A creative content writer skilled in crafting articles, blogs, and marketing materials. Specializes in creating content that informs, persuades, and resonates with readers.",
    allow_delegation=True,  # Allow the agent to delegate tasks
    llm=llm  # Attach the language model
)

# Define the Research Task
research_task = Task(
    description=f"Analyze the applications and impact of Generative AI in the {topic}. Identify trends, benefits, challenges, and future opportunities.",
    expected_output="A comprehensive report or insights on the role and influence of Generative AI in the Medical Industry.",
    agent=senior_research_analyst  # Assign the Senior Research Analyst agent to the task
)

# Define the Content Writing Task
writing_task = Task(
    description="Write a detailed and engaging article based on the insights obtained from the research on Generative AI in the Medical Industry.",
    expected_output=(
        "A well-structured article highlighting the key applications, benefits, challenges, "
        "and future potential of Generative AI in the Medical Industry. The tone should be professional and informative."
    ),
    agent=content_writer  # Assign the Content Writer agent to the task
)

# Create the Crew instance
crew = Crew(
    agents=[senior_research_analyst, content_writer],  # Add the agents
    tasks=[research_task, writing_task],  # Add the tasks
    verbose=True  # Enable verbose mode for detailed output
)

# Kick off the tasks with the provided topic as input
results = crew.kickoff(
    inputs={
        "topic": topic  # Ensure the topic is passed as a key-value pair
    }
)

# Print the results
print("Crew Results:")
print(results)
