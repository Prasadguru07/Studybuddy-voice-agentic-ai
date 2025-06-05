def get_code_example(topic):
    from langchain.llms import Ollama
    llm = Ollama(model="qwen2.5:0.5b")
    prompt = f"Give a code example or diagram explanation for: {topic}"
    return llm(prompt)
