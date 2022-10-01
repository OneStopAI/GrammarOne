import streamlit as st


st.title("Grammar One")

tab1, tab2, tab3, tab4 = st.tabs(["Spell check", "Text summarization", "Auto-complete", "Grammar correction"])

with tab1:
    st.header("Spell check")

with tab2:
    st.header("Text summarization")

with tab3:
    st.header("Auto-complete")

with tab4:
    st.header("Grammar correction")