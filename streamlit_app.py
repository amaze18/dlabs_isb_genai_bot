from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import openai
#from qa import answer_question

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

print("ISB Dlabs Chat Bot") 

import os
SECRET_TOKEN=os.getenv('SECRET_TOKEN')
st.write("secret_token::",SECRET_TOKEN) 
openai.api_key = SECRET_TOKEN

st.write(openai.api_key)
