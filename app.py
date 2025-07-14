import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
st.set_page_config(
    page_title="My Cool App",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="expanded",
)


# Matplotlib
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)


df = pd.DataFrame({
    "name": ["John", "Jane", "Jim", "Jill"],
    "age": [25, 30, 35, 40],
    "city": ["New York", "Los Angeles", "Chicago", "Houston"],
    "score": [85, 90, 95, 100]
})

st.dataframe(df)
st.metric(label="Temperature", value="70 °F", delta="+2 °F")
if st.button("Click Me"): st.write("Clicked!")
if st.checkbox("Show data"): st.write(df)
options = st.multiselect("Select:", df['name'])
st.line_chart(df["age"])
value = st.slider("Range", 0, 100, 50)
num = st.number_input("Enter number:", 0, 10)
st.bar_chart(df["age"])
st.area_chart(df["age"])
st.scatter_chart(df["age"])

st.table(df)

st.sidebar.title("This is a sidebar")
score_filter = st.slider("Minimum Score:", 0, 100, 50)
filtered_df = df[df["score"] >= score_filter]
st.dataframe(filtered_df)
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Column 1")
    st.button("Press me!")

with col2:
    st.header("Column 2")
    st.write("Text here.")

tab1, tab2 = st.tabs(["Tab One", "Tab Two"])

with tab1:
    st.title("Home page")
    st.header("This is a headersss")
    st.subheader("This is a subheader")
    st.markdown("This is a markdown")
    st.text("This is a text")


with tab2:
    st.write("Content of Tab Two.")




st.text_input("Enter your name")
st.number_input("Enter your age")
st.text_area("Enter your message")
st.selectbox("Select your gender", ["Male", "Female", "Other"])
st.multiselect("Select your hobbies", ["Reading", "Writing", "Coding", "Other"])
st.checkbox("Do you want to subscribe to our newsletter?")
st.radio("Select your gender", ["Male", "Female", "Other"])
st.date_input("Enter your date of birth")
st.time_input("Enter your time")
st.file_uploader("Upload your file")
st.color_picker("Select your color")
st.code("print('Hello World')")

with st.form("This is a form"):
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age")
    submit = st.form_submit_button("Submit")

if submit:
    st.text(f"Hello {name} you are {age} years old")







