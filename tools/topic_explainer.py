def explain_topic(topic):
    prompt = f"explain the topic {topic} in detail, covering its key concepts, principles, and applications. Provide examples where relevant."
    from langchain_ollama import OllamaLLM 
    llm = OllamaLLM(model="llama3")
    return llm.invoke(prompt)