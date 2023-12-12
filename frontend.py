import streamlit as st

# Define constants
MIN_MOISTURE_LEVEL = 400
INTERVAL = 60
PUMP_DURATION = 30
WIFI_SSID = "YOUR_WIFI_SSID"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"

# Connect to ESP8266
client = wifi.ESP8266Client(ssid=WIFI_SSID, password=WIFI_PASSWORD)

# Create layout
st.title("Smart Irrigation System")

# On/Off switch
is_on = st.checkbox("Turn on irrigation system", value=False)

# Humidity level slider
humidity_level = st.slider("Target humidity level", min_value=0, max_value=100, value=50)

# Pump duration slider
pump_duration = st.slider("Pump duration (seconds)", min_value=1, max_value=60, value=PUMP_DURATION)

# Interval slider
interval = st.slider("Interval between checks (minutes)", min_value=1, max_value=60, value=INTERVAL)

# Send control commands to ESP8266
if is_on:
  # Send command to turn on pump
  client.send_command(f"digitalWrite({relayPin}, HIGH);")
  # Wait for pump duration
  time.sleep(pump_duration)
  # Send command to turn off pump
  client.send_command(f"digitalWrite({relayPin}, LOW);")

# Show current moisture level
moisture_level = client.get_moisture_level()
st.write(f"Current moisture level: {moisture_level}")

# Show target humidity level
st.write(f"Target humidity level: {humidity_level}")

# Show pump duration
st.write(f"Pump duration: {pump_duration} seconds")

# Show interval
st.write(f"Interval between checks: {interval} minutes")
