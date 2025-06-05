def summarize_day(_=None):
    from langchain.llms import Ollama
    llm = Ollama(model="qwen2.5:0.5b")
    prompt = "Summarize all that I’ve learned today related to DBMS, OS, CN, or SQL."
    return llm(prompt)
