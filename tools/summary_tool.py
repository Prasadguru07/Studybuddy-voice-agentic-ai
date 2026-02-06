def summarize_day(_=None):
    from langchain_ollama import OllamaLLM 
    llm = OllamaLLM(model="llama3")
    prompt = "Summarize all that I’ve learned today related to DBMS, OS, CN, or SQL."
    return llm(prompt)
