"""
DISCO 2023-24
Advik, Druva, Kushagra

hungarian.py
"""
import networkx as nx
import itertools
from alive_progress import alive_bar
import time
import json

import input_graph
from sorter import sort


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
            input["prof_data"].items(), start=len(input["prof_data"]) - 1
        )
        if data[1] in (1, 1.5)
    ],
    bipartite=0,
)

G.add_nodes_from(
    [
        (i, prof)
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
courses = len(G.nodes()) - profs

"""if profs != courses:
    raise Exception("Professors and courses are not equal")"""

labels = {}
for node in G.nodes():
    if node[1] in labels:
        labels[node[1]].append(node)
    else:
        labels[node[1]] = [node]


for prof, data in input["prof_data"].items():
    for courses in data[2:]:
        for i, course in enumerate(courses):
            prof_nodes = labels[prof]
            course_nodes = labels[course]
            G.add_edges_from(itertools.product(prof_nodes, course_nodes), weight=4 - i)

# print(G.edges())


"""def all_maximal_matchings(T):
    maximal_matchings = []
    partial_matchings = [{(u, v)} for (u, v) in T.edges()]

    i = 0
    while partial_matchings:
        i += 1
        print(i)
        # get current partial matching
        m = partial_matchings.pop()
        nodes_m = set(itertools.chain(*m))

        extended = False
        for u, v in T.edges():
            if u not in nodes_m and v not in nodes_m:
                extended = True
                # copy m, extend it and add it to the list of partial matchings
                m_extended = set(m)
                m_extended.add((u, v))
                partial_matchings.append(m_extended)

        if not extended and m not in maximal_matchings:
            maximal_matchings.append(m)

    return maximal_matchings"""


solution = {}

def graph_to_dict(graph):
    result_dict = {}

    for node in graph.nodes():
        successors = list(graph.successors(node))
        result_dict[node] = successors

    return result_dict

import time
import py_bipartite_matching as pbm

start = time.time()
cout = 0

print("starting for all solutions")
matches = []

for matching in pbm.enum_maximum_matchings(G):
    cout += 1
    if(cout % 10000 == 0):
        print(str(cout) + ": done!")
    matches.append(matching)
    if(cout == 600000):
        break

print("completed")
print(str(cout) + " possible solutions")
print("time for all solutions: " + str(time.time() - start))
print("completed")


valid_matches = list()
hash_list = set()
for match in matches:
    vm = {}
    for key, value in match.items():
        prof = key[1]
        course = value[1]
        if prof in vm:
            vm[prof].add(course)
        else:
            vm[prof] = set()
            vm[prof].add(course)
    for key, value in vm.items():
        vm[key] = sorted(value)
    import json
    from hashlib import sha256

    ha = sha256(json.dumps(vm).encode())
    if ha.digest() in hash_list:
        continue
    hash_list.add(ha.digest())
    valid_matches.append(vm)
# print(hash_list)
print("number of valid matches:" + str(len(valid_matches)))
# print(*valid_matches, sep="\n")

best_matches = sort(valid_matches, input["prof_data"])
json_data = json.dumps(best_matches, indent=2)
with open("all_outputs.json", "w") as file:
    file.write(json_data)
