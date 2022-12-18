import streamlit as st
import send_email

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message here")
    message = f"""
    From: {user_email}
    {message} 
    """
    button = st.form_submit_button("Submit")

    if button:
        send_email.send_email(message)
        st.info("Your email has sent successfully")