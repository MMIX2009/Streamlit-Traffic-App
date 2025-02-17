import streamlit as st
import folium
from streamlit_folium import st_folium
from datetime import datetime
import pytz

API_KEY = "******************************"  # YOUR_GOOGLE_MAPS_API_KEY
headers = {
    "authorization": st.secrets["API_KEY"],
    "content-type": "application/json"
}


# City options with coordinates and timezones
cities = {
    "Abuja, Nigeria": {"coords": [9.0579, 7.4951], "timezone": "Africa/Lagos"},
    "Beijing, China": {"coords": [39.9042, 116.4074], "timezone": "Asia/Shanghai"},
    "Berlin, Germany": {"coords": [52.5200, 13.4050], "timezone": "Europe/Berlin"},
    "Brazzaville, Congo": {"coords": [-4.2634, 15.2429], "timezone": "Africa/Brazzaville"},
    "Brussels, Belgium": {"coords": [50.8503, 4.3517], "timezone": "Europe/Brussels"},
    "Buenos Aires, Argentina": {"coords": [-34.6037, -58.3816], "timezone": "America/Argentina/Buenos_Aires"},
    "Cairo, Egypt": {"coords": [30.0444, 31.2357], "timezone": "Africa/Cairo"},
    "Cape Town, South Africa": {"coords": [-33.9249, 18.4241], "timezone": "Africa/Johannesburg"},
    "Jakarta, Indonesia": {"coords": [-6.2088, 106.8456], "timezone": "Asia/Jakarta"},
    "Johannesburg, South Africa": {"coords": [-26.2041, 28.0473], "timezone": "Africa/Johannesburg"},
    "Kinshasa, DRC": {"coords": [-4.322447, 15.307045], "timezone": "Africa/Kinshasa"},
    "Kigali, Rwanda": {"coords": [-1.9706, 30.1044], "timezone": "Africa/Kigali"},
    "Kyiv, Ukraine": {"coords": [50.4501, 30.5234], "timezone": "Europe/Kiev"},
    "Lagos, Nigeria": {"coords": [6.5244, 3.3792], "timezone": "Africa/Lagos"},
    "Liege, Belgium": {"coords": [50.6333, 5.5667], "timezone": "Europe/Brussels"},
    "London, UK": {"coords": [51.5074, -0.1278], "timezone": "Europe/London"},
    "Los Angeles, USA": {"coords": [34.0522, -118.2437], "timezone": "America/Los_Angeles"},
    "Miami, USA": {"coords": [25.7617, -80.1918], "timezone": "America/New_York"},
    "Mexico City, Mexico": {"coords": [19.4326, -99.1332], "timezone": "America/Mexico_City"},
    "Moscow, Russia": {"coords": [55.7558, 37.6173], "timezone": "Europe/Moscow"},
    "Mumbai, India": {"coords": [19.0760, 72.8777], "timezone": "Asia/Kolkata"},
    "Nairobi, Kenya": {"coords": [-1.286389, 36.817223], "timezone": "Africa/Nairobi"},
    "New York, USA": {"coords": [40.7128, -74.0060], "timezone": "America/New_York"},
    "Paris, France": {"coords": [48.8566, 2.3522], "timezone": "Europe/Paris"},
    "Pretoria, South Africa": {"coords": [-25.7479, 28.2293], "timezone": "Africa/Johannesburg"},
    "San Francisco, USA": {"coords": [37.7749, -122.4194], "timezone": "America/Los_Angeles"},
    "São Paulo, Brazil": {"coords": [-23.5505, -46.6333], "timezone": "America/Sao_Paulo"},
    "Seattle, USA": {"coords": [47.6062, -122.3321], "timezone": "America/Los_Angeles"},
    "Seoul, South Korea": {"coords": [37.5665, 126.9780], "timezone": "Asia/Seoul"},
    "Sydney, Australia": {"coords": [-33.8688, 151.2093], "timezone": "Australia/Sydney"},
    "Tokyo, Japan": {"coords": [35.6895, 139.6917], "timezone": "Asia/Tokyo"},
    "Toronto, Canada": {"coords": [43.651070, -79.347015], "timezone": "America/Toronto"}
}

# Sidebar selection for city
selected_city = st.sidebar.selectbox("Select a city", list(cities.keys()))

# Get selected city's details
city_info = cities[selected_city]
map_center = city_info["coords"]
timezone = pytz.timezone(city_info["timezone"])
local_time = datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")

# Create map centered on the selected city
traffic_map = folium.Map(location=map_center, zoom_start=12)

# Add Google Maps traffic layer
google_traffic = folium.TileLayer(
    tiles=f"https://mt1.google.com/vt/lyrs=m,traffic&x={{x}}&y={{y}}&z={{z}}&key={API_KEY}",
    attr="Google Maps",
    name="Google Traffic",
    overlay=True,
    control=True
)
google_traffic.add_to(traffic_map)

# Add a layer control to toggle layers
folium.LayerControl().add_to(traffic_map)

st.title("Real-Time Traffic Heatmap with Traffic Layer")
st_folium(traffic_map, width=700, height=500)

# Display city name, local time, latitude, and longitude
st.write(f"📍 City: {selected_city}")
st.write(f"🌐 Latitude: {map_center[0]}, Longitude: {map_center[1]}")
st.write(f"🕒 Local Time: {local_time}")

# Required packages:
# pip install streamlit streamlit-folium folium pytz
