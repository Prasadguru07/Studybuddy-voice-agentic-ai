import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os
import platform
import time
from main import ask_studybuddy  # Make sure this returns the agent's response

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
        st.error(f"Speech recognition service error: {e}")
        return ""

def speak_text(text):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save("response.mp3")

        system_platform = platform.system()
        if system_platform == "Windows":
            os.system("start response.mp3")
        elif system_platform == "Darwin":  # macOS
            os.system("afplay response.mp3")
        else:  # Linux
            os.system("mpg123 response.mp3")

        st.audio("response.mp3", format='audio/mp3')
    except Exception as e:
        st.warning(f"Could not play audio: {e}")

def display_response_with_code(response: str):
    if not response:
        st.warning("🤖 No response received.")
        return

    if "```" in response:
        parts = response.split("```")
        st.markdown(f"**🧾 Answer:** {parts[0].strip()}")
        for i in range(1, len(parts), 2):
            code_block = parts[i].strip()
            if any(x in code_block for x in ['─', '│', '┌', '└', '+']):
                st.text(code_block)
            else:
                st.code(code_block, language="python")
    elif '\n' in response and any(x in response.lower() for x in ['def ', 'class ', 'import ', '=', ':']):
        st.code(response, language="python")
    elif '│' in response or '+' in response or '─' in response:
        st.text(response)
    else:
        st.markdown(f"**🧾 Answer:** {response}")

# 🧠 UI Start
st.title("🧠 StudyBuddy Voice Assistant")
st.markdown("Ask your doubts via **voice** or **text** (DBMS / CN / OS / SQL)")

# 🎤 Voice input
if st.button("🎤 Ask via Voice"):
    user_input = transcribe_audio()
    if user_input:
        try:
            time.sleep(1)  # Optional: prevent fast repeated queries
            response = ask_studybuddy(user_input)
            if response:
                display_response_with_code(response)
                speak_text(response)
            else:
                st.warning("🤖 No response from agent.")
        except Exception as e:
            st.error(f"❌ Agent failed: {e}")

# 📝 Text input
with st.form("text_form"):
    user_text = st.text_input("Or type your question:")
    submitted = st.form_submit_button("Ask")
    if submitted and user_text:
        try:
            time.sleep(1)  # Optional: prevent fast repeated queries
            response = ask_studybuddy(user_text)
            if response:
                display_response_with_code(response)
                speak_text(response)
            else:
                st.warning("🤖 No response from agent.")
        except Exception as e:
            st.error(f"❌ Agent failed: {e}")
