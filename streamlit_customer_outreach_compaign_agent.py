import warnings
import os
from dotenv import load_dotenv
load_dotenv()
warnings.filterwarnings('ignore')
from crewai import Agent, Task, Crew
from crewai_tools import DirectoryReadTool , FileReadTool ,SerperDevTool
from crewai.tools import BaseTool




class SentimentAnalysisTool(BaseTool):
    name: str = "Sentiment Analysis Tool"
    description: str = ("Analyzes the sentiment of text "
                        "to ensure positive and engaging communication.")

    def _run(self, text: str) -> str:
        # Your custom code tool goes here
        return "positive"

sentiment_analysis_tool = SentimentAnalysisTool()
# tasks
crew =  Crew(
    agents=[sales_rep_agent,
            lead_sales_rep_agent],

    tasks=[lead_profiling_task,
           personalized_outreach_task],
    verbose = 2,
    memory = True
)


































