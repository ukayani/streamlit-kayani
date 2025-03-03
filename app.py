import streamlit as st
import os

st.title('kayani')
st.write('Welcome to kayani!')
secret = os.environ.get('GITHUB_TOKEN')[:2]
st.write(secret)
