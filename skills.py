import streamlit as st
def skills():
    choice = st.text_input("enter skills",key="skills1",value="python")
    return choice
