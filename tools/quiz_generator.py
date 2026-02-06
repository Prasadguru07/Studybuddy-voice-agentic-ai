from langchain_ollama import OllamaLLM 


def generate_quiz(topic: str) -> str:
    llm = OllamaLLM(model="llama3")
    prompt = (
        f"Create 5 quiz questions on the topic '{topic}'. "
        "Each question should be multiple choice with 4 options labeled (A), (B), (C), and (D). "
        "After each question, clearly provide the correct answer on a new line starting with 'Answer: '.\n\n"
        "Example format:\n"
        "1. What is ...?\n"
        "(A) option1\n"
        "(B) option2\n"
        "(C) option3\n"
        "(D) option4\n"
        "Answer: (B)\n"
    )

