import json
from itertools import product
import time

start_time = time.time()

with open("input.json", "r") as f:
    data = json.load(f)

prof_groups = {}
prof_preferences = {}

for prof, details in data.items():
    prof_groups[prof] = details["group"]
    prof_preferences[prof] = []
    for course_category, courses in details["courses"].items():
        prof_preferences[prof].extend(courses.values())

all_possible_assignments = product(*prof_preferences.values())

count = 0
valid_assignments = []

for assignment in all_possible_assignments:
    course_loads = {prof: 0 for prof in prof_groups}

    
    for prof, course in zip(prof_groups, assignment):
        course_loads[prof] += 0.5 

    
    if all(0 <= course_loads[prof] <= prof_groups[prof] for prof in prof_groups):
        count += 1
        valid_assignments.append(dict(zip(prof_groups, assignment)))

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds\n\n")


output_data = {
    "valid_assignments": valid_assignments,
    "number_of_valid_assignments": count,
    "time_taken": end_time - start_time
}

with open("output.json", "w") as json_file:
    json.dump(output_data, json_file, indent=2)
