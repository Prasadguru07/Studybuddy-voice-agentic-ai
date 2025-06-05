def explain_topic(topic):
    prompt = f"explain the topic {topic} in detail, covering its key concepts, principles, and applications. Provide examples where relevant."
    from langchain.llms import Ollama
    llm = Ollama(model="qwen2.5:0.5b")
    return llm(prompt)