import streamlit as st



tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab2", "Tab3"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")
tab3.write("This is tab 3")

# You can also use "with" notation:
with tab1:
    st.write("Most objects") # df, err, func, keras!
    st.write(["st", "is <", 3]) # see *

    st.text("Fixed width text")
    st.markdown("_Markdown_") # see *
    st.latex(r""" e^{i\pi} + 1 = 0 """)
    st.title("My title")
    st.header("My header")
    st.subheader("My sub")
    st.code("for i in range(8): foo()")

with tab2:
    expand = st.expander("My label")
    expand.write("Inside the expander.")
    pop = st.popover("Button label")
    pop.checkbox("Show all")

# You can also use "with" notation:
    with expand:
        st.radio("Select one:", [1, 2])
with tab3:
    data = "123"
    url = "123"
    st.button("Click me")
    st.download_button("Download file", data)
    st.link_button("Go to gallery", url)
    st.page_link("app.py", label="Home")
    #st.data_editor("Edit data", data)
    st.checkbox("I agree")
    st.toggle("Enable")
    st.radio("Pick one", ["cats", "dogs"])
    st.selectbox("Pick one", ["cats", "dogs"])
    st.multiselect("Buy", ["milk", "apples", "potatoes", "Gapplebees"])
    st.slider("Pick a number", 0, 100)
    st.select_slider("Pick a size", ["S", "M", "L"])
    st.text_input("First name")
    st.number_input("Pick a number", 0, 10)
    st.text_area("Text to translate")
    st.date_input("Your birthday")
    st.time_input("Meeting time")
    st.file_uploader("Upload a CSV")
    st.camera_input("Take a picture")
    st.color_picker("Pick a color")