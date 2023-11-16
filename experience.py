import streamlit as st

def total_exp():
    skill_choice=[]
    choice = st.text_input("enter experience",key="experience1")
    skill_choice.append(choice)
    return skill_choice 
