#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, "r", newline="") as f:
            data = list(csv.DictReader(f))
        with open("data.json", "w") as f:
            json.dump(data, f)
        return True
    except Exception:
        return False
