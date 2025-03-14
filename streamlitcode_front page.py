import streamlit as st


st.markdown("<h1 style='text-align: center;'>Welcome to my website</h1>", unsafe_allow_html=True)

input_1 = st.text_input('Enter your user name:')
input_2 = st.text_input('Enter your password:')

if st.button('Submit'):
    if len(input_1)==12 and len(input_2)==10:
        st.markdown(f"<h2 style='text-align: center;'>You entered: {input_1} and {input_2}</h2>", unsafe_allow_html=True)
    else:
        st.error("Please fill in both fields before submitting.")
