from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import Tool

# Initialize the DuckDuckGo search tool
search_tool = DuckDuckGoSearchRun()

# Export it as a LangChain Tool
web_search_tool = Tool(
    name="WebSearch",
    func=search_tool.run,
    description="Useful for answering questions about current events or when external web knowledge is required."
)
