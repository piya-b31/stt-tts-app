import streamlit as st
from groq import Groq
import os
import tempfile
import speech_recognition as sr

r = sr.Recognizer()

# Safe way - won't crash if secrets file missing
try:
    api_key = st.secrets["GROQ_API_KEY"]
except:
    api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

def stt():
    st.title("🎙️ Speech to Text App")

    # --- MIC SECTION ---
    st.subheader("Speak & Transcribe")

    if st.button("Start Recording"):
        try:
            import speech_recognition as sr
            r = sr.Recognizer()
            with sr.Microphone() as source:
                st.info("Listening... Please speak now")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=7)
            try:
                text = r.recognize_google(audio)
                st.success(f"You said: {text}")
            except sr.UnknownValueError:
                st.error("Sorry, could not understand the audio.")
            except sr.RequestError:
                st.error("Could not connect to Google Speech service.")
        except OSError:
            st.warning(" Microphone is not available on Streamlit Cloud. Please use the **Upload Audio** section below instead.")
        except Exception as e:
            st.warning(" Microphone is not available on Streamlit Cloud. Please use the **Upload Audio** section below instead.")

    # --- FILE UPLOAD SECTION ---
    st.subheader("📁 Upload Audio")

    audio_file = st.file_uploader(
        "Choose an audio file",
        type=["mp3", "wav", "m4a", "mp4", "mpeg4"]
    )

    if audio_file and st.button("Transcribe audio"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            tmp.write(audio_file.read())
            tmp_path = tmp.name

        with st.spinner("Transcribing..."):
            try:
                with open(tmp_path, "rb") as f:
                    result = client.audio.transcriptions.create(
                        model="whisper-large-v3",
                        file=f,
                    )
                st.success(" Transcription:")
                st.write(result.text)
            except Exception as e:
                st.error(f"Failed to transcribe: {str(e)}")
            finally:
                os.unlink(tmp_path)  # Clean up temp filev
