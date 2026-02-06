import urllib.request
import xml.etree.ElementTree as ET
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

URL = "https://danepubliczne.imgw.pl/api/data/meteo/format/xml"


def fetch_xml(url):
    with urllib.request.urlopen(url, timeout=15) as f:
        return f.read()


def parse_wind_from_xml(xml_bytes):
    root = ET.fromstring(xml_bytes)
    stations = {}
    for elem in root:
        name = None
        speed = None
        for child in elem:
            tag = child.tag
            if "}" in tag:
                tag = tag.split("}")[-1]
            text = (child.text or "").strip()
            if tag.lower() in ("stacja", "station", "nazwa", "name"):
                name = text
            if tag.lower() in ("predkosc_wiatru", "predkosc_wiatru_kmh", "wind_speed"):
                try:
                    speed = float(text.replace(",", "."))
                except ValueError:
                    pass
        if name and speed is not None:
            if name not in stations:
                stations[name] = []
            stations[name].append(speed)
    result = {}
    for name, speed_list in stations.items():
        result[name] = sum(speed_list) / len(speed_list)
    return result


SAMPLE_XML = b"""<?xml version="1.0"?>
<meteo>
<item><stacja>Warszawa</stacja><predkosc_wiatru>12</predkosc_wiatru></item>
<item><stacja>Krakow</stacja><predkosc_wiatru>8</predkosc_wiatru></item>
<item><stacja>Gdansk</stacja><predkosc_wiatru>15</predkosc_wiatru></item>
<item><stacja>Poznan</stacja><predkosc_wiatru>10</predkosc_wiatru></item>
<item><stacja>Wroclaw</stacja><predkosc_wiatru>9</predkosc_wiatru></item>
</meteo>"""

if __name__ == "__main__":
    print("Pobieram dane z IMGW...")
    data = {}
    try:
        xml_bytes = fetch_xml(URL)
        data = parse_wind_from_xml(xml_bytes)
    except Exception as e:
        print("Blad pobierania:", e)
    if not data:
        print("Uzyte dane przykladowe.")
        data = parse_wind_from_xml(SAMPLE_XML)
    if not data:
        print("Nie udalo sie odczytac danych.")
        exit(1)
    station_names = list(data.keys())
    speeds = [data[s] for s in station_names]
    plt.figure(figsize=(10, 5))
    plt.bar(station_names, speeds, color="lightblue", edgecolor="black")
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Srednia predkosc wiatru (km/h)")
    plt.title("Predkosc wiatru - stacje IMGW")
    plt.tight_layout()
    plt.savefig("wiatr_stacje.png")
    print("Wykres zapisany w pliku wiatr_stacje.png")
