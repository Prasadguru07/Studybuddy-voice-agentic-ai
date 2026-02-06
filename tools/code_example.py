def get_code_example(topic):
    from langchain_ollama import OllamaLLM 
    llm = OllamaLLM(model="llama3")
    prompt = f"Give a code example or diagram explanation for: {topic}"
    return llm(prompt)
