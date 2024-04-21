import streamlit as st
from menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()
df = conn.query('SELECT * from drivers;', ttl=600)
st.title("This page is available to all users")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")

for row in df.itertuples():
    st.write(f"{row.first_name} {row.last_name}:")