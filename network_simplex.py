"""
DISCO 2023-24
Advik, Druva, Kushagra

hungarian.py
"""
import networkx as nx
import itertools

import input_graph


def plotGraph(graph, ax, title):
    pos = [(ii[1], ii[0]) for ii in graph.nodes()]
    pos_dict = dict(zip(graph.nodes(), pos))
    nx.draw(graph, pos=pos_dict, ax=ax, with_labels=True)
    ax.set_title(title)
    return


input = input_graph.get_data()


def graph_to_json(G):
    json_data = {}
    json_data["professors"] = set()
    json_data["courses"] = set()
    json_data["prof_data"] = {}
    json_data["course_data"] = {}
    for prof, course in G.edges():
        json_data["professors"].add(prof)
        json_data["courses"].add(course)
        if prof in json_data["prof_data"]:
            json_data["prof_data"][prof].append(course)
        else:
            json_data["prof_data"][prof] = [course]
        if course in json_data["course_data"]:
            json_data["course_data"][course].append(prof)
        else:
            json_data["course_data"][course] = [prof]
    json_data["professors"] = list(json_data["professors"])
    json_data["courses"] = list(json_data["courses"])
    for prof, data in input["prof_data"].items():
        json_data["prof_data"][prof].insert(0, data[1])
        json_data["prof_data"][prof].insert(0, data[0])
    return json_data


G = nx.DiGraph()

# Adding all professors
G.add_nodes_from(
    [((i, prof), {"demand": 1}) for i, prof in enumerate(input["prof_data"].keys())],
    bipartite=0,
)

G.add_nodes_from(
    [
        ((i, prof), {"demand": 1})
        for i, (prof, data) in enumerate(
            input["prof_data"].items(), start=len(input["prof_data"]) - 1
        )
        if data[1] in (1, 1.5)
    ],
    bipartite=0,
)

G.add_nodes_from(
    [
        ((i, prof), {"demand": 1})
        for i, (prof, data) in enumerate(
            input["prof_data"].items(), start=len(input["prof_data"]) * 2
        )
        if data[1] == 1.5
    ],
    bipartite=0,
)
profs = len(G.nodes())
# Multiply by two because of two slots
G.add_nodes_from(
    [
        ((i, x), {"demand": -1})
        for i, x in enumerate(input["F_C"] + input["F_E"] + input["H_C"] + input["H_E"])
    ],
    bipartite=1,
)
G.add_nodes_from(
    [
        ((i, x), {"demand": -1})
        for i, x in enumerate(
            input["F_C"] + input["F_E"] + input["H_C"] + input["H_E"],
            start=len(input["F_C"] + input["F_E"] + input["H_C"] + input["H_E"]),
        )
    ],
    bipartite=1,
)
courses = len(G.nodes()) - profs


if profs != courses:
    raise Exception("Professors and courses are not equal")

labels = {}
for node in G.nodes():
    print(node)
    if node[1] in labels:
        labels[node[1]].append(node)
    else:
        labels[node[1]] = [node]


for prof, data in input["prof_data"].items():
    for courses in data[2:]:
        for i, course in enumerate(courses):
            prof_nodes = labels[prof]
            course_nodes = labels[course]
            G.add_edges_from(
                itertools.product(prof_nodes, course_nodes), weight=i, capacity=1, w=i
            )

# print(G.edges())


from matplotlib import pyplot as plt

import time

start = time.time()
# matches = all_maximal_matchings(G)
# matches = nx.max_weight_matching(G, maxcardinality=True)
flowCost, matches = nx.network_simplex(G, weight="w")
print(time.time() - start)
print(matches)
matches = [matches]
g_match2 = nx.Graph()
for match2 in matches:
    for kk, vv in match2:
        g_match2.add_edge(kk, vv)
    match2 = nx.max_weight_matching(G, maxcardinality=True)
    g_match = nx.DiGraph()
    print("edges")
    for edge in match2:
        prof = edge[1][1]
        course = edge[0][1]
        print(prof, course)
        g_match.add_edge(prof, course)
    print(*g_match.edges(), sep="\n")
    nx.draw(g_match, with_labels=True)
    # nx.draw(G, with_labels=True)
    plt.show()
    import json

    with open("output.json", "w") as f:
        json.dump(graph_to_json(g_match), f, indent=4)
    print("done")


# nx.draw(G, with_labels=True)
