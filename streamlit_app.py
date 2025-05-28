import streamlit
x = streamlit.slider("Select a value")
streamlit.write(x, "squared is", x * x)
