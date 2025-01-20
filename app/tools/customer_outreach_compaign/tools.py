from crewai_tools import DirectoryReadTool , FileReadTool ,SerperDevTool


class CustomerOutreachCampaignTools:

    def __int__(self):
        self.directory_real_tool = DirectoryReadTool(directory="./instruction")
        self.file_read_tool = FileReadTool()
        self.search_tool = SerperDevTool()