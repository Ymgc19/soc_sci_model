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

st.title("二章の章末問題に関して")
st.markdown("##### 1問目")
st.markdown("")