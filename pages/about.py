def about():
    import streamlit as st

    # -------- TITLE --------
    st.title("About This Project")

    # st.caption("A small project built to explore AI-powered voice applications.")

    # -------- INTRO CARD --------
    st.markdown(
        """
        <div style="
            background: rgba(255,255,255,0.08);
            padding: 20px;
            border-radius: 14px;
            margin-top: 20px;
            border: 1px solid rgba(255,255,255,0.15);
        ">
            <p>
            This project is a simple yet powerful application that lets you
            convert <b>speech into text</b> and <b>text into natural-sounding speech</b>
            using modern AI technologies.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # -------- WHAT IT DOES --------
    st.write("\n\n")
    st.markdown("## WHAT THIS APP CAN DO")

    col1, col2 = st.columns(2)

    with col1:
        st.success("🎙️ Speech to Text\n\nConvert your voice or audio files into readable text.")

    with col2:
        st.success("🔊 Text to Speech\n\nTurn written content into clear and natural audio.")

    # -------- WHY THIS PROJECT --------
    st.markdown("##  WHY THIS")


    st.markdown(
        """
        <div style="
            background: rgba(255,255,255,0.08);
            padding: 20px;
            border-radius: 14px;
            margin-top: 20px;
            border: 1px solid rgba(255,255,255,0.15);
        ">
            <p>
            I created this project to explore how Artificial Intelligence can make
            everyday tasks easier — from taking voice notes to creating audio from text.
            It helped me learn how to work with APIs, audio processing, and simple UI design.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # st.write("""
    # I created this project to explore how Artificial Intelligence can make
    # everyday tasks easier — from taking voice notes to creating audio from text.
    # It helped me learn how to work with APIs, audio processing, and simple UI design.
    # """)

    # -------- TECH STACK --------
    st.write("\n\n")
    st.markdown("##  TECHNOLOGIES USED")

    tech_col1, tech_col2 = st.columns(2)

    with tech_col1:
        st.success("• Python \n • Streamlit \n • SpeechRecognition")

    with tech_col2:
        st.success("• WhisperAI API \n • gTTS \n • Requests")    

    # -------- FUN FOOTER --------
    st.markdown("---")
    st.write("\n\n")
    st.markdown(
    "<div style='text-align:center;'>This is a personal project created to explore AI and voice-based applications.</div>",
    unsafe_allow_html=True
    )
    st.write("\n\n")
    st.markdown(
        """
        <div style="text-align:center; font-size:14px; opacity:0.85;">
            <p>🔗 <b>Connect with me</b></p>
            <p>
                <a> piyabharwani.31@gmail.com</a> |
                <a href="www.linkedin.com/in/piya-bharwani-9888a3305" target="_blank">LinkedIn</a> |
                <a href="https://github.com/piya-b31?tab=repositories" target="_blank">GitHub</a> 
            </p>
        </div>
        """,
        unsafe_allow_html=True
        )

