import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import japanize_matplotlib
import base64
from datetime import datetime, timedelta

# フルスクリーン
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(
    page_title="webpage of yama frog",
    layout="wide", 
    initial_sidebar_state="auto",
    page_icon=":paintbrush:"
)

st.title("『社会科学のためのモデル入門』を読む会")
st.markdown("議事録をここに載せていくかもしれない")

image = Image.open("photos/IMG_4841.png")
st.image(image)