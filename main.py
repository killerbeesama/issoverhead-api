import requests
import datetime as dt
import time

my_lat = "<your lattitude>"
my_lng = "<your longitude>"


def iss_location():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    if my_lat - 5 <= iss_latitude <= my_lat + 5 and my_lng - 5 <= iss_longitude <= my_lng + 5:
        return True


def is_night():
    parameter = {
        "lat": my_lat,
        "lng": my_lng,
        "formatted": 0,

    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
    data = response.json()
    sunrise = int(data['results']['sunrise'].split(":")[0].split("T")[1])
    sunset = int(data['results']['sunset'].split(":")[0].split("T")[1])

    time_now = dt.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if iss_location() and is_night():
        #send email from here
        pass
