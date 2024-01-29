import streamlit as st
import plotly.express as px
from Backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input(label="Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Enter the days for which you want the data")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days}"
             f" days in {place}")

if place:
    try:
        filtered_data = get_data(place, days, option)

        if option == 'Temperature':
            temps = []
            dates = []
            for i in range(0, len(filtered_data)):
                temps.append(filtered_data[i]['main']['temp'])
                dates.append(filtered_data[i]['dt_txt'])
            figure = px.line(x=dates, y=temps, labels={"x": 'Date', 'y': "Temperature"})
            st.plotly_chart(figure)
        else:
            result = []
            for i in range(0, len(filtered_data)):
                result.append(f"images/{(filtered_data[i]['weather'][0]['main']).lower()}.png")
            st.image(result, width=115)
    except KeyError:
        st.write("Place does not exists")