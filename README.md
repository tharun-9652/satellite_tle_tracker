# Satellite TLE Tracker

A personal Python desktop project that tracks satellites in real time using live TLE data from CelesTrak, Skyfield orbital calculations, and an interactive Tkinter map.

## Installation  (for windows)

1. Clone the repository:

```bash
git clone https://github.com/tharun-9652/satellite-tle-tracker.git
cd satellite-tle-tracker
```

2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate the virtual environment:

```bash
.venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the application:

```bash
python project.py
```

## Short Description

Satellite TLE Tracker is a personal project built to explore how real satellite tracking works behind the scenes. It lets users choose a satellite category, select a satellite, fetch its latest TLE data, calculate its current latitude and longitude, and view its live movement on a world map.

## Why This Project

This project was built to connect Python programming with a real-world space data use case. It focuses on fetching live orbital data, converting that data into meaningful coordinates, and presenting the result in a simple visual interface.

## Features

- Fetches live satellite data from CelesTrak
- Calculates satellite position with Skyfield
- Shows the satellite on an interactive TkinterMapView map
- Updates the marker position automatically
- Supports satellite category, group, and satellite-name selection
- Uses a custom satellite marker image

## Tech Stack

- Python
- Tkinter
- TkinterMapView
- Skyfield
- Requests
- Rich
- Pillow

## Project Structure

```text
satellite-tle-tracker/
|-- assets/
|   |-- groups.py
|   |-- satellite_image_bg.png
|-- fetch_satellite.py
|-- map.py
|-- project.py
|-- requirements.txt
|-- README.md
|-- LICENSE
```

## How It Works

1. The app displays satellite interest categories in the terminal.
2. The user selects a category, group, and satellite.
3. The app fetches TLE data for the selected satellite.
4. Skyfield calculates the current satellite coordinates.
5. TkinterMapView displays the satellite marker on the map.
6. The marker refreshes automatically to show live movement.

## License

This project is licensed under the MIT License.
