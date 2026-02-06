import urllib.request
import urllib.parse
import json
import threading

API_URL = "http://universities.hipolabs.com/search?country="

countries = [
    "Poland", "Germany", "France", "United Kingdom", "Spain",
    "Italy", "Netherlands", "Belgium", "Czech Republic", "Austria",
    "Sweden", "Norway", "Denmark", "Finland", "Portugal",
    "Greece", "Romania", "Hungary", "Ireland", "Switzerland"
]

results = {}
lock = threading.Lock()


def fetch_for_country(country):
    url = API_URL + urllib.parse.quote(country)
    try:
        with urllib.request.urlopen(url, timeout=10) as f:
            data = json.loads(f.read().decode())
        names = []
        for item in data:
            if isinstance(item, dict) and "name" in item:
                names.append(item["name"])
        with lock:
            results[country] = names
    except Exception as e:
        with lock:
            results[country] = ["Blad: " + str(e)]


if __name__ == "__main__":
    threads = []
    for country in countries:
        t = threading.Thread(target=fetch_for_country, args=(country,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    for country in countries:
        print(country, ":", results[country][:3], "...")
    print("\nPelny wynik (slownik):")
    print(json.dumps(results, indent=2, ensure_ascii=False)[:500], "...")
