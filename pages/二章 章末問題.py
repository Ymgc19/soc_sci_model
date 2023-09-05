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

st.title("2章の章末問題に関して")
st.markdown("#### 1問目")
st.markdown("##### a ")
st.markdown("##### b")
st.markdown("生徒会になる前は「ぶっ潰してやる」とか言うけど，実際に生徒会に入ったら中庸になる．")
st.markdown("権力を持つにつれて異なる意見に接触する機会が減って，意見を変えにくくなる．けど，委員会とかでは他の意見に接触する機会が増えて，意見を変えやすくなる．")
st.markdown("福祉問題よりも外交の方が責任が重いので，上院のが外務員のメンバーの方が極端な意見を持つ．")
st.markdown("上院6年，下院2年．任期")