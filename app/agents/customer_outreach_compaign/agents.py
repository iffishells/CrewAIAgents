from crewai import Agent, Task, Crew

class CustomerOutreachCampaignAgents:
    def __init__(self):
        self.sales_rep_agent = Agent(
            role="Sales Representative",
            goal="Identify high-value leads that match the company's criteria.",
            backstory=(
                "As part of the dynamic sales team at CrewAI, "
                "your mission is to scour the digital landscape for potential leads. "
                "Armed with cutting-edge tools and a strategic mindset, you analyze data, trends, "
                "and interactions to uncover opportunities that others might overlook. "
                "Your work is crucial in paving the way for meaningful connections and driving the company's growth."
            ),
            allow_delegation=False,
            verbose=True
        )

        self.lead_sales_rep_agent = Agent(
            role="Lead Sales Representative",
            goal="Nurture leads with personalized, compelling communications.",
            backstory=(
                "Within the vibrant ecosystem of CrewAI's sales department, "
                "you stand out as the bridge between potential clients and the solutions they need. "
                "By creating engaging, personalized messages, you not only inform the leads about our offerings "
                "but also make them feel seen and heard. "
                "Your role is pivotal in converting interest into action, guiding leads through their journey "
                "from curiosity to commitment."
            ),
            allow_delegation=False,
            verbose=True
        )
