import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import folium 
from streamlit_folium import st_folium
from geopy.distance import geodesic
from helper.utils import calculate_distance , is_open_spot , rating_star , get_spot_type_icon


df_areas = pd.read_csv("Datasets/dubai_areas_label.csv")
df = pd.read_csv("Datasets/dubai_cold_coffee_spots_clean.csv")


### --------------  PAGE TITLE----------------
st.set_page_config(page_title="Dubai Cold Coffee Finder" , page_icon="☕" , layout="wide")
st.title("☕ Dubai Cold Coffee Finder")

st.write("Find the nearest cold coffee spots around you in Dubai.")
st.write("Explore cafes, carts, and trucks based on distance, rating, and availability.")
# st.caption("Explore cafes, carts, and trucks based on distance, rating, and availability.")

st.header("📍 Select Your Area")

area_labels=list(df_areas['Label'])
# area_labels.insert(0,"Select")
# area_labels = df_areas["Label"]

## ------------DROPWDOWN---------------
selected_area = st.selectbox("Choose your area", area_labels)

## ------------ SIDE BAR---------------

with st.sidebar:
    st.header("🔍 Search & Filters")
    # st.write("Search by name")
    '''Search Input'''
    spot_name= st.text_input("Search By Name" , placeholder="eg. Al Safa")
    # Line divide
    st.divider()
    
    st.header("⚙️ Filters")
    '''Search Input'''
    options = list(df['type'].unique())
    options.insert(0,"All")
    '''Spot Type'''
    spot_type_selection= st.selectbox("Spot Type" ,  options)
    
    '''Min & Max Distance'''
    max_distance= st.slider("Max Distance (km)", min_value=1 , max_value=20 , value=10)
    
    '''Rating'''
    min_Rating = st.slider("Min Rating" , min_value=1.0 , max_value=5.0 , value=3.0, step=0.1)
    
    '''Checkbox'''
    show_only_open = st.checkbox("Show only open spots",False)
    
    '''Sort By'''
    sort_by = st.radio("Sort By", ["Distance" , "Rating"] )
    

''' Filters '''
# USER LOCATION
ss = df_areas[df_areas['Label'] == selected_area][["lat" , "lng"]]
user_location = tuple(ss.iloc[0])

# 1.distance Calculation
def get_row(row):
    return calculate_distance(user_location , row)

df["distance_km"] = df.apply(get_row , axis=1)

# Open Status
df["is_open"]=df.apply(is_open_spot , axis=1)

''' Copy Dataset '''
df2= df.copy()

#2.Spot type selection
if spot_type_selection != "All":
    df = df[df["type"] == spot_type_selection]

#3. Distance
df=df[df['distance_km'] <= max_distance]

#4. Rating
df=df[df['rating'] >=min_Rating]

#5. show only open
if show_only_open:
    df = df[df["is_open"] == "Open"]
    
#6. Sort By
if sort_by == "Distance":
    df = df.sort_values(by= "distance_km")
else:
    df = df.sort_values(by="rating" , ascending=False)
    
#7.Search by name 
if spot_name:
    df = df[df['name'].str.contains(spot_name , case=False) ]
    

##------------Tab Creation---------------  
tab1,tab2,tab3=st.tabs(["🗺️ Nearby Spots" , "📊 Analytics" , "🏆 Leaderboard"]) 

with tab1:
    
    st.subheader(f"{len(df)} spot(s) found")### No. of spots
    
    
    
# --------------MAP---------------------------------------------------
    dubai_map=folium.Map(location=user_location ,
                         zoom_start=14)
    marker_icon = folium.Icon(color="red" ,
                              icon="user")
    
    # marker for user location
    area_marker = folium.Marker( user_location , 
                                icon= marker_icon , 
                                tooltip=f"Area: {selected_area}")
    area_marker.add_to(dubai_map)
    # to  iterate all the rows in dataset one by one 
    for data in df.iterrows(): #df.iterrows tuple format me value deta h (0 [index], data in series)
        row = data[1]
        lat = row['lat']
        lng = row['lng']
        name =row["name"]
        spot_type= row["type"]
        is_open = row['is_open']
        color = "green"
        if is_open=="close":
            color = "red"
        
        spot_location = (lat,lng)
        spot_icon = folium.Icon(color=color , 
                                icon="coffee" ,
                                prefix="fa")
        #marker for spots
        marker = folium.Marker(spot_location , 
                               icon=spot_icon , 
                               tooltip=f"{spot_type} : {name} ")
        marker.add_to(dubai_map)
    
    # to show the map on web app  
    st_folium(dubai_map ,
              height=300 , 
              use_container_width=True )
   
    '''CARDS'''
    for i in range(0,len(df) , 2):
        small_df = df.iloc[i:i+2]
        columns = st.columns(2)
        for j in range(len(small_df)):
            with columns[j]:
                with st.container(border=True):
                    row=small_df.iloc[j]
                    spot_type= row["type"]
                    icons = get_spot_type_icon(spot_type)
                    st.subheader(f"{icons} {row["name"]}")
                    col1, col2= st.columns(2)
                    with col1:
                        st.markdown(f"##### Type: {row["type"]}")
                        st.markdown(f"##### Distance: {row["distance_km"]}Km")
                    with col2:
                        status_icon = "🟢"
                        if row["is_open"] == "Close":
                            status_icon="🔴"
                        st.markdown(f"##### Status: {status_icon} {row['is_open']}")
                        rating = (row['rating'])
                        st.markdown(f"##### Rating: {"⭐"*int(rating)}({rating})")
                        
                st.caption(f"🕛{row['opening_time']} - {row['closing_time']}")
    # st.dataframe(df)
    
with tab2:
    st.header("📈 Summary Stats")
    c1 , c2 , c3 , c4 = st.columns(4)
    total_spots = len(df2)
    avg_rating = round(df['rating'].mean() ,2)
    open_spots= len(df2[df2['is_open'] == "Open"])
    sort_data = df2.sort_values(by="distance_km")
    min_dis= sort_data["distance_km"].iloc[0]
    
    # '''METRIC'''
    c1.metric("Total Spots " , total_spots)
    c2.metric("Avg Rating" , avg_rating)
    c3.metric("Open Now" , f'{open_spots} / {total_spots}' )
    c4.metric("Nearest Spot" , min_dis)
    
    spot_count = df['type'].value_counts()
    st.subheader("🏆 Top 10 Rated Spots")
    st.bar_chart(spot_count, color="#68C2E35B" )
    
    st.divider()
    
    st.subheader("⭐ Average Rating by Type")
    average_rating = df2.groupby("type")["rating"].mean()
    st.bar_chart(average_rating , color="#68C2E35B")
    
with tab3:
    
    st.header("Top 10 Rated Spot(s) 🌟")
    # data = pd.read_csv("Datasets/dubai_cold_coffee_spots_clean.csv")
    dff2= df2.sort_values(by="rating" , ascending= False).reset_index(drop=True).head(10)
    dff2.index = dff2.index +1
    st.dataframe(dff2[['name' , 'type' , 'rating' , 'opening_time' , 'closing_time' , 'distance_km' , 'is_open']])
    st.divider()
    st.header("Top 10 Nearest Spot 📍")
    # data2 = pd.read_csv("Datasets/dubai_cold_coffee_spots_clean.csv")
    dff2 = df2.sort_values(by="distance_km").reset_index(drop=True).head(10)
    dff2.index=dff2.index +1
    st.dataframe(dff2)