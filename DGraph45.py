# Copyright 2019 D-Wave Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Import networkx for graph tools
import networkx as nx

# Import dwave_networkx for d-wave graph tools/functions
import dwave_networkx as dnx

# Import matplotlib.pyplot to draw graphs on screen
# note: since there are people without an interactive matplotlib backend
# and since the code does not need said backend, we will explicitly call for
# a non-interactive backend, Agg. See the following for details:
# https://matplotlib.org/faq/usage_faq.html#what-is-a-backend
import matplotlib
matplotlib.use("agg")    # must select backend before importing pyplot
import matplotlib.pyplot as plt
# Import time to determinate the time the algorithm use to solve the problem
import time

# Set the solver we're going to use
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

sampler = EmbeddingComposite(DWaveSampler())

# Create empty graph
G = nx.Graph()

# Add edges to graph - this also adds the nodes
G.add_edges_from([(1, 4), (1, 5), (1, 7), (1, 8), (1, 10), (1, 14), (1, 16), (1, 17), (1, 22), (1, 23), (1, 24), (1, 32), (1, 36), (1, 40), (2, 6), (2, 10), (2, 12), (2, 19), (2, 26), (2, 30), (2, 32), (2, 35), (2, 37), (2, 41), (2, 43), (2, 44), (3, 5), (3, 10), (3, 18), (3, 28), (3, 30), (3, 31), (3, 34), (3, 37), (3, 39), (3, 40), (3, 44), (4, 8), (4, 19), (4, 20), (4, 22), (4, 27), (4, 31), (4, 34), (4, 36), (4, 39), (4, 43), (4, 44), (5, 6), (5, 15), (5, 16), (5, 21), (5, 25), (5, 29), (5, 33), (5, 36), (5, 37), (5, 38), (5, 42), (6, 1), (6, 3), (6, 4), (6, 13), (6, 15), (6, 23), (6, 24), (6, 28), (6, 29), (6, 30), (6, 35), (6, 36), (6, 40), (7, 2), (7, 5), (7, 9), (7, 14), (7, 18), (7, 19), (7, 22), (7, 23), (7, 25), (7, 27), (7, 33), (7, 37), (7, 41), (7, 42), (8, 5), (8, 6), (8, 7), (8, 9), (8, 12), (8, 19), (8, 22), (8, 23), (8, 27), (8, 28), (8, 32), (8, 33), (8, 38), (8, 39), (8, 41), (8, 43), (9, 2), (9, 4), (9, 6), (9, 14), (9, 17), (9, 20), (9, 21), (9, 24), (9, 30), (9, 31), (9, 32), (9, 40), (9, 41), (9, 44), (9, 45), (10, 6), (10, 7), (10, 12), (10, 18), (10, 19), (10, 21), (10, 22), (10, 23), (10, 24), (10, 27), (10, 30), (10, 32), (10, 40), (10, 43), (11, 4), (11, 6), (11, 15), (11, 28), (11, 29), (11, 33), (11, 44), (12, 3), (12, 5), (12, 6), (12, 9), (12, 13), (12, 21), (12, 22), (12, 24), (12, 26), (12, 27), (12, 28), (12, 35), (12, 36), (12, 42), (13, 1), (13, 7), (13, 11), (13, 20), (13, 29), (13, 34), (13, 45), (14, 10), (14, 13), (14, 20), (14, 22), (14, 27), (14, 35), (14, 37), (14, 43), (14, 44), (15, 2), (15, 3), (15, 8), (15, 10), (15, 13), (15, 19), (15, 20), (15, 24), (15, 27), (15, 36), (15, 37), (15, 43), (15, 44), (16, 9), (16, 10), (16, 13), (16, 19), (16, 25), (16, 27), (16, 29), (16, 31), (16, 37), (16, 40), (16, 42), (17, 4), (17, 5), (17, 6), (17, 7), (17, 8), (17, 10), (17, 11), (17, 13), (17, 14), (17, 21), (17, 24), (17, 25), (17, 28), (17, 29), (17, 32), (17, 37), (17, 39), (17, 41), (17, 44), (18, 2), (18, 8), (18, 12), (18, 23), (18, 25), (18, 29), (18, 32), (18, 40), (18, 41), (18, 42), (18, 43), (18, 44), (18, 45), (19, 14), (19, 18), (19, 20), (19, 25), (19, 33), (19, 36), (19, 39), (19, 40), (19, 42), (19, 45), (20, 3), (20, 6), (20, 23), (20, 27), (20, 31), (20, 36), (20, 37), (20, 38), (20, 43), (20, 44), (20, 45), (21, 2), (21, 3), (21, 4), (21, 6), (21, 18), (21, 19), (21, 20), (21, 23), (21, 27), (21, 31), (21, 33), (21, 34), (21, 35), (21, 37), (21, 39), (22, 2), (22, 28), (22, 32), (22, 39), (22, 45), (23, 14), (23, 16), (23, 19), (23, 22), (23, 30), (23, 31), (23, 36), (23, 37), (23, 38), (23, 43), (24, 2), (24, 8), (24, 13), (24, 14), (24, 19), (24, 23), (24, 26), (24, 27), (24, 38), (24, 39), (24, 41), (24, 43), (24, 45), (25, 2), (25, 3), (25, 9), (25, 11), (25, 12), (25, 15), (25, 22), (25, 23), (25, 24), (25, 29), (25, 31), (25, 33), (25, 34), (25, 35), (25, 36), (25, 37), (25, 38), (25, 43), (25, 44), (26, 6), (26, 10), (26, 22), (26, 25), (26, 28), (26, 31), (26, 40), (26, 41), (26, 43), (26, 44), (27, 1), (27, 2), (27, 13), (27, 22), (27, 25), (27, 26), (27, 28), (27, 30), (27, 33), (27, 34), (27, 35), (27, 38), (27, 42), (27, 43), (27, 44), (27, 45), (28, 7), (28, 9), (28, 13), (28, 18), (28, 20), (28, 25), (28, 30), (28, 31), (28, 32), (28, 42), (28, 43), (28, 44), (28, 45), (29, 1), (29, 2), (29, 7), (29, 9), (29, 14), (29, 15), (29, 19), (29, 22), (29, 27), (29, 34), (29, 35), (29, 37), (29, 40), (29, 41), (29, 42), (29, 43), (30, 1), (30, 5), (30, 7), (30, 11), (30, 18), (30, 20), (30, 24), (30, 29), (30, 39), (30, 41), (30, 43), (31, 7), (31, 10), (31, 12), (31, 14), (31, 17), (31, 19), (31, 34), (31, 36), (31, 37), (31, 42), (32, 7), (32, 11), (32, 12), (32, 13), (32, 21), (32, 25), (32, 38), (32, 39), (32, 45), (33, 1), (33, 4), (33, 15), (33, 17), (33, 18), (33, 24), (33, 30), (33, 32), (33, 34), (33, 35), (33, 37), (33, 39), (33, 40), (33, 42), (33, 43), (33, 44), (33, 45), (34, 5), (34, 7), (34, 8), (34, 12), (34, 15), (34, 17), (34, 18), (34, 28), (34, 37), (34, 42), (35, 3), (35, 7), (35, 10), (35, 11), (35, 13), (35, 16), (35, 19), (35, 23), (35, 30), (35, 31), (35, 34), (35, 38), (35, 39), (35, 40), (35, 42), (35, 43), (36, 2), (36, 7), (36, 9), (36, 10), (36, 26), (36, 34), (36, 39), (36, 42), (36, 45), (37, 1), (37, 4), (37, 10), (37, 11), (37, 13), (37, 22), (37, 27), (37, 30), (37, 32), (37, 35), (37, 42), (38, 3), (38, 10), (38, 12), (38, 17), (38, 30), (38, 33), (38, 34), (38, 36), (38, 42), (38, 43), (39, 1), (39, 2), (39, 5), (39, 7), (39, 12), (39, 13), (39, 26), (39, 27), (39, 28), (39, 38), (39, 40), (39, 44), (39, 45), (40, 4), (40, 5), (40, 11), (40, 13), (40, 15), (40, 20), (40, 21), (40, 22), (40, 28), (40, 32), (40, 36), (40, 37), (40, 38), (40, 41), (40, 42), (40, 43), (41, 1), (41, 4), (41, 13), (41, 14), (41, 21), (41, 23), (41, 28), (41, 31), (41, 37), (41, 42), (41, 45), (42, 3), (42, 4), (42, 9), (42, 11), (43, 3), (43, 5), (43, 9), (43, 11), (43, 12), (43, 16), (43, 17), (43, 22), (43, 32), (43, 37), (43, 39), (43, 42), (44, 1), (44, 16), (44, 19), (44, 21), (44, 22), (44, 24), (44, 32), (44, 36), (44, 40), (44, 45), (45, 1), (45, 11), (45, 12), (45, 16), (45, 25), (45, 35), (45, 40), (45, 42)])

start_time = time.time()

# Find the minimum vertex cover, S
S = dnx.min_vertex_cover(G, sampler=sampler, lagrange=5, num_reads=10, label='MVC-45')
print("--- %s seconds ---" % (time.time() - start_time))

# Print the solution for the user
print('Minimum vertex cover found is', len(S))
print(S)

# Visualize the results
k = G.subgraph(S)
notS = list(set(G.nodes()) - set(S))
othersubgraph = G.subgraph(notS)
pos = nx.spring_layout(G)
plt.figure()

# Save original problem graph
original_name = "pipelines_plot_original_45.png"
nx.draw_networkx(G, pos=pos, with_labels=True)
plt.savefig(original_name, bbox_inches='tight')

# Save solution graph
# Note: red nodes are in the set, blue nodes are not
solution_name = "pipelines_plot_solution_45.png"
nx.draw_networkx(k, pos=pos, with_labels=True, node_color='r', font_color='k')
nx.draw_networkx(othersubgraph, pos=pos, with_labels=True, node_color='b', font_color='w')
plt.savefig(solution_name, bbox_inches='tight')

print("Your plots are saved to {} and {}".format(original_name, solution_name))
