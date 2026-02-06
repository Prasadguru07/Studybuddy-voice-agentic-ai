from langchain.agents import initialize_agent, Tool, AgentType
from langchain_ollama import OllamaLLM  
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import Tool
import os
import time
from functools import lru_cache
from datetime import datetime, timedelta


# Importing tools
from tools.topic_explainer import explain_topic
from tools.quiz_generator import generate_quiz
from tools.code_example import get_code_example
from tools.summary_tool import summarize_day
from tools.search_tool import search_tool

# Use CPU instead of GPU to avoid CUDA errors
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'  # Force CPU usage

# Use faster, smaller model for better performance
llm = OllamaLLM(model="qwen2.5:0.5b")

# Simple in-memory cache for responses (24 hour TTL)
response_cache = {}
cache_timestamp = {}

def get_cached_response(prompt: str) -> str:
    """Check if response exists in cache and is still valid"""
    if prompt in response_cache:
        if datetime.now() - cache_timestamp[prompt] < timedelta(hours=24):
            return response_cache[prompt]
    return None

def cache_response(prompt: str, response: str):
    """Store response in cache"""
    response_cache[prompt] = response
    cache_timestamp[prompt] = datetime.now()

# Optimized tool definitions with timeouts
tools = [
    Tool(
        name="TopicExplainer",
        func=explain_topic,
        description="Explains core CS topics like DBMS, OS, CN, SQL. Use FIRST for known topics."
    ),
    Tool(
        name="CodeExample",
        func=get_code_example,
        description="Provides code examples for CS topics. Use for code-related questions."
    ),
    Tool(
        name="QuizGenerator",
        func=generate_quiz,
        description="Creates MCQs or short questions. Use ONLY when user asks for quiz/questions."
    ),
    Tool(
        name="WebSearch",
        func=search_tool,
        description="Web search ONLY for current events or unknown topics. Avoid if TopicExplainer works."
    ),
    Tool(
        name="SummaryTool",
        func=summarize_day,
        description="Summarizes learned content. Use ONLY at session end when user asks."
    )
]

# Initialize Agent with optimizations
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose=False,  # Disable verbose for faster processing
    max_iterations=3,  # Limit agent steps (prevents excessive tool calls)
    early_stopping_method="generate",  # Stop early if good response found
)

# Wrapper function with caching and streaming support
def ask_studybuddy(prompt: str) -> str:
    """
    Optimized agent wrapper with:
    - Response caching (24hr TTL)
    - Limited iterations (max 3 steps)
    - Timeout protection
    - Smaller, faster model
    """
    # Check cache first
    cached = get_cached_response(prompt)
    if cached:
        return f"[⚡ Cached Response]\n{cached}"
    
    try:
        # Invoke agent with timeout
        result = agent.invoke(
            {"input": prompt},
            config={"timeout": 30}  # 30 second timeout
        )
        response = result["output"]
        
        # Cache successful response
        cache_response(prompt, response)
        return response
    except Exception as e:
        return f"⚠️ Error: {str(e)[:100]}. Try simpler question."
