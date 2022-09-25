import streamlit as st
from transformers import pipeline

st.title('Text Classification')
pipe = pipeline("text-classification")
text = st.text_area("Enter some text:")
if text:
    out = pipe(text)
    st.json(out)







