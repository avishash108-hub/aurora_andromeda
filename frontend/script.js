// AURORA REGION POINTS (fallback if NOAA fails)
const auroraPoints = [
{lat:64.1466,lng:-21.9426,size:0.4},
{lat:69.6492,lng:18.9553,size:0.4},
{lat:64.8378,lng:-147.7164,size:0.4},
{lat:67.8558,lng:20.2253,size:0.4},
{lat:60.7212,lng:-135.0568,size:0.4}
];


// CREATE GLOBE
const globe = Globe()
(document.getElementById("globeContainer"))
.globeImageUrl("//unpkg.com/three-globe/example/img/earth-blue-marble.jpg")
.backgroundColor("rgba(0,0,0,0)");


// SIZE
globe.width(500);
globe.height(400);


// ROTATION
globe.controls().autoRotate = true;
globe.controls().autoRotateSpeed = 0.6;


// DEFAULT POINTS
globe
.pointsData(auroraPoints)
.pointAltitude("size")
.pointColor(() => "#00ffcc");


// LOAD REAL AURORA DATA (NOAA)
async function loadAuroraData(){

try{

let response = await fetch(
"https://services.swpc.noaa.gov/json/ovation_aurora_latest.json"
);

let data = await response.json();

let coords = data.coordinates;

let aurora = coords
.filter(p => p[2] > 20) // ignore very low probability
.map(p => ({
lat: p[1],
lng: p[0],
size: p[2] / 100
}));


globe.pointsData(aurora);

console.log("Aurora overlay updated");

}catch(e){

console.log("Aurora data failed, using fallback points");

}

}


// INITIAL LOAD
loadAuroraData();


// AUTO UPDATE EVERY 5 MINUTES
setInterval(loadAuroraData,300000);



// BUTTON FUNCTION
async function checkVisibility(){

console.log("Button clicked!");

let location = document.getElementById("locationInput").value;
console.log("Location:", location);

if(!location){
alert("Please enter a location");
return;
}


// GEOCODING API
let geo = await fetch(
https://api.openweathermap.org/geo/1.0/direct?q=${location}&limit=1&appid=8c5783e89d2dabb10240bb2275934424
);

let geoData = await geo.json();

if(!geoData.length){
alert("Location not found");
return;
}

let lat = geoData[0].lat;
let lon = geoData[0].lon;

console.log("Latitude:",lat,"Longitude:",lon);


// MOVE GLOBE
globe.pointOfView({
lat: lat,
lng: lon,
altitude: 1.5
},2000);


// CALL BACKEND API
let response = await fetch(
https://aurora-andromeda.onrender.com/score?lat=${lat}&lon=${lon}&bortle_scale=7
);

let data = await response.json();

console.log(data);


// UPDATE SCORECARD
document.getElementById("alert").innerText = data.aurora_alert_status;
document.getElementById("probab").innerText = data.aurora_probability;
document.getElementById("strength").innerText = data.aurora_strength;
document.getElementById("visibility").innerText = data.visibility;
document.getElementById("darkness").innerText = data.darkness;
document.getElementById("photo").innerText = data.photography_score;

}


// BUTTON EVENT
document.getElementById("checkBtn").addEventListener("click", checkVisibility);

window.checkVisibility = checkVisibility;
