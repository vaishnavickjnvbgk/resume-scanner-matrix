import streamlit as st

def degree():
    choice = st.text_input("enter degree",key="degree1",value="btech")
    return choice 
