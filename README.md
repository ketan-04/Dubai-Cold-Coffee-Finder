# ☕ Dubai Cold Coffee Finder

## Preview

![Main App View](preview-1.png)
![Analytics & Filters](preview-2.png)

---

## About this project

This is a location-based web app built to explore cold coffee spots in Dubai.

The goal of this project is to make it easier to find nearby coffee places based on a selected area.
Instead of searching manually, users can quickly view nearby options along with distance, rating, and whether the place is open or closed.

---

## What it can do

* Select an area and instantly view nearby coffee spots
* Apply distance and rating filters to narrow down results
* Check which spots are currently open
* Search for a specific place by name
* Explore all locations on an interactive map
* View simple analytics like average rating
* See top rated and nearest spots in leaderboard format

---

## How it works

* User selects an area
* The app gets its latitude and longitude
* Distance is calculated for all coffee spots
* Filters are applied based on user input
* Results are displayed using map, cards, and tables

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

This project was built as part of my data analytics learning journey.
It focuses on applying data filtering, working with location data, and building a simple interactive interface.
