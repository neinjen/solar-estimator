import streamlit as st
import requests
from datetime import datetime
import numpy as np

# Fixed location: Linköping, Sweden
API_KEY = '9b46710c71ae7f6ab5722ff013507c9a'
CITY = 'Linköping'
COUNTRY = 'SE'
PANEL_EFFICIENCY = 0.18
CLOUD_ALPHA = 0.8
DNI_MODE = 'avg'
DNI_CLEAR = 600 if DNI_MODE == 'avg' else 1000
month_to_sunlight = {1: 1.0, 2: 2.0, 3: 3.5, 4: 4.5, 5: 5.5, 6: 6.0, 7: 6.5, 8: 5.5, 9: 4.0, 10: 3.0, 11: 2.0, 12: 1.0}

def estimate_dni(clouds, dni_clear=600, alpha=0.8):
    return dni_clear * max(0.0, 1 - alpha * (clouds / 100))

# UI
st.title("🔆 Solar Energy Estimator – Linköping, Sweden")

num_panels = st.number_input("Number of solar panels", min_value=1, value=5)
area_per_panel = st.number_input("Area of each panel (m²)", min_value=0.1, value=1.6)

if st.button("Estimate Energy"):
    total_area = num_panels * area_per_panel
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY},{COUNTRY}&appid={API_KEY}&units=metric"
    res = requests.get(url).json()

    if 'main' not in res:
        st.error("Failed to fetch weather data.")
    else:
        clouds = res['clouds']['all']
        temp = res['main']['temp']
        weather = res['weather'][0]['main']
        sunrise = datetime.utcfromtimestamp(res['sys']['sunrise'] + res['timezone'])
        sunset = datetime.utcfromtimestamp(res['sys']['sunset'] + res['timezone'])
        month = datetime.now().month
        sunlight_hours = month_to_sunlight[month]

        dni = estimate_dni(clouds, DNI_CLEAR, CLOUD_ALPHA)
        energy_kwh = dni * total_area * PANEL_EFFICIENCY * sunlight_hours / 1000

        mu_ln = np.log(energy_kwh + 1e-6)
        sigma_ln = 0.1
        lower = np.exp(mu_ln - 1.96 * sigma_ln)
        upper = np.exp(mu_ln + 1.96 * sigma_ln)

        hours = (energy_kwh / 6) * 24
        percent = (energy_kwh / 6) * 100

        st.markdown(f"### 📍 Linköping, Sweden")
        st.write(f"🌤 Weather: {weather} | ☁️ Cloudiness: {clouds}% | 🌡 Temp: {temp:.1f}°C")
        st.write(f"🌅 Sunrise: {sunrise.strftime('%H:%M')} | 🌇 Sunset: {sunset.strftime('%H:%M')}")
        st.write(f"🔋 Estimated production: **{energy_kwh:.2f} kWh**")
        st.write(f"📉 95% Prediction Interval: **{lower:.2f} ~ {upper:.2f} kWh**")
        st.write(f"⏱ Can support: **{hours:.1f} hours** of electricity")
        st.write(f"📈 Covers about: **{percent:.1f}%** of average daily use")
