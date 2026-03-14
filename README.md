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
