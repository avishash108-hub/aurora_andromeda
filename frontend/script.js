// Initialize map

var map = L.map('map').setView([20,0],2);


// Map tiles

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
attribution:'Map data',
opacity:3
}).addTo(map);


// Get user location

navigator.geolocation.getCurrentPosition(function(position){

var lat = position.coords.latitude;
var lon = position.coords.longitude;

L.marker([lat,lon]).addTo(map)
.bindPopup("Your Location")
.openPopup();

map.setView([lat,lon],5);

});


// Dummy Aurora Data

const data = {

"Aurora strength":3.4,
visibility:25,
Darkness:520,
Photo:0

};


// Show data on page
document.getElementById("aurora").innerText = data["Aurora strength"];
document.getElementById("visibility").innerText = data.visibility;
document.getElementById("darkness").innerText = data.Darkness;
document.getElementById("photo").innerText = data.Photo;


// Button Function

function checkVisibility(){

alert("Visibility data will connect to backend later.");

}
