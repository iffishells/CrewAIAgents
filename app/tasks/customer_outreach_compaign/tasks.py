from crewai import Agent, Task, Crew
class CustomerOutreachCampaignTasks:

    def __int__(self):
        self.lead_profiling_task = Task(
            description=(
                "Conduct an in-depth analysis of {lead_name}, "
                "a company in the {industry} sector "
                "that recently showed interest in our solutions. "
                "Utilize all available data sources "
                "to compile a detailed profile, "
                "focusing on key decision-makers, recent business "
                "developments, and potential needs "
                "that align with our offerings. "
                "This task is crucial for tailoring "
                "our engagement strategy effectively.\n"
                "Don't make assumptions and "
                "only use information you absolutely sure about."
            ),
            expected_output=(
                "A comprehensive report on {lead_name}, "
                "including company background, "
                "key personnel, recent milestones, and identified needs. "
                "Highlight potential areas where "
                "our solutions can provide value, "
                "and suggest personalized engagement strategies."
            ),
            tools=[directory_real_tool, file_read_tool, search_tool],
            agent=sales_rep_agent,
        )

        self.personalized_outreach_task = Task(
            description=(
                "Using the insights gathered from "
                "the lead profiling report on {lead_name}, "
                "craft a personalized outreach campaign "
                "aimed at {key_decision_maker}, "
                "the {position} of {lead_name}. "
                "The campaign should address their recent {milestone} "
                "and how our solutions can support their goals. "
                "Your communication must resonate "
                "with {lead_name}'s company culture and values, "
                "demonstrating a deep understanding of "
                "their business and needs.\n"
                "Don't make assumptions and only "
                "use information you absolutely sure about."
            ),
            expected_output=(
                "A series of personalized email drafts "
                "tailored to {lead_name}, "
                "specifically targeting {key_decision_maker}."
                "Each draft should include "
                "a compelling narrative that connects our solutions "
                "with their recent achievements and future goals. "
                "Ensure the tone is engaging, professional, "
                "and aligned with {lead_name}'s corporate identity."
            ),
            tools=[sentiment_analysis_tool, search_tool],
            agent=lead_sales_rep_agent,
        )

