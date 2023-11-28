"""
DiSCo 2023 - 24
Advik, Druva, Kushagra

[THIS FILE IS NOT PART OF THE PROJECT, IT IS JUST A SAMPLE BRUTEFORCE ALGORITHM FOR THIS ASSIGNMENT]
Bruteforces through the test case to find solutions
"""

import json
from itertools import product

# Read input data from a JSON file
with open("input.json", "r") as f:
    data = json.load(f)

# Initialize dictionaries to store professor groups and preferences
prof_groups = {}
prof_preferences = {}

# Extract information from the input JSON data
for prof, details in data.items():
    prof_groups[prof] = details["group"]
    prof_preferences[prof] = []
    for course_category, courses in details["courses"].items():
        prof_preferences[prof].extend(courses.values())

# Generate all possible assignments using Cartesian product
all_possible_assignments = product(*prof_preferences.values())
print(all_possible_assignments)

# Initialize a counter for valid assignments
count = 0

# Iterate through all possible assignments
for assignment in all_possible_assignments:
    # Initialize the course loads for each professor
    course_loads = {prof: 0 for prof in prof_groups}

    # Distribute the courses in the assignment to the respective professors
    for prof, course in zip(prof_groups, assignment):
        course_loads[prof] += 0.5  # Each course is split into 0.5 to represent a half-course load

    # Check if the assignment satisfies the constraints (course load within the allowed range)
    if all(0 <= course_loads[prof] <= prof_groups[prof] for prof in prof_groups):
        count += 1
        print(f"Valid assignment: {dict(zip(prof_groups, assignment))}")

# Print the total number of valid assignments
print(count)
