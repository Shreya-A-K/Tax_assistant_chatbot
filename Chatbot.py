import os
import google.generativeai as genai
import speech_recognition as sr
import streamlit as st
from gtts import gTTS
import pyttsx3

genai.configure(api_key="YOUR_API_KEY")

# Create the model
generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash",
  generation_config=generation_config,
  system_instruction="Tax assistant that can automate tax filing processes, simplifying complex calculations, identifying deductions, and minimizing errors. Answer should be step by step. Maximum of 5 steps can be given.",
)

chat_session = model.start_chat(
  history=[]
)

# Initialize recognizer class in order to recognize the speech
r = sr.Recognizer()

# Recognize the voice command
def recognize_voice():
    with sr.Microphone() as source:
        st.write("Listening for your query...")
        audio_data = r.listen(source)
        st.write("Recognizing...")
        try:
            text = r.recognize_google(audio_data)
            st.write(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            st.write("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            st.write("Sorry, the service is down.")
            return None

# Text-to-speech conversion
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

st.title("Tax Assistant")
st.write("Talk to the Tax Assistant using your voice or text.")

# Text input for text output
user_input = st.text_input("Enter your query:")
if st.button("Submit Text Query"):
    if user_input:
        response = chat_session.send_message(user_input)
        st.write(response.text)

# Button to start voice input
if st.button("Start Voice Input"):
    voice_input = recognize_voice()
    if voice_input:
        response = chat_session.send_message(voice_input)
        st.write(response.text)
        speak_text(response.text)
