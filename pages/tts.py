
def tts():
    import streamlit as st
    from gtts import gTTS

    st.title("🔊 Text to Speech")

    # -------- OPTION 1: TYPE TEXT --------
    st.subheader("Type your text")
    text_input = st.text_area("Enter text to convert into speech")

    # -------- OPTION 2: UPLOAD TEXT FILE --------
    st.subheader("Or upload a text file")
    uploaded_txt = st.file_uploader("Upload a .txt file", type=["txt"])

    final_text = ""

    # If user typed text
    if text_input.strip():
        final_text = text_input

    # If user uploaded file
    if uploaded_txt is not None:
        file_text = uploaded_txt.read().decode("utf-8")
        final_text = file_text
        st.success("Text file loaded successfully!")
        st.text_area("File Content", final_text, height=150)

    # -------- CONVERT TO SPEECH --------
    if st.button("Convert to Speech"):
        if final_text.strip() == "":
            st.warning("Please type text or upload a text file first.")
        else:
            tts = gTTS(text=final_text, lang="en")
            tts.save("voice.mp3")

            st.success("Speech generated!")

            with open("voice.mp3", "rb") as f:
                audio_bytes = f.read()

            st.audio(audio_bytes, format="audio/mp3")

            st.download_button(
                label="Download Audio",
                data=audio_bytes,
                file_name="voice.mp3",
                mime="audio/mp3"
            )
