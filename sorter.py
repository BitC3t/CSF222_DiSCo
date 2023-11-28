"""
DiSCo 2023 - 24
Advik, Druva, Kushagra

[HELPER SCRIPT]
Sorts the solutions based on the preferences of the professor.
"""

def get_weight_sum(weights: dict, cur: dict) -> int:
    """
    Calculate the weighted sum of courses in the current assignment based on given weights.

    Parameters:
    - weights: Dictionary representing weights for each professor and course combination.
    - cur: Dictionary representing the current assignment of courses to professors.

    Returns:
    - int: Weighted sum of courses in the current assignment.
    """
    weight = 0
    for prof, courses in cur.items():
        for course in courses:
            weight += weights[prof][course]
    return weight


def sort(weights, input):
    """
    Sort a list of assignments based on their weighted sums.

    Parameters:
    - weights: Dictionary representing weights for each professor and course combination.
    - input: Dictionary containing professor information and course categories.

    Returns:
    - list: Sorted list of assignments based on the weighted sums.
    """
    w = {}

    # Extract weights from the input data
    for prof, data in input.items():
        w[prof] = {}
        for course_list in data[2:]:
            for i, course in enumerate(course_list):
                w[prof][course] = 4 - int(i)

    # Sort the list of assignments based on weighted sums
    sorted_weights = sorted(
        weights,
        key=lambda x: get_weight_sum(w, x),
    )
    return sorted_weights
