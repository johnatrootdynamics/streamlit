import streamlit as st
from menu import menu



conn = st.connection('mysql', type='sql')

df = conn.query('SELECT * from drivers;', ttl=600)


# Initialize st.session_state.role to None
if "role" not in st.session_state:
    st.session_state.role = None

# Retrieve the role from Session State to initialize the widget
st.session_state._role = st.session_state.role

def set_role():
    # Callback function to save the role selection to Session State
    st.session_state.role = st.session_state._role


# Selectbox to choose role
st.selectbox(
    "Select your role:",
    [None, "user", "admin", "super-admin"],
    key="_role",
    on_change=set_role,
)

for row in df.itertuples():
    st.write(f"{row.first_name} {row.last_name}:")

menu() # Render the dynamic menu!