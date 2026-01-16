def stt():
    import streamlit as st
    import speech_recognition as sr
    import requests

    st.title("🎙️ Speech to Text App")

    r = sr.Recognizer()

    # -------------------- LIVE SPEECH --------------------
    st.subheader("Speak & Transcribe")

    if st.button("Start Recording"):
        with sr.Microphone() as source:
            st.info("Listening... Please speak now")
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            st.success("Transcription:")
            st.write(text)
        except sr.UnknownValueError:
            st.error("Sorry, could not understand the audio.")
        except sr.RequestError:
            st.error("API unavailable. Check your internet connection.")

    # -------------------- FILE UPLOAD --------------------
    st.subheader("Upload Audio")

    WHISPER_URL = "https://platform.qubrid.com/api/v1/qubridai/audio/transcribe"
    HEADERS = {
        "Authorization": "Bearer k_55416db50a74.eANgqtFuzkwspG2Z8hsgFYEDYlLUWDLUdwd3CBW4xMiO6jvJaDupZw"
    }

    uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3", "m4a"])

    if uploaded_file is not None:
        with open("temp_audio.mp3", "wb") as f:
            f.write(uploaded_file.read())

        if st.button("Transcribe audio"):
            with st.spinner("Whisper is transcribing..."):
                files = {"file": open("temp_audio.mp3", "rb")}
                data = {"model": "openai/whisper-large-v3"}

                response = requests.post(
                    WHISPER_URL,
                    headers=HEADERS,
                    files=files,
                    data=data
                )

            if response.status_code == 200:
                result = response.json()
                st.success("Transcription:")
                st.write(result["text"])
            else:
                st.error("Failed to transcribe audio with Whisper API.")
