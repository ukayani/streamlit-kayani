import streamlit as st
import os

st.title('kayani')
st.write('Welcome to kayani!')
test = os.environ.get("GITHUB_TOKEN", 'test')[:2]
st.write(test)
