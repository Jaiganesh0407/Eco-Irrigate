import streamlit as st
import random
import time

st.set_page_config(page_title="EcoIrrigate", layout="wide")

# --- CUSTOM CSS (FUTURISTIC UI) ---
st.markdown("""
<style>
body {
    background-color: #0b0f1a;
    color: white;
}

.big-title {
    font-size: 40px;
    font-weight: bold;
    color: #00ff9f;
    text-align: center;
    margin-bottom: 20px;
}

.card {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 20px;
    padding: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0 0 20px rgba(0,255,159,0.2);
    text-align: center;
}

.metric {
    font-size: 28px;
    font-weight: bold;
    color: #00ff9f;
}

.label {
    font-size: 14px;
    color: #aaa;
}

.pump-on {
    color: #00ff9f;
    font-weight: bold;
    font-size: 20px;
}

.pump-off {
    color: #ff4b4b;
    font-weight: bold;
    font-size: 20px;
}
</style>
""", unsafe_allow_html=True)

# --- TITLE ---
st.markdown('<div class="big-title">🌿 EcoIrrigate</div>', unsafe_allow_html=True)

# --- THRESHOLD ---
threshold = st.slider("Set Moisture Threshold (%)", 0, 100, 55)

# --- SIMULATED DATA ---
moisture = random.randint(20, 80)
solar = random.randint(800, 1500)
used = random.randint(200, 700)
battery = solar - used

# --- AUTO LOGIC ---
pump = "ON" if moisture < threshold else "OFF"

# --- METRIC CARDS ---
col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"""
<div class="card">
    <div class="metric">{moisture}%</div>
    <div class="label">Soil Moisture</div>
</div>
""", unsafe_allow_html=True)

col2.markdown(f"""
<div class="card">
    <div class="metric">{solar} Wh</div>
    <div class="label">Solar Energy</div>
</div>
""", unsafe_allow_html=True)

col3.markdown(f"""
<div class="card">
    <div class="metric">{used} Wh</div>
    <div class="label">Energy Used</div>
</div>
""", unsafe_allow_html=True)

col4.markdown(f"""
<div class="card">
    <div class="metric">{battery} Wh</div>
    <div class="label">Battery</div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- PUMP STATUS ---
st.subheader("💧 Irrigation Status")

if pump == "ON":
    st.markdown('<div class="pump-on">🟢 Pump ON (Auto)</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="pump-off">🔴 Pump OFF</div>', unsafe_allow_html=True)

# --- BATTERY BAR ---
st.subheader("🔋 Battery Level")
battery_percent = int((battery / 1500) * 100)
st.progress(min(battery_percent, 100))

# --- BUTTONS ---
st.subheader("🕹 Manual Control")

col5, col6 = st.columns(2)

if col5.button("Force ON"):
    st.success("Pump manually turned ON")

if col6.button("Force OFF"):
    st.error("Pump manually turned OFF")

# --- CHART ---
st.subheader("⚡ Energy Flow")
st.area_chart({
    "Produced": [solar]*10,
    "Used": [used]*10,
    "Stored": [battery]*10
})

# --- REFRESH ---
time.sleep(2)
st.rerun()
