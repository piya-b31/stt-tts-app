def show_home():
    import streamlit as st

    # ---------------- TITLE ----------------
    st.markdown("# 🏠 :rainbow[AI Voice Assistant]")

    # ---------------- DESCRIPTION ----------------
    st.write("""
    Welcome to the AI Voice Assistant — an intelligent application that helps you
    convert speech into text and text into natural-sounding speech using AI.
    """)

    # ---------------- STYLES ----------------
    st.markdown(
        """
        <style>
        .box-container {
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-top: 40px;
        }
        .nav-box {
            width: 260px;
            height: 160px;
            border-radius: 16px;
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .nav-box:hover {
            transform: translateY(-6px);
            background: rgba(255, 255, 255, 0.15);
        }
        .nav-title {
            font-size: 22px;
            font-weight: 700;
        }
        .nav-sub {
            font-size: 14px;
            opacity: 0.8;
            margin-top: 6px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # ---------------- BOXES (UI) ----------------
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="nav-box">
                <div class="nav-title">🔊 Text to Speech</div>
                <div class="nav-sub">Convert text into natural voice</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="nav-box">
                <div class="nav-title">🎙️ Speech to Text</div>
                <div class="nav-sub">Convert your voice into text</div>
            </div>
            """,
            unsafe_allow_html=True
        )
