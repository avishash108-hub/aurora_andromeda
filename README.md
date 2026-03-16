# Aurora Visibility Intelligence Platform
A web platform that predicts the likelihood of observing and photographing auroras using environmental and space‑weather data.

## Problem Statement
Aurora visibility depends on multiple complex environmental and space‑weather factors such as solar activity, cloud cover, moon illumination, and light pollution. Most existing scientific data sources provide raw measurements that are difficult for observers and photographers to interpret in practical terms. This makes it challenging for users to determine whether auroras can realistically be observed or photographed at a specific location and time.

## Our Solution
The **Aurora Visibility Intelligence Platform** integrates multiple environmental and space‑weather parameters to generate simple, actionable scores for aurora visibility.

The system computes:
- **Aurora Strength Score** – estimates auroral activity based on solar wind and IMF data
- **Sky Visibility Score** – evaluates atmospheric visibility using cloud cover data
- **Darkness Score** – models sky darkness using moon illumination and Bortle scale
- **Aurora Photography Feasibility Score** – predicts whether auroras can be captured using long‑exposure photography

These signals are combined to estimate the real‑world probability of observing and photographing auroras.

## Features
- **Location‑based aurora visibility prediction**
- **Aurora activity estimation using solar wind and IMF data**
- **Cloud cover–based sky visibility analysis**
- **Moon illumination and Bortle scale darkness modeling**
- **Aurora photography feasibility scoring**
- **Interactive web interface with map and location input**
- **Cloud‑deployed backend API**

## System Architecture
User (Web Interface)
↓
Frontend Web Application
↓
Flask API Backend
↓
Aurora Visibility Model
↓
Visibility & Photography Scores
↓
Results displayed to the user




## Tech Stack

### Frontend
- **HTML**
- **CSS**
- **JavaScript**
- **Leaflet Map API**

### Backend
- **Python**
- **Flask**
- **Flask-CORS**
- **Gunicorn**
- **Requests** *(for future space‑weather API integration)*

### Deployment / Infrastructure
- **GitHub**
- **Render Cloud Hosting**

## API Endpoint
Example request: 

Example response:
```json
{
 "aurora_strength": 0.58,
 "visibility": 0.8,
 "darkness": 0.72,
 "photography_score": 33.6
}

##How to Run Locally
Clone the repository:

git clone <your-repository-link>
Navigate to the project folder:

cd aurora-platform
Install dependencies:

pip install -r requirements.txt
Run the application:

python app.py```




##Future Improvements
Integrate real‑time NOAA space‑weather APIs

Automatic weather data fetching

Machine learning–based aurora visibility prediction

Global aurora heatmap visualization

Real‑time aurora alert notifications

##Team
Team Andromeda
Avisha
Bhuvi
Rinki

##Project Vision
The Aurora Visibility Intelligence Platform aims to bridge the gap between complex scientific space‑weather data and real‑world aurora observation, enabling photographers, researchers, and enthusiasts to make informed decisions about when and where auroras can be observed.


