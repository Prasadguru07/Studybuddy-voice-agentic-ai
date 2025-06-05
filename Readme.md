# 🧠 StudyBuddy: Voice-Powered Agentic AI for CS Major Learning

StudyBuddy is an **Agentic AI-based voice assistant** designed to help students understand core **Computer Science** topics like **DBMS, OS, CN and SQL**. Built using cutting-edge **LLM (qwen2.5:0.5b via Ollama)** and integrated with tools for **web search, quiz generation, code examples, topic explanation**, and **daily summaries**.



## 🚀 Features

- 🎙️ **Voice-based interaction** using SpeechRecognition and gTTS
- 📚 **Topic explanations** for DBMS, OS, CN, SQL
- 🧾 **Quiz generation** with answers
- 💡 **Code examples and diagrams**
- 🧠 **Summarization of daily learning**
- 🌐 **Web search integration** (RAG-enabled)
- 🎨 Simple **Streamlit UI** for interaction



## 🛠️ Technologies & Tools Used

| Tool | Purpose |
|------|---------|
| [LangChain](https://www.langchain.com/) | Agent framework for LLM orchestration |
| [Ollama](https://ollama.com/) | Local LLM runtime (qwen2.5:0.5b) |
| [Streamlit](https://streamlit.io/) | Web UI framework |
| [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) | Voice input |
| [gTTS](https://pypi.org/project/gTTS/) | Text-to-speech |
| [Python 3.12+](https://www.python.org/) | Programming language |
| Web scraping API or search tool | For real-time retrieval (RAG) |



## 📂 Folder Structure

studybuddy-voice-agentic-ai/
├── main.py # Agent setup and routing
├── tools/
│ ├── topic_explainer.py
│ ├── quiz_generator.py
│ ├── code_example.py
│ ├── summary_tool.py
│ └── search_tool.py
├── ui_streamlit.py # Streamlit + voice interface
├── README.md



## ✅ Setup Instructions

1. pip install requirements.txt

2. install ollama locally and download desired model (ex: Ollama3 or qwen2.5:0.5b)

3. ollama run qwen2.5:0.5b

4. ollama pull qwen2.5:0.5b

5. streamlit run ui_streamlit.py

### Example Prompts

"Explain normalization in DBMS."

"Create five quiz questions on computer networks."

"Show me a code example of bubble sort in Python."

"Summarize what I learned today."

"Search recent cybersecurity attacks."


### Feedback & Contributions

Pull requests are welcome! For major changes, open an issue first.