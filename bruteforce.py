import json 
from itertools import product

with open('input.json','r') as f:
    data = json.load(f)


prof_groups = {}
prof_preferences = {}


for prof, details in data.items():
    prof_groups[prof] = details['group']
    prof_preferences[prof] = []
    for course_category, courses in details['courses'].items():
        prof_preferences[prof].extend(courses.values())


all_possible_assignments = product(*prof_preferences.values())
print(all_possible_assignments)

for assignment in all_possible_assignments:
    # Initialize the course loads
    course_loads = {prof: 0 for prof in prof_groups}

    # Assign courses to professors
    for prof, course in zip(prof_groups, assignment):
        course_loads[prof] += 0.5  # Each course is split into 0.5

    # Check if the assignment is valid
    if all(0 <= course_loads[prof] <= prof_groups[prof] for prof in prof_groups):
        print(f"Valid assignment: {dict(zip(prof_groups, assignment))}")




