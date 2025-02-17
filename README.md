# Real-Time Traffic Heatmap App

## Overview
This Streamlit application provides a real-time traffic heatmap with a user-friendly interface to select cities across the world. It utilizes the Google Maps Traffic Layer to display traffic conditions and shows the local time, latitude, and longitude for the selected city.

## Features
- **Interactive Map**: Displays a map centered on the selected city.
- **Global City Selection**: Choose from a wide range of cities from different continents.
- **Real-Time Traffic Data**: Integrates with Google Maps to display live traffic information.
- **Local Time Display**: Shows the current time for the selected city.
- **Geolocation Information**: Displays the latitude and longitude coordinates of the chosen location.

## How It Works
1. **Sidebar City Selector**: Users select a city from the dropdown menu in the sidebar.
2. **Map Rendering**: The map is updated to show the chosen city's location.
3. **Traffic Layer**: Google Maps' traffic tiles are loaded on the map.
4. **Time Display**: The local time for the selected city is retrieved and displayed.
5. **Coordinate Display**: Latitude and longitude values are presented to the user.

## Technologies Used
- **Streamlit**: For the web interface.
- **Folium**: For map rendering.
- **Google Maps API**: For traffic data.
- **pytz**: For timezone management.

## Installation
```bash
pip install streamlit streamlit-folium folium pytz
```

## Usage
1. Obtain a Google Maps API key.
2. Update the `API_KEY` variable in the code.
3. Run the application with:
```bash
streamlit run app.py
```

## City List
The app includes cities like Kinshasa, New York, London, Tokyo, Sydney, Paris, Berlin, Moscow, Beijing, Mumbai, São Paulo, Cape Town, Mexico City, Buenos Aires, Cairo, Lagos, Jakarta, Seoul, Toronto, Nairobi, Pretoria, Johannesburg, Kigali, Brazzaville, Abuja, Brussels, Liege, Kyiv, Seattle, Miami, Los Angeles, and San Francisco.
