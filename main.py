import streamlit as st

st.title("Weather Forecast for the Next Days")
place = st.text_input(label="Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Enter the days for which you want the data")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days}"
             f" days in {place}")
