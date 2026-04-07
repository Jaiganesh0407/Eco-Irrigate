
import streamlit as st
import random
import time

st.set_page_config(page_title="EcoIrrigate", layout="wide")

st.title("🌿 EcoIrrigate - Smart Solar Drip Irrigation System")

# Simulated data (replace with API later)
data = {
    "moisture": random.randint(30, 80),
    "solar_produced": random.randint(800, 1500),
    "energy_used": random.randint(200, 700),
    "battery_level": random.randint(300, 900),
    "pump": random.choice(["ON", "OFF"])
}

col1, col2, col3, col4 = st.columns(4)

col1.metric("🌱 Soil Moisture (%)", data["moisture"])
col2.metric("☀️ Solar Energy Produced (Wh)", data["solar_produced"])
col3.metric("⚡ Energy Used (Wh)", data["energy_used"])
col4.metric("🔋 Battery Storage (Wh)", data["battery_level"])

st.markdown("---")

st.subheader("💧 Irrigation Control")

if data["pump"] == "ON":
    st.success("Pump is ON")
else:
    st.error("Pump is OFF")

if st.button("Turn ON Pump"):
    st.success("Pump turned ON (simulated)")

if st.button("Turn OFF Pump"):
    st.error("Pump turned OFF (simulated)")

st.markdown("---")

st.subheader("⚡ Energy Overview")
energy_data = {
    "Produced": data["solar_produced"],
    "Used": data["energy_used"],
    "Stored": data["battery_level"]
}
st.bar_chart(energy_data)

st.subheader("🌱 Soil Moisture Trend")
st.line_chart([random.randint(30, 80) for _ in range(10)])

time.sleep(2)
st.rerun()
