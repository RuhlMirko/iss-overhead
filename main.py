import requests
from datetime import datetime

MY_LAT = -34.61315  # Your latitude
MY_LONG = -58.37723  # Your longitude


def near():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    lat_dif = iss_latitude - MY_LAT
    lng_dif = iss_longitude - MY_LONG
    # Prints Overhead if your position is within +5 or -5 degrees of the ISS position.
    if 5 >= lat_dif >= -5:
        if 5 >= lng_dif >= -5:
            print("Overhead")
        else:
            print("Maybe next time")
    else:
        print("Maybe next time")


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

near()
