import csv
import time
import xml.sax
from dataclasses import dataclass
from xml.dom.minidom import Element, parse


@dataclass
class Place:
    lat: str
    lgt: str
    tipo: str
    nome: str


def getElementNameAndType(node: Element) -> Place | None:
    name = ""
    type = ""
    for tag in node.getElementsByTagName("tag"):
        if name != "" and type != "":
            break
        if tag.getAttribute("k") == "name":
            name = tag.getAttribute("v")
        elif tag.getAttribute("k") == "amenity":
            type = tag.getAttribute("v")
    if name == "" or type == "":
        return None
    lat = node.getAttribute("lat")
    lon = node.getAttribute("lon")
    return Place(lat, lon, type, name)


def saveToCsvFile(places: list[Place], filename: str):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["lat", "lgt", "tipo", "nome"])
        for place in places:
            writer.writerow([place.lat, place.lgt, place.tipo, place.nome])
        file.write("\n")


class Listener(xml.sax.ContentHandler):
    def __init__(self):
        self.currentData = ""
        self.lat: str = ""
        self.lgt: str = ""
        self.name: str = ""
        self.type: str = ""
        self.insideNode = False
        self.list: list[Place] = []
        self.start_time = time.time()

    def startElement(self, name, attrs):
        self.currentData = ""

        if name == "node":
            lat = attrs.get("lat")
            lgt = attrs.get("lon")
            if lat is not None and lgt is not None:
                self.lat = lat
                self.lgt = lgt
            self.insideNode = True
        elif name == "tag" and self.insideNode:
            if attrs.get("k") == "name":
                name = attrs.get("v")
                if name is not None:
                    self.name = name
            elif attrs.get("k") == "amenity":
                type = attrs.get("v")
                if type is not None:
                    self.type = type

    def endElement(self, name):
        if name == "node":
            if self.name != "" and self.type != "":
                self.list.append(Place(self.lat, self.lgt, self.type, self.name))
            self.name = ""
            self.type = ""

    def characters(self, content):
        self.currentData += content

    def startDocument(self):
        print("\n\n\nReading file with SAX Parser...")

    def endDocument(self):
        saveToCsvFile(self.list, "places-sax.csv")
        end_time = time.time()
        print(f"File 'places-sax.csv' created with {len(self.list)} entries.")
        print(f"Time taken to save to CSV: {end_time - self.start_time:.6f} seconds")


if __name__ == "__main__":
    start_time = time.time()
    listOfPlaces: list[Place] = []

    print("Reading file with DOM parser...")
    OpenStreetMapsRegion = parse("mq-fm.osm")
    for node in OpenStreetMapsRegion.getElementsByTagName("node"):
        numberOfChildren = node.childNodes.length
        if numberOfChildren > 0:
            place = getElementNameAndType(node)
            if place is not None:
                listOfPlaces.append(place)

    saveToCsvFile(listOfPlaces, "places-dom.csv")
    print(f"File 'places-dom.csv' created with {len(listOfPlaces)} entries.")

    end_time = time.time()
    print(f"Time taken to save to CSV: {end_time - start_time:.6f} seconds")

    # Sax parser
    parser = xml.sax.make_parser()
    Handler = Listener()
    parser.setContentHandler(Handler)
    parser.parse("mq-fm.osm")
