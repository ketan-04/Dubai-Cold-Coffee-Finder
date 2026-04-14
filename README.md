\# ☕ Dubai Cold Coffee Finder



\## About this project



This is a simple web app that helps users find cold coffee spots in Dubai.



The idea is basic — if someone is in a particular area, they should be able to see nearby coffee places without searching manually again and again.

So I built this app where you can select an area and it shows nearby options with useful details.



\---



\## What it can do



\* You can select an area and see nearby coffee spots

\* You can filter results by distance

\* You can filter by rating to see better places

\* You can choose to see only open spots

\* You can search any place by name

\* It shows all spots on a map

\* It also shows some basic analytics like average rating

\* There is a simple leaderboard for top rated and nearest spots



\---



\## How it works



\* First, user selects an area

\* Then the app takes its latitude and longitude

\* It calculates distance between that area and all coffee spots

\* After that, filters are applied based on user input

\* Finally, results are shown using map, cards, and tables



\---



\## Technologies used



\* Streamlit for building the app

\* Pandas for handling data

\* Folium for map visualization

\* Geopy for distance calculation



\---



\## How to run



```bash id="qv8t2x"

pip install -r requirements.txt

streamlit run dubai\_web\_app.py

```



\---



\## Note



This project was created during my learning phase in data analytics.

The goal was to practice working with data, applying filters, and building a simple interactive app.



