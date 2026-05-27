from assets.groups import GROUP_CATEGORIES
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import math, json, requests

        #FORMATTED USING BLACK#

console = Console()
def fetch_url(url):
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response, ""
    except requests.Timeout:
        return None, "Request timed out, Try again."
    except requests.RequestException as error:
        return None, f"Request failed: {error}"
    
def fetch_index(prompt, max_value):
    while True:
        try: 
            value = console.input(prompt)
        except KeyboardInterrupt():
            console.print("Program interrupted using keyboard.")
            continue
        if not value.isdigit():
            console.print("[red]Enter a Valid Serial Number[red/]")
            continue
        value = int(value)
        if 0< value <= max_value:
            return value
        console.print("[red]Enter a Valid Serial Number[red/]")
        continue

def intrest():
    table = Table(
        title="Satellite Interests Category",
        show_header=True,
        title_style="",
    )
    table.add_column("S.No.", justify="left", style="")
    table.add_column("Intrest Categories", justify="left", style="")

    for index, key in enumerate(GROUP_CATEGORIES.keys(), start=1):
        table.add_row(f"{index}", f"{key}")
    console.print(table)

    while True:
        position = console.input("Enter a valid S.No. of the Intrests category: ")
        if not position.isdigit():
            console.print("Enter a valid Serial Number")
            continue
        position = int(position)
        if 0 < position <= len(GROUP_CATEGORIES.keys()):
            return list(GROUP_CATEGORIES.keys())[position - 1]
        continue


def group(category):
    table = Table(show_header=True, title="Satellite Groups Category", title_style="")
    table.add_column("S.No", justify="left", style="")
    table.add_column("Group Category", justify="left", style="")

    list_category = [dict_ for dict_ in GROUP_CATEGORIES[f"{category}"]]
    ids = [dict["id"] for dict in list_category]
    for index, group in enumerate(list_category, start=1):
        table.add_row(f"{index}", group["name"])
    console.print(table)

    index = fetch_index(f"Enter a valid S.No. of the {category} category: ", len(ids))
    return ids[index-1]

def satellite_name(group):
    url = (
        f"https://celestrak.org/NORAD/elements/gp.php?GROUP={group}&FORMAT=json-pretty"
    )
    response, error = fetch_url(url)
    if response is None:
        return None, error

    with open("assets/satellites.json", "w", newline="") as f:
        f.write(response.text)
    with open("assets/satellites.json", "r") as f:
        data = json.load(f)
    satellite_names = [sat["OBJECT_NAME"] for sat in data]

    table = Table(title="Satellite Names")
    columns = int(4)
    rows = math.ceil(len(satellite_names) / columns)

    for _ in range(columns):
        table.add_column("S.No")
        table.add_column("Satellite")
    for row in range(rows):
        entire_first_row = []
        for col in range(columns):
            index = row + (col * rows)
            if index < len(satellite_names):
                entire_first_row.append(f"{index+1}")
                entire_first_row.append(f"{satellite_names[index]}")
            else:
                entire_first_row.append("")
                entire_first_row.append("")
        table.add_row(*entire_first_row)
    console.print(table)
    
    index = fetch_index("Enter a valid S.No. of the Satellite you want to track: ", len(satellite_names))
    return data[index - 1]["OBJECT_NAME"], ""

def satellite_tle(name):
    url = f"https://celestrak.org/NORAD/elements/gp.php?NAME={name}&FORMAT=tle"
    r, error = fetch_url(url)
    if r is None:
        return None, error

    with open("assets/tle_data.csv", "w+", newline="") as f:
        f.write(f"{r.text}")
        f.seek(0)
        lines = [line.strip() for line in f]
    return lines, ""
