import streamlit as st
import string as str
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch.nn.functional as F
from random import randint, seed
import math
import pickle 
import re

st.title("Lyrical")
name = st.text_input("Lyrics","")
st.write("Output " + str(name))


