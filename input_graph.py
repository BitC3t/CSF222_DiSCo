
import json

f = open("input.json")

data = json.load(f)

new_data = {}
F_C = set()
F_E = set()
H_C = set()
H_E = set()
for name, prof_data in data.items():
    id = prof_data["id"]
    group = prof_data["group"]
    courses = prof_data["courses"]

    FD_CDC = []
    for sem, course in courses["FD_CDC"].items():
        FD_CDC.append(course)
        F_C.add(course)

    FD_Electives = []
    for sem, course in courses["FD_Electives"].items():
        FD_Electives.append(course)
        F_E.add(course)

    HD_CDC = []
    for sem, course in courses["HD_CDC"].items():
        HD_CDC.append(course)
        H_C.add(course)

    HD_Electives = []
    for sem, course in courses["HD_Electives"].items():
        HD_Electives.append(course)
        H_E.add(course)

    new_data[name] = [id, group, FD_CDC, FD_Electives, HD_CDC, HD_Electives]


if __name__ == "__main__":
    dump = json.dumps(new_data, indent=4)
    print(dump)


def get_data():
    return {
        "prof_data": new_data,
        "F_C": list(F_C),
        "F_E": list(F_E),
        "H_C": list(H_C),
        "H_E": list(H_E),
    }
