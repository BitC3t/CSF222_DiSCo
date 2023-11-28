"""
DiSCo 2023 - 24
Advik, Druva, Kushagra

[HELPER SCRIPT]
Reads input.json to give us information about the preferences, professors & courses.
"""

import json

# Open and read data from the input JSON file
f = open("input.json")
data = json.load(f)

# Initialize dictionaries and sets to store processed data
new_data = {}
F_C = set()
F_E = set()
H_C = set()
H_E = set()

# Iterate through the original data and extract relevant information
for name, prof_data in data.items():
    id = prof_data["id"]
    group = prof_data["group"]
    courses = prof_data["courses"]

    # Extract courses for FD_CDC category
    FD_CDC = []
    for sem, course in courses["FD_CDC"].items():
        FD_CDC.append(course)
        F_C.add(course)

    # Extract courses for FD_Electives category
    FD_Electives = []
    for sem, course in courses["FD_Electives"].items():
        FD_Electives.append(course)
        F_E.add(course)

    # Extract courses for HD_CDC category
    HD_CDC = []
    for sem, course in courses["HD_CDC"].items():
        HD_CDC.append(course)
        H_C.add(course)

    # Extract courses for HD_Electives category
    HD_Electives = []
    for sem, course in courses["HD_Electives"].items():
        HD_Electives.append(course)
        H_E.add(course)

    # Organize extracted data into a new dictionary
    new_data[name] = [id, group, FD_CDC, FD_Electives, HD_CDC, HD_Electives]

# If the script is executed directly (not imported), generate and print the JSON dump
if __name__ == "__main__":
    dump = json.dumps(new_data, indent=4)
    print(dump)


# Function to return processed data in a specific format
def get_data():
    """
    Return processed data in a specific format.

    Returns:
    - Dictionary containing processed data, including professor information and course categories.
    """
    return {
        "prof_data": new_data,
        "F_C": list(F_C),
        "F_E": list(F_E),
        "H_C": list(H_C),
        "H_E": list(H_E),
    }
