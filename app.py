import streamlit as st



tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")

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