#!/usr/bin/python3
from geopy import distance
import json
import sys


class GeoCalculator:
    def __init__(self):
        super(GeoCalculator, self).__init__()

    def load_data(self, filepath):
        with open(filepath) as f:
            data = json.load(f)
        return data["coordinates"]

    def distances(self, data):
        distances = []
        while len(data) != 0:
            a = (data[0][0], data[0][1])
            del data[0]
            for i in range(len(data)):
                b = (data[i][0], data[i][1])
                gc_distance = distance.distance(a, b).km
                distances.append([str(a) + "⟷" + str(b), gc_distance])
        distances = self.sort_max(distances)
        return distances

    def sort_max(self, distances):
        def takeSecond(elem):
            return elem[1]

        distances.sort(key=takeSecond, reverse=True)
        return distances

    def write_to_file(self, distances):
        print(distances[:10])
        dict = {"distances": distances}
        data = json.dumps(dict, indent=4)
        with open("distances.json", "w") as f:
            f.write(data)

    def run(self, filepath):
        data = self.load_data(filepath)
        distances = self.distances(data)
        self.write_to_file(distances)


if __name__ == "__main__":
    GeoCalculator().run(sys.argv[1])
