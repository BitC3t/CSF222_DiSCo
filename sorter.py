def get_weight_sum(weights: dict, cur: dict):
    """
    Sorts the weights by the current weights
    """
    weight = 0
    for prof, courses in cur.items():
        for course in courses:
            weight += weights[prof][course]
    return weight


def sort(weights, input):
    """
    Sorts the weights by the current weights
    """
    # Sort the weights by the current weights
    w = {}

    for prof, data in input.items():
        w[prof] = {}
        for map in data[2:]:
            for i, course in enumerate(map):
                w[prof][course] = 4 - int(i)
    sorted_weights = sorted(
        weights,
        key=lambda x: get_weight_sum(w, x),
    )
    return sorted_weights
