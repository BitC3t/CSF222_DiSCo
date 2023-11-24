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
G = nx.Graph()

# Adding all professors
G.add_nodes_from(
    [(i, prof) for i, prof in enumerate(input["prof_data"].keys())],
    bipartite=0,
)

G.add_nodes_from(
    [
        (i, prof)
        for i, (prof, data) in enumerate(
            input["prof_data"].items(), start=len(input["prof_data"])
        )
        if data[1] == 1
    ],
    bipartite=0,
)

G.add_nodes_from(
    [
        (i, prof)
        for i, (prof, data) in enumerate(
            input["prof_data"].items(), start=len(input["prof_data"])
        )
        if data[1] == 1.5
    ],
    bipartite=0,
)
# Multiply by two because of two slots
G.add_nodes_from(
    [
        (i, x)
        for i, x in enumerate(input["F_C"] + input["F_E"] + input["H_C"] + input["H_E"])
    ],
    bipartite=1,
)
G.add_nodes_from(
    [
        (i, x)
        for i, x in enumerate(
            input["F_C"] + input["F_E"] + input["H_C"] + input["H_E"],
            start=len(input["F_C"] + input["F_E"] + input["H_C"] + input["H_E"]),
        )
    ],
    bipartite=1,
)

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
            G.add_edges_from(itertools.product(prof_nodes, course_nodes))

# print(G.edges())

match2 = nx.bipartite.maximum_matching(G)
g_match2 = nx.Graph()
for kk, vv in match2.items():
    g_match2.add_edge(kk, vv)
match2 = nx.max_weight_matching(G, maxcardinality=True)
g_match = nx.Graph()
print(match2)
for edge in match2:
    prof = edge[0][1]
    course = edge[1][1]
    g_match.add_edge(prof, course)

from matplotlib import pyplot as plt


# nx.draw(G, with_labels=True)
nx.draw(g_match, with_labels=True)
# nx.draw(G, with_labels=True)
plt.show()
