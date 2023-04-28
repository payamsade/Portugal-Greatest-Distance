#!/usr/bin/python3
import json
import sys


def run(filepath):
    with open(filepath, "r") as f:
        data = f.read()
    d = json.loads(data)
    for i in range(len(d["coordinates"])):
        temp = d["coordinates"][i][0]
        d["coordinates"][i][0] = d["coordinates"][i][1]
        d["coordinates"][i][1] = temp
    with open(filepath, "w") as f:
        json_object = json.dumps(d, indent=4)
        f.write(json_object)


if __name__ == "__main__":
    run(sys.argv[1])
