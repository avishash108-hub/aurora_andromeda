from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
import base64
import threading
import time

solar_cache = {
  "bz": 0,
  "solarwind": 400,
  "last_update": None
}
def fetch_cloud_cover(lat, lon):
  weatherapi_key = os.getenv("WEATHER_API")
  url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weatherapi_key}"
  data = requests.get(url).json()
  cloud_cover = data.get("clouds",{}).get("all",0)/100
  return cloud_cover

def fetch_moon_light(lat, lon):
  try:
    app_id = os.getenv("APP_ID")
    app_secret = os.getenv("SECRET_KEY")

    credentials = f"{app_id}:{app_secret}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    url = f"https://api.astronomyapi.com/api/v2/bodies/positions/moon?latitude={lat}&longitude={lon}&elevation=0"

    headers = {
      "Authorization": f"Basic {encoded_credentials}"
    }

    response = requests.get(url, headers=headers).json()

    moon_light = response["data"]["table"]["rows"][0]["cells"][0]["extraInfo"]["illumination"]["fraction"]

    return float(moon_light)

  except Exception as e:
    print("Moon API failed:", e)
    return 0.5
  
def fetch_solar_data():

  plasma = requests.get("https://services.swpc.noaa.gov/products/solar-wind/plasma-1-day.json", timeout=5).json()
  mag = requests.get("https://services.swpc.noaa.gov/products/solar-wind/mag-1-day.json", timeout=5).json()

  latest_plasma = plasma[-1]
  latest_mag = mag[-1]

  solar_value = latest_plasma[2]
  bz_value = latest_mag[3]

  if solar_value != "" and solar_value != None:
    solarwind_speed = float(solar_value)
  else:
    solarwind_speed = 400

  if bz_value != "" and bz_value != None:
    bz = float(bz_value)
  else:
    bz = 0

  return bz, solarwind_speed

def poll_solar_data():
  global solar_cache

  while True:
    try:
      bz, solar = fetch_solar_data()

      solar_cache["bz"] = bz
      solar_cache["solarwind"] = solar
      solar_cache["last_update"] = time.time()

      print("Solar data updated")

    except Exception as e:
      print("Solar fetch failed:", e)

    time.sleep(300)

def fetch_aurora_probab(lat, lon):

    aurora = requests.get(
        "https://services.swpc.noaa.gov/json/ovation_aurora_latest.json",
        timeout=5
    ).json()

    coordinates = aurora["coordinates"]

    closest_prob = 0
    min_dist = 999

    for p in coordinates:

        lon_point = p[0]
        lat_point = p[1]
        prob = p[2]

        dist = abs(lat_point - lat) + abs(lon_point - lon)

        if dist < min_dist:
            min_dist = dist
            closest_prob = prob

    return closest_prob / 100
  
app = Flask(__name__)
CORS(app)
def aurora_strength(bz, solarwind_speed):
  bz_factor = abs(bz)/10
  if bz_factor > 1:
    bz_factor = 1

  solar_factor = (solarwind_speed-300)/400
  if solar_factor > 1:
    solar_factor = 1

  strength = bz_factor*0.6 + solar_factor*0.4
  return strength


def cloud_cov(cloud_cover):
  visibility = 1-cloud_cover
  return visibility

def darkness(moon_light, bortle_scale):
  moon_dark = 1 - moon_light
  lightpoll_factor = 1 - (bortle_scale/9)
  darkness_factor = (moon_dark + lightpoll_factor)/2
  return darkness_factor

def photo_factor(strength, visibility, dark, prob):
  photo_score = (strength + visibility + dark + prob) / 4
  percentage  = photo_score*100
  return percentage

@app.route("/")
def home():
  return "Aurora API running"
@app.route("/score")
def score():
  bz = solar_cache["bz"]
  solar = solar_cache["solarwind"]
  lat = float(request.args.get("lat"))
  lon = float(request.args.get("lon"))
  cloud = fetch_cloud_cover(lat, lon)
  moon = fetch_moon_light(lat, lon)
  bortle = float(request.args.get("bortle_scale"))
  prob = fetch_aurora_probab(lat, lon)
  
  if bz < -7 or solar > 500:
    alert = "High Aurora activity"
  else:
    alert = "Normal Aurora conditions"
    
  strength = aurora_strength(bz, solar)
  visibility = cloud_cov(cloud)
  dark = darkness (moon, bortle)
  photo = photo_factor(strength, visibility, dark, prob)
  alert_message = None

  if photo > 60:
    alert_message = "High Aurora visibility expected!"

  if bz < -8:
    alert_message = "Substorm warning: Aurora may intensify soon!"

  return jsonify({
    "aurora_alert_status" : alert,
    "aurora_probability": f"{round(prob * 100, 2)}%",
    "aurora_strength": f"{round(strength * 100, 2)}%",
    "visibility": f"{round(visibility * 100, 2)}%",
    "darkness": f"{round(dark * 100, 2)}%",
    "photography_score": photo,
    "alert_message" : alert_message
  })


if __name__ == "__main__":
    threading.Thread(target=poll_solar_data, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
