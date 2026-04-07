import streamlit as st
import random
import time

st.set_page_config(page_title="EcoIrrigate", layout="wide")

st.title("🌿 EcoIrrigate - Smart Solar Drip Irrigation System")

# --- USER INPUT (Threshold Control) ---
threshold = st.slider("Set Moisture Threshold (%)", 0, 100, 60)

# --- Simulated Sensor Data ---
moisture = random.randint(20, 80)
solar_produced = random.randint(800, 1500)
energy_used = random.randint(200, 700)
battery_level = solar_produced - energy_used

# --- AUTO IRRIGATION LOGIC ---
if moisture < threshold:
    pump_status = "ON"
else:
    pump_status = "OFF"

# --- DISPLAY METRICS ---
col1, col2, col3, col4 = st.columns(4)

col1.metric("🌱 Current Moisture (%)", moisture)
col2.metric("☀️ Solar Energy Produced (Wh)", solar_produced)
col3.metric("⚡ Energy Used (Wh)", energy_used)
col4.metric("🔋 Battery Storage (Wh)", battery_level)

st.markdown("---")

# --- IRRIGATION STATUS ---
st.subheader("💧 Irrigation Status")

if pump_status == "ON":
    st.success(f"Pump is ON (Moisture {moisture}% < Threshold {threshold}%)")
else:
    st.error(f"Pump is OFF (Moisture {moisture}% ≥ Threshold {threshold}%)")

st.markdown("---")

# --- MANUAL OVERRIDE ---
st.subheader("🕹 Manual Control (Override Auto)")

col5, col6 = st.columns(2)

if col5.button("Force ON"):
    st.success("Pump manually turned ON")

if col6.button("Force OFF"):
    st.error("Pump manually turned OFF")

st.markdown("---")

# --- ENERGY CHART ---
st.subheader("⚡ Energy Overview")
st.bar_chart({
    "Produced": solar_produced,
    "Used": energy_used,
    "Stored": battery_level
})

# --- MOISTURE TREND ---
st.subheader("🌱 Moisture Trend")
st.line_chart([random.randint(20, 80) for _ in range(10)])

# --- AUTO REFRESH ---
time.sleep(2)
st.rerun()
