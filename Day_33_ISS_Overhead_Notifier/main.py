import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 50.644459 # pozice Teplic v latlong.net
MY_LNG = 13.835284
MY_EMAIL = "your email here"
MY_PASSWORD = "your password here"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status() #kdyz nedostaneme response 200 - vypise chybu i s kodem

    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    # zjistíme, jestli je iss blízko naší pozice
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return True
    else:
        return False

def is_night():
    parametres = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parametres)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) #splitem ziskame jen hodinu
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False

while True:
    time.sleep(60)

    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.youremaildomain")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up\n\nThe ISS is above you."
        )