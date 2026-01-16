import os

import streamlit as st
from streamlit_navigation_bar import st_navbar

import pages as pg

st.set_page_config(initial_sidebar_state="collapsed")


pages = ["Home","Text to Speech", "Speech to Text", "About"]
parent_dir = os.path.dirname(os.path.abspath(__file__))
# logo_path = os.path.join(parent_dir, "cubes.svg")

styles = {
    "nav": {
        "background-color": "Grey",
        "justify-content": "center",
    },
    # "img": {
    #     "padding-right": "14px",
    # },
    "span": {
        "color": "black",
        "padding": "14px",
    },
    "active": {
        "background-color": "black",
        "color": "var(--text-color)",
        "font-weight": "normal",
        "padding": "14px",
    }
}
options = {
    "show_menu": False,
    "show_sidebar": False,
}

page = st_navbar(
    pages,
    # logo_path=logo_path,
    styles=styles,
    options=options,
)

functions = {
    "Home": pg.show_home,
    "Text to Speech": pg.tts,
    "Speech to Text": pg.stt,
    "About": pg.about
}
go_to = functions.get(page)
if go_to:
    go_to()