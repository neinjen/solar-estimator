# 🔆 Solar Energy Estimator  
### Real-time Photovoltaic Yield Modeling for Linköping, Sweden

🚀 **Live Demo:** [https://solar-estimator-xec3nwtmnb89alfw6kzbu8.streamlit.app/]

## 📌 Overview
This project is a **Solar Energy Estimation Tool** designed specifically for **Linköping, Sweden**.

By integrating real-time meteorological data from the **OpenWeatherMap API**, the application estimates the potential electricity generation of a photovoltaic (PV) system based on:

- Cloud coverage  
- Ambient temperature  
- Seasonal sunlight patterns  

The project demonstrates the application of:

- Environmental modeling  
- Statistical uncertainty estimation  
- Real-time API integration  
- Interactive web deployment using **Streamlit**

---

## 🚀 Key Features

### Real-time API Integration
Fetches live weather data including cloudiness, temperature, and sunrise/sunset times using the **OpenWeatherMap API**.

### Dynamic DNI Modeling
Implements a **Direct Normal Irradiance (DNI)** estimation algorithm that adjusts solar radiation according to cloud opacity.

### Statistical Robustness
Uses a **Log-Normal distribution** to estimate a **95% prediction interval**, capturing uncertainty in solar power generation.

### Localized Solar Logic
Designed for **Northern European latitudes**, using a custom **monthly sunlight-hour coefficient matrix**.

### User-Centric Interface
Displays results in an intuitive format by converting estimated electricity output into **hours of electricity supported for a typical household**.

---

## 🛠️ Technical Stack

**Programming Language**

- Python

**Framework**

- Streamlit (Frontend & Deployment)

**Libraries**

- NumPy (Statistical modeling)

**Data Source**

- OpenWeatherMap API (Meteorological JSON data)

---

## 🧬 Estimation Methodology

The model estimates PV energy production by simulating the interaction between **atmospheric conditions and panel characteristics**.

---

### 1️⃣ Solar Irradiance Calculation

The estimated **Direct Normal Irradiance (DNI)** is computed as:

$$
DNI_{est} = DNI_{clear} \times \max\left(0, 1 - \alpha \cdot \frac{Cloud\%}{100}\right)
$$

Where:

- $DNI_{clear}$ = clear-sky irradiance  
- $\alpha = 0.8$ = cloud attenuation coefficient  
- $Cloud\%$ = cloud coverage percentage  

---

### 2️⃣ Energy Production Formula

The estimated energy output is:

$$
E = \frac{DNI_{est} \times Area_{total} \times \eta \times t_{sun}}{1000}
$$

Where:

- $Area_{total}$ = total panel area  
- $\eta$ = panel efficiency (default **18%**)  
- $t_{sun}$ = monthly weighted sunlight hours  

---

### 3️⃣ Uncertainty Analysis

To provide statistical transparency, the model estimates a **95% prediction interval** using a **log-normal distribution**:

$$
Interval = e^{\mu \pm 1.96\sigma}
$$

Where:

- $\mu$ = log-transformed expected energy output  
- $\sigma = 0.1$ = assumed standard deviation  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/solar-energy-estimator.git
cd solar-energy-estimator
