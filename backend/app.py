from flask import Flask, request, jsonify
from flask import Flask, request, jsonify
from flask import Flask, request, jsonify
app = Flask(_name_)
def aurora_strength(bz, solarwind_speed):
  bz_factor = abs(bz)/10
  if bz_factor >1:
    bz_factor  = 1
  
  solar_factor = (solarwind_speed-300)/400
  #for 0 to 1 scale normalize
  if solar_factor > 1:
    solar_factor  = 1

strength = bz_factor*0.6 + solar_factor*0.4
return strength


def cloud_cov(cloud_cover):
  visibility = 1-cloud_cover
  return visibility

def darkness(moon_light, bortle_scale):
  moon_dark = 1 - moon_light
  lightpoll_factor = 1 - (bortle_scale/9)
  darkness_factor = moon_dark + lightpoll_factor
  return darkness

def photo_factor(strength, visibility, darkness):
photo_score = stregth*visibility*darkness
percentage  = photo_score*100
return percentage

@app.route("/score") #put url here

def score():
  bz = float(request.args.get("bz"))
  solar = float(request.args.get("solarwind_speed"))
  cloud = float(request.args.get("cloud_cover"))
  moon = float(request.args.get("moon_light"))
  bortle = float(request.args.get("bortle_scale"))

  strength = aurora_strength(bz, solarwind_speed)
  visibility = cloud_cov(cloud_cover)
  dark = darkness (moon_light, bortle_scale)
  photo = photo_factor(strength, visibility, darkness)

  return jsonify({
     "aurora strength" : strength,
     "visibility" : visibility,
     "darkness" : dark,
     "photography score" : photo
  })

if _name_ == "_main_":
   app.run(host = "0.0.0.0", port=10000)
def aurora_strength(bz, solarwind_speed):
  bz_factor = abs(bz)/10
  if bz_factor >1:
    bz_factor  = 1
  
  solar_factor = (solarwind_speed-300)/400
  #for 0 to 1 scale normalize
  if solar_factor > 1:
    solar_factor  = 1

strength = bz_factor*0.6 + solar_factor*0.4
return strength


def cloud_cov(cloud_cover):
  visibility = 1-cloud_cover
  return visibility

def darkness(moon_light, bortle_scale):
  moon_dark = 1 - moon_light
  lightpoll_factor = 1 - (bortle_scale/9)
  darkness_factor = moon_dark + lightpoll_factor
  return darkness

def photo_factor(strength, visibility, darkness):
photo_score = stregth*visibility*darkness
percentage  = photo_score*100
return percentage

@app.route("/score") #put url here

def score():
  bz = float(request.args.get("bz"))
  solar = float(request.args.get("solarwind_speed"))
  cloud = float(request.args.get("cloud_cover"))
  moon = float(request.args.get("moon_light"))
  bortle = float(request.args.get("bortle_scale"))

  strength = aurora_strength(bz, solarwind_speed)
  visibility = cloud_cov(cloud_cover)
  dark = darkness (moon_light, bortle_scale)
  photo = photo_factor(strength, visibility, darkness)

  return jsonify({
     "aurora strength" : strength,
     "visibility" : visibility,
     "darkness" : dark,
     "photography score" : photo
  })

if _name_ == "_main_":
   app.run(host = "0.0.0.0", port=10000)
def aurora_strength(bz, solarwind_speed):
  bz_factor = abs(bz)/10
  if bz_factor >1:
    bz_factor  = 1
  
  solar_factor = (solarwind_speed-300)/400
  #for 0 to 1 scale normalize
  if solar_factor > 1:
    solar_factor  = 1

strength = bz_factor*0.6 + solar_factor*0.4
return strength


def cloud_cov(cloud_cover):
  visibility = 1-cloud_cover
  return visibility

def darkness(moon_light, bortle_scale):
  moon_dark = 1 - moon_light
  lightpoll_factor = 1 - (bortle_scale/9)
  darkness_factor = moon_dark + lightpoll_factor
  return darkness

def photo_factor(strength, visibility, darkness):
photo_score = stregth*visibility*darkness
percentage  = photo_score*100
return percentage

@app.route("/score") #put url here

def score():
  bz = float(request.args.get("bz"))
  solar = float(request.args.get("solarwind_speed"))
  cloud = float(request.args.get("cloud_cover"))
  moon = float(request.args.get("moon_light"))
  bortle = float(request.args.get("bortle_scale"))

  strength = aurora_strength(bz, solarwind_speed)
  visibility = cloud_cov(cloud_cover)
  dark = darkness (moon_light, bortle_scale)
  photo = photo_factor(strength, visibility, darkness)

  return jsonify({
     "aurora strength" : strength,
     "visibility" : visibility,
     "darkness" : dark,
     "photography score" : photo
  })

if _name_ == "_main_":
   app.run(host = "0.0.0.0", port=10000)

