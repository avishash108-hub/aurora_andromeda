from flask import Flask, request, jsonify
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
  bz = float(request.args.get("bz"))
  solar = float(request.args.get("solarwind_speed"))
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
     "photography score" : photo
  })

if __name__ == "__main__":
   app.run(host = "0.0.0.0", port=10000)
