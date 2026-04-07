import streamlit as st
import random
import time

st.set_page_config(page_title="EcoIrrigate", layout="wide")

# --- ADVANCED CSS ---
st.markdown("""
<style>

/* Background gradient */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

/* Title */
.title {
    text-align: center;
    font-size: 48px;
    font-weight: 700;
    color: #00ffcc;
    margin-bottom: 10px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #cfcfcf;
    margin-bottom: 30px;
}

/* Glass card */
.card {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(15px);
    box-shadow: 0 0 30px rgba(0,255,200,0.15);
    text-align: center;
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.05);
}

/* Metric value */
.metric {
    font-size: 32px;
    font-weight: bold;
    color: #00ffcc;
}

/* Label */
.label {
    color: #bbb;
    font-size: 14px;
}

/* Status dot */
.status-on {
    color: #00ff88;
    font-size: 20px;
    font-weight: bold;
}

.status-off {
    color: #ff4b4b;
    font-size: 20px;
    font-weight: bold;
}

/* Buttons */
.stButton button {
    background: linear-gradient(90deg, #00ffcc, #00ccff);
    color: black;
    border-radius: 10px;
    height: 50px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.05);
}

</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="title">🌿 EcoIrrigate</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart Solar-Powered Irrigation Control System</div>', unsafe_allow_html=True)

# --- DATA ---
MIN_MOISTURE = 50

moisture = random.randint(20, 80)
solar = random.randint(800, 1500)
used = random.randint(200, 700)
battery = solar - used

pump = "ON" if moisture < MIN_MOISTURE else "OFF"

# --- CARDS ---
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
    <div class="label">Solar Generated</div>
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
    <div class="label">Battery Storage</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- STATUS ---
st.subheader("💧 Irrigation System Status")

if pump == "ON":
    st.markdown('<div class="status-on">🟢 Pump ACTIVE (Auto Irrigation Running)</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="status-off">🔴 Pump OFF (Soil Moisture OK)</div>', unsafe_allow_html=True)

# --- ALERT LOGIC ---
if moisture < 40:
    st.error("🚨 Critical Dry Soil! Immediate irrigation required")
elif moisture < 50:
    st.warning("⚠️ Soil drying - irrigation active")
else:
    st.success("✅ Soil moisture optimal")

# --- BATTERY BAR ---
st.subheader("🔋 Battery Status")
battery_percent = int((battery / 1500) * 100)
st.progress(min(battery_percent, 100))

# --- CONTROL PANEL ---
st.subheader("🎛 Control Panel")

col5, col6 = st.columns(2)

if col5.button("Force Start Irrigation"):
    st.success("Manual Override: Pump ON")

if col6.button("Stop Irrigation"):
    st.error("Manual Override: Pump OFF")

# --- CHART ---
st.subheader("⚡ Energy Flow")
st.area_chart({
    "Produced": [solar]*10,
    "Used": [used]*10,
    "Stored": [battery]*10
})

# --- AUTO REFRESH ---
time.sleep(2)
st.rerun()

import streamlit as st
import random
import time

st.set_page_config(page_title="EcoIrrigate", layout="wide")

# --- CUSTOM FUTURISTIC CSS ---
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

.title {
    text-align: center;
    font-size: 48px;
    font-weight: 700;
    color: #00ffcc;
}

.subtitle {
    text-align: center;
    color: #cfcfcf;
    margin-bottom: 30px;
}

.card {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(15px);
    box-shadow: 0 0 25px rgba(0,255,200,0.15);
    text-align: center;
    transition: 0.3s;
}
.card:hover {
    transform: scale(1.05);
}

.metric {
    font-size: 30px;
    font-weight: bold;
    color: #00ffcc;
}

.label {
    color: #bbb;
    font-size: 14px;
}

.status-on {
    color: #00ff88;
    font-size: 20px;
    font-weight: bold;
}

.status-off {
    color: #ff4b4b;
    font-size: 20px;
    font-weight: bold;
}

.stButton button {
    background: linear-gradient(90deg, #00ffcc, #00ccff);
    color: black;
    border-radius: 10px;
    height: 50px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="title">🌿 EcoIrrigate</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart Solar-Powered Irrigation System</div>', unsafe_allow_html=True)

# --- CONSTANTS ---
MIN_MOISTURE = 50  # for mirchi
FLOW_RATE = 10     # liters/min

# --- SIMULATED SENSOR DATA ---
moisture = random.randint(20, 80)
solar = random.randint(800, 1500)
used_energy = random.randint(200, 700)
battery = solar - used_energy

# --- AUTO IRRIGATION ---
pump = "ON" if moisture < MIN_MOISTURE else "OFF"

# --- WATER CALCULATION ---
pump_runtime = random.randint(10, 60)  # minutes today
water_used = FLOW_RATE * pump_runtime
traditional_water = int(water_used * 1.4)
water_saved = traditional_water - water_used

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
    <div class="label">Solar Generated</div>
</div>
""", unsafe_allow_html=True)

col3.markdown(f"""
<div class="card">
    <div class="metric">{used_energy} Wh</div>
    <div class="label">Energy Used</div>
</div>
""", unsafe_allow_html=True)

col4.markdown(f"""
<div class="card">
    <div class="metric">{battery} Wh</div>
    <div class="label">Battery Storage</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- WATER ANALYTICS ---
st.subheader("💧 Water Analytics (Today)")

col5, col6, col7 = st.columns(3)

col5.markdown(f"""
<div class="card">
    <div class="metric">{water_used} L</div>
    <div class="label">Water Used</div>
</div>
""", unsafe_allow_html=True)

col6.markdown(f"""
<div class="card">
    <div class="metric">{traditional_water} L</div>
    <div class="label">Traditional Usage</div>
</div>
""", unsafe_allow_html=True)

col7.markdown(f"""
<div class="card">
    <div class="metric">{water_saved} L</div>
    <div class="label">Water Saved</div>
</div>
""", unsafe_allow_html=True)

# --- STATUS ---
st.subheader("💧 Irrigation Status")

if pump == "ON":
    st.markdown('<div class="status-on">🟢 Pump ACTIVE (Auto Irrigation Running)</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="status-off">🔴 Pump OFF (Soil Moisture OK)</div>', unsafe_allow_html=True)

# --- ALERTS ---
if moisture < 40:
    st.error("🚨 Critical Dry Soil! Immediate irrigation required")
elif moisture < 50:
    st.warning("⚠️ Soil drying - irrigation active")
else:
    st.success("✅ Soil moisture optimal")

# --- BATTERY ---
st.subheader("🔋 Battery Level")
battery_percent = int((battery / 1500) * 100)
st.progress(min(battery_percent, 100))

# --- CONTROL PANEL ---
st.subheader("🎛 Control Panel")

col8, col9 = st.columns(2)

if col8.button("Force Start Irrigation"):
    st.success("Manual Override: Pump ON")

if col9.button("Stop Irrigation"):
    st.error("Manual Override: Pump OFF")

# --- WATER ANALYTICS ---
st.markdown("---")
st.markdown("## 💧 Water Analytics (Today)")

# Ensure values exist
st.write(f"DEBUG → Used: {water_used}, Traditional: {traditional_water}, Saved: {water_saved}")

col5, col6, col7 = st.columns(3)

with col5:
    st.markdown(f"""
    <div class="card">
        <div class="metric">{water_used} L</div>
        <div class="label">Water Used Today</div>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown(f"""
    <div class="card">
        <div class="metric">{traditional_water} L</div>
        <div class="label">Traditional Usage</div>
    </div>
    """, unsafe_allow_html=True)

with col7:
    st.markdown(f"""
    <div class="card">
        <div class="metric">{water_saved} L</div>
        <div class="label">Water Saved</div>
    </div>
    """, unsafe_allow_html=True)
