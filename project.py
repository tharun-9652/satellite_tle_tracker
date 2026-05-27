from rich.console import Console
import tkinter as tk
from tkintermapview import TkinterMapView
from skyfield.api import EarthSatellite, load, wgs84
from PIL import Image, ImageTk
from fetch_satellite import intrest, group, satellite_name, satellite_tle

        #FORMATTED USING BLACK#
console = Console()
def main():
    intrest_category = intrest()  # Fetch Intrests Category of the User
    group_category = group(intrest_category)  # Fetch Group category under the  selected intrest
    sat_name = check_error(satellite_name(group_category))  # Fetch Name of the satellite user wants to see the location of
    tle_data = check_error(satellite_tle(sat_name))
    root, widget, marker = tk_window(tle_data)
    update(root, widget, marker, tle_data)
    root.mainloop()
def check_error(data):
    value, error = data
    if error != "":
        console.log(error)
        return
    return value
def satellite_position(tle_data):  # source to learn "https://rhodesmill.org/skyfield/earth-satellites.html"
    ts = load.timescale()  # creates a Timescale object, idk to calculate relative times
    t = ts.now()  # Current time
    satellite = EarthSatellite(
        tle_data[1], tle_data[2], tle_data[0], ts
    )  # Creating a satallite object
    location = satellite.at(t)  # Satellite position in space
    lat, lon = wgs84.latlon_of(
        location
    )  # Convert space position into earths latitiude and longitude
    return [lat.degrees, lon.degrees]  # returns latitude and longitude


def tk_window(tle_data):
    # create tkinter window
    root = tk.Tk()
    root.geometry("1000x700")
    root.title("Satellite Live Location")

    widget = TkinterMapView(root, width=1000, height=700, corner_radius=10)
    widget.pack(fill="both", expand=True, anchor="center")

    lat, lon = satellite_position(tle_data)
    widget.set_position(lat, lon, text="Live Location")
    widget.set_zoom(5)
    satellite_icon = ImageTk.PhotoImage(
        Image.open("assets/satellite_image_bg.png").resize((100, 100))
    )
    marker = widget.set_marker(lat, lon, icon=satellite_icon)
    return root, widget, marker


def update(root, widget, marker, tle_data):

    lat, lon = satellite_position(tle_data)
    marker.set_position(lat, lon)
    widget.set_position(lat, lon)

    root.after(1000, update, root, widget, marker, tle_data)


if __name__ == "__main__":
    main()
