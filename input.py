"""
DISCO 2023-24
Advik, Druva, Kushagra

input.py
"""
import json

f = open('input.json')

data = json.load(f)

new_data = {}
for name, prof_data in data.items():
    id = prof_data["id"]
    group = prof_data["group"]
    courses = prof_data["courses"]

    FD_CDC = []
    for sem, course in courses["FD_CDC"].items():
        FD_CDC.append(course)

    FD_Electives = []
    for sem, course in courses["FD_Electives"].items():
        FD_Electives.append(course)

    HD_CDC = []
    for sem, course in courses["HD_CDC"].items():
        HD_CDC.append(course)

    HD_Electives = []
    for sem, course in courses["HD_Electives"].items():
        HD_Electives.append(course)

    new_data[name] = [id, group, FD_CDC, FD_Electives, HD_CDC, HD_Electives]


print(new_data)