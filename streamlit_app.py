import streamlit as st
from app.main import run_app

st.title("A Biography of a Pixel 👾")
st.write("Interactive examples & history from Alvy Ray Smith's [\"A Biography of the Pixel\"](https://www.alvyray.com/DigitalLight/).")

run_app()

st.divider()

st.subheader("Credits")
st.markdown(
    """
- “A Biography of the Pixel” book: https://www.alvyray.com/DigitalLight/  
- History of Computer Graphics (CG): https://www.cs.cmu.edu/~ph/nyit/masson/history.htm  
- "Pixel: A Biography" article: https://aeon.co/essays/a-biography-of-the-pixel-the-elementary-particle-of-pictures
    """
)