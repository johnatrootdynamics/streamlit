import streamlit as st



tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")

# You can also use "with" notation:
with tab1:
    st.write("Most objects") # df, err, func, keras!
    st.write(["st", "is <", 3]) # see *
    st.write_stream(my_generator)
    st.write_stream(my_llm_stream)

    st.text("Fixed width text")
    st.markdown("_Markdown_") # see *
    st.latex(r""" e^{i\pi} + 1 = 0 """)
    st.title("My title")
    st.header("My header")
    st.subheader("My sub")
    st.code("for i in range(8): foo()")

with tab2:
    st.radio("Select one", [3,5,6,7])