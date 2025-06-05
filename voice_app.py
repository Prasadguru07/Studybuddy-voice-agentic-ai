import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os
from main import ask_studybuddy

def transcribe_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Listening... Speak now!")
        audio = r.listen(source, phrase_time_limit=5)

    try:
        query = r.recognize_google(audio)
        st.success(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        st.error("Sorry, I couldn’t understand.")
        return ""
    except sr.RequestError as e:
        st.error(f"Error with the speech service: {e}")
        return ""

def speak_text(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("start response.mp3")  # For Windows
    st.audio("response.mp3", format='audio/mp3')

def display_response_with_code(response: str):
    if "```" in response:
        parts = response.split("```")
        st.markdown(f"**🧾 Answer:** {parts[0].strip()}")
        for i in range(1, len(parts), 2):
            code_block = parts[i].strip()
            if any(x in code_block for x in ['─', '│', '┌', '└', '+']):
                st.text(code_block)  # Treat as diagram
            else:
                st.code(code_block, language="python")
                
    elif '\n' in response and any(x in response.lower() for x in ['def ', 'class ', 'import ', '=', ':']):
        # Simple fallback if response is multi-line and looks like code
        st.code(response, language="python")
    elif '│' in response or '+' in response or '─' in response:
        st.text(response)  # Text diagram (ASCII)
    else:
        st.markdown(f"**🧾 Answer:** {response}")

st.title("🧠 StudyBuddy Voice Assistant")
st.markdown("Ask your doubts via **voice** (DBMS / CN / OS / SQL)")

if st.button("🎤 Ask via Voice"):
    user_input = transcribe_audio()
    if user_input:
        response = ask_studybuddy(user_input)
        display_response_with_code(response)
        speak_text(response)

with st.form("text_form"):
    user_text = st.text_input("Or type your question:")
    submitted = st.form_submit_button("Ask")
    if submitted and user_text:
        response = ask_studybuddy(user_text)
        display_response_with_code(response)
        speak_text(response)
