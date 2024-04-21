import streamlit as st
from menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()
conn = st.connection('mysql', type='sql')
df = conn.query('SELECT * from drivers;', ttl=600)
st.title("This page is available to all users")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")
col1,col2,col3 = st.columns(3)
col1.write('First Name')
col2.write('Last Name')
col3.write('ID')


for row in df.itertuples():
    with col1:
        st.write(row.first_name)
    with col2:
        st.write(row.last_name)
    with col3:
        st.write(row.id)




st.dataframe(
    df,
    column_config={
        "first_name": "First Name"
        "last_name": "Last Name"
        "date_of_birth": "Date of Birth"
        "picture_path": "Profile Pic"


    }