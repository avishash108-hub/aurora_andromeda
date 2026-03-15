from flask import Flask, request, jsonify
import requests
def fetch_solar_data():
  plasma = requests.get("https://services.swpc.noaa.gov/products/solar-wind/plasma-1-day.json").json()
  mag = requests.get("https://services.swpc.noaa.gov/products/solar-wind/mag-1-day.json").json()
  latest_plasma = plasma[len(plasma)-1]
  latest_mag = mag[len(mag)-1]
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
  
  
app = Flask(__name__)
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
  darkness_factor = moon_dark + lightpoll_factor
  return darkness_factor

def photo_factor(strength, visibility, dark):
  photo_score = strength*visibility*dark
  percentage  = photo_score*100
  return percentage

@app.route("/")
def home():
  return "Aurora API running"
@app.route("/score")
def score():
  bz, solar = fetch_solar_data()
  if bz < -7 or solar > 500:
    alert = "High Aurora activity"
  else:
    alert = "Normal Aurora conditions"
  cloud = float(request.args.get("cloud_cover"))
  moon = float(request.args.get("moon_light"))
  bortle = float(request.args.get("bortle_scale"))

  strength = aurora_strength(bz, solar)
  visibility = cloud_cov(cloud)
  dark = darkness (moon, bortle)
  photo = photo_factor(strength, visibility, dark)

  return jsonify({
     "aurora_strength" : strength,
     "visibility" : visibility,
     "darkness" : dark,
     "photography_score" : photo
  })

if __name__ == "__main__":
   app.run(host = "0.0.0.0", port=10000)
