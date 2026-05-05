import os
import streamlit as st
from streamlit_option_menu import option_menu

import pages as pg

st.set_page_config(initial_sidebar_state="collapsed")

# Custom CSS to style the nav bar like your original
st.markdown("""
    <style>
        /* Hide default streamlit sidebar toggle */
        [data-testid="collapsedControl"] { display: none; }
        
        /* Nav bar styling */
        .nav-container {
            background-color: grey;
        }
    </style>
""", unsafe_allow_html=True)

# Navigation bar
page = option_menu(
    menu_title=None,
    options=["Home", "Text to Speech", "Speech to Text", "About"],
    icons=["house", "volume-up", "mic", "info-circle"],
    orientation="horizontal",
    styles={
        "container": {
            "padding": "0px",
            "background-color": "grey",
            "justify-content": "center",
        },
        "nav-link": {
            "color": "black",
            "padding": "14px",
            "font-size": "15px",
        },
        "nav-link-selected": {
            "background-color": "black",
            "color": "white",
            "font-weight": "normal",
        },
    }
)

# Page routing
functions = {
    "Home": pg.show_home,
    "Text to Speech": pg.tts,
    "Speech to Text": pg.stt,
    "About": pg.about,
}

go_to = functions.get(page)
if go_to:
    go_to()
