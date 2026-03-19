import csv
import json


def getCsvValues(path: str) -> list[list[str]]:
    with open(path, newline="") as file:
        reader = csv.reader(file)
        res: list[list[str]] = []
        for row in reader:
            res.append(row)
        return res


def toGeoJson(places: list[list[str]]) -> dict:
    featureCollection = dict()
    featureCollection["type"] = "FeatureCollection"
    features = []
    featureCollection["features"] = features
    for place in places[1:]:
        if len(place) < 4:
            continue
        feature = dict()
        feature["type"] = "Feature"
        geometry = dict()
        geometry["type"] = "Point"
        geometry["coordinates"] = [float(place[1]), float(place[0])]
        feature["geometry"] = geometry
        properties = dict()
        properties["tipo"] = place[2]
        properties["nome"] = place[3]
        feature["properties"] = properties
        features.append(feature)

    return featureCollection


def saveToJsonFile(val: dict, filename: str):
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(val, file, indent=4, ensure_ascii=False)


def main():
    print("Hello from atividade-04!")
    csv = getCsvValues("../atividade-03/places-sax.csv")
    geoJson = toGeoJson(csv)

    saveToJsonFile(geoJson, "places.json")


if __name__ == "__main__":
    main()
