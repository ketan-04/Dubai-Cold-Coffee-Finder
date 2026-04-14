# ☕ Dubai Cold Coffee Finder

## Preview

![App Screenshot](Preview 1.png)
![App Screenshot](Preview 2.png)

---

## About this project

This is a simple location-based web app to find cold coffee spots in Dubai.

The goal of this project is to make it easier to explore nearby coffee places based on a selected area.
Instead of searching manually, users can quickly see nearby options along with distance, rating, and whether the place is open or closed.

---

## What it can do

* Select an area and view nearby coffee spots
* Filter places based on distance
* Filter by rating to find better options
* Show only currently open spots
* Search for a specific place by name
* View all spots on an interactive map
* See basic analytics like average rating
* Check top rated and nearest spots

---

## How it works

* User selects an area
* The app gets its latitude and longitude
* Distance is calculated for all coffee spots
* Filters are applied based on user input
* Results are shown using map, cards, and tables

---

## Technologies used

* Streamlit – for building the web app
* Pandas – for data handling
* Folium – for map visualization
* Geopy – for distance calculation

---

## How to run

```bash
pip install -r requirements.txt
streamlit run dubai_web_app.py
```

---

## Note

This project was created during my data analytics learning phase.
It helped me understand data filtering, basic geolocation logic, and building a simple interactive app.
