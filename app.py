import streamlit as st
import pandas as pd

st.title("Lyrical")
name = st.text_input("Lyrics","")
st.write("Output " + str(name))


