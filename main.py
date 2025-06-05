from langchain.agents import initialize_agent, Tool, AgentType
from langchain_community.llms import Ollama
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import Tool


# Importing tools
from tools.topic_explainer import explain_topic
from tools.quiz_generator import generate_quiz
from tools.code_example import get_code_example
from tools.summary_tool import summarize_day
from tools.search_tool import search_tool

llm = Ollama(model="qwen2.5:0.5b")

# Defining LangChain Tools
tools = [
    Tool(
        name="WebSearch",
        func= search_tool,
        description="Useful for answering questions about current events or unknown topics from the web"
    ),
    Tool(
        name="TopicExplainer",
        func=explain_topic,
        description="Explains core CS topics like DBMS, OS, CN, SQL."
    ),
    Tool(
        name="QuizGenerator",
        func=generate_quiz,
        description="Creates MCQs or short questions to test understanding of CS topics."
    ),
    Tool(
        name="CodeExample",
        func=get_code_example,
        description="Provides code examples or diagrams for CS topics."
    ),
    Tool(
        name="SummaryTool",
        func=summarize_day,
        description="Summarizes what was learned during the session."
    )
]

# Initialize Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose=True
)

# Wrapper function to call agent
def ask_studybuddy(prompt: str) -> str:
    result = agent.invoke({"input": prompt})
    return result["output"]
