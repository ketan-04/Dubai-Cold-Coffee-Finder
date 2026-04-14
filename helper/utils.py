from geopy.distance import geodesic

from datetime import datetime

def calculate_distance(user_location,row):
    
    lat = row["lat"]
    lng = row['lng']
    spot_loc = (lat,lng)
    dis= geodesic(user_location, spot_loc).km
    return round(dis,2)



# def is_open_spot(row):
#     current_time = datetime.now().strftime("%H:%M")
#     open_time = row["opening_time"]
#     closing_time = row["closing_time"]
#     if current_time <= open_time <=closing_time:
#         return ("open")
        
#     else :
#         return("closed")



def is_open_spot(row):
       open = row["opening_time"]
       close = row["closing_time"]
       a = datetime.now().strftime("%H:%M")
       if open <= a <= close:
              return "Open"
       else:
              return "Close"
       
       
def rating_star(rating):
    intg = int(rating)
    if rating<0 or rating>5:
        print("Please Enter Rating Between 1 and 5")
    else:
        print("⭐" * intg , "("+ str(rating) + ")")
        
        
def get_spot_type_icon(spot_type):
      spot_icon = ["🏠","🛒","🚚","☕"]
    #   print("ENter Your chocie:")
      if spot_type == "cafe":
          return ( spot_icon [0])
      elif spot_type == "cart":
          return( spot_icon[1])
      elif spot_type == "truck":
          return( spot_icon[2]  )
      else: 
          return( spot_icon[2])  
      
