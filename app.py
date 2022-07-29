import streamlit as st
import string as str
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch.nn.functional as F
from random import randint, seed
import math
import pickle 
import re

# https://github.com/AlekseyKorshuk/huggingartists
# List: https://huggingface.co/huggingartists

st.title("Lyrical")

ARTIST_STYLE = st.selectbox('Artist Name',(
    'kendrick-lamar',
    'kanye-west',
    'nf',
    'eminem',
    'coldplay',
    'drake',
    'kota-the-friend',
    'kanye-west',
    'snoop-dogg',
    'billie-eilish',
    'logic',
    'lil-uzi-vert',
    'juice-wrld',
    'snoop-dogg',
    'distilgpt-2',
    'gpt2',
    'gpt2-medium',
    'gpt2-large',
    'gpt2-medium',
    'gpt2-xl',
    ))
MOTIVATION = st.text_input("Lyrics","")
if ARTIST_STYLE and MOTIVATION:
    st.write("Output " + str(ARTIST_STYLE))
    st.write("Output " + str(MOTIVATION))


