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
G.add_edges_from([(1, 6), (1, 8), (1, 11), (1, 15), (1, 18), (1, 19), (1, 22), (1, 31), (1, 32), (1, 35), (2, 5), (2, 7), (2, 12), (2, 15), (2, 17), (2, 20), (2, 24), (2, 31), (2, 32), (2, 33), (2, 37), (2, 39), (3, 6), (3, 8), (3, 19), (3, 21), (3, 27), (3, 32), (3, 34), (3, 37), (3, 40), (4, 3), (4, 6), (4, 8), (4, 10), (4, 11), (4, 19), (4, 20), (4, 21), (4, 24), (4, 27), (4, 29), (4, 30), (4, 32), (4, 33), (4, 39), (5, 1), (5, 7), (5, 9), (5, 15), (5, 20), (5, 21), (5, 23), (5, 24), (5, 26), (5, 27), (5, 28), (5, 29), (5, 30), (5, 31), (5, 32), (5, 36), (5, 37), (5, 39), (5, 40), (6, 5), (6, 19), (6, 20), (6, 21), (6, 22), (6, 32), (7, 9), (7, 15), (7, 16), (7, 19), (7, 21), (7, 22), (7, 23), (7, 25), (7, 28), (7, 32), (8, 2), (8, 14), (8, 15), (8, 17), (8, 22), (8, 23), (8, 32), (8, 33), (8, 36), (9, 4), (9, 8), (9, 10), (9, 13), (9, 15), (9, 21), (9, 22), (9, 24), (9, 30), (9, 33), (9, 34), (9, 35), (9, 38), (10, 2), (10, 5), (10, 6), (10, 11), (10, 13), (10, 15), (10, 19), (10, 20), (10, 21), (10, 26), (10, 28), (10, 29), (10, 33), (10, 34), (10, 36), (11, 3), (11, 5), (11, 7), (11, 9), (11, 15), (11, 16), (11, 17), (11, 20), (11, 24), (11, 35), (12, 3), (12, 5), (12, 15), (12, 17), (12, 19), (12, 21), (12, 23), (12, 24), (12, 26), (12, 33), (12, 38), (13, 2), (13, 5), (13, 6), (13, 7), (13, 11), (13, 16), (13, 20), (13, 24), (13, 25), (13, 26), (13, 28), (13, 30), (13, 31), (13, 32), (13, 34), (13, 36), (13, 38), (14, 1), (14, 4), (14, 10), (14, 11), (14, 15), (14, 16), (14, 17), (14, 25), (14, 26), (14, 27), (14, 28), (14, 34), (15, 3), (15, 6), (15, 13), (15, 16), (15, 19), (15, 20), (15, 22), (15, 24), (15, 29), (15, 34), (15, 35), (15, 38), (16, 2), (16, 4), (16, 12), (16, 18), (16, 22), (16, 25), (16, 26), (16, 28), (16, 32), (16, 33), (16, 34), (16, 36), (16, 38), (16, 39), (17, 5), (17, 7), (17, 13), (17, 16), (17, 18), (17, 22), (17, 23), (17, 24), (17, 25), (17, 28), (17, 30), (17, 38), (17, 39), (18, 7), (18, 14), (18, 22), (18, 25), (18, 26), (18, 29), (18, 30), (18, 32), (18, 34), (18, 38), (18, 40), (19, 20), (19, 21), (19, 22), (19, 23), (19, 30), (19, 36), (19, 38), (20, 1), (20, 3), (20, 8), (20, 12), (20, 21), (20, 23), (20, 26), (20, 28), (20, 29), (20, 34), (20, 35), (20, 36), (20, 37), (20, 40), (21, 13), (21, 16), (21, 22), (21, 23), (21, 25), (21, 27), (21, 31), (21, 37), (21, 39), (21, 40), (22, 2), (22, 5), (22, 14), (22, 24), (22, 25), (22, 26), (22, 28), (22, 34), (22, 35), (23, 1), (23, 2), (23, 4), (23, 6), (23, 14), (23, 22), (23, 24), (23, 28), (23, 31), (23, 34), (23, 39), (24, 6), (24, 8), (24, 19), (24, 30), (24, 31), (24, 34), (24, 35), (24, 38), (25, 1), (25, 2), (25, 4), (25, 11), (25, 12), (25, 27), (25, 28), (25, 31), (25, 32), (25, 39), (25, 40), (26, 3), (26, 4), (26, 7), (26, 11), (26, 15), (26, 21), (26, 23), (26, 25), (26, 27), (26, 30), (26, 31), (26, 33), (26, 35), (26, 37), (26, 39), (27, 7), (27, 13), (27, 23), (27, 34), (27, 37), (27, 39), (28, 3), (28, 15), (28, 31), (28, 32), (28, 33), (28, 36), (29, 1), (29, 6), (29, 9), (29, 13), (29, 19), (29, 28), (29, 32), (29, 33), (29, 34), (29, 36), (29, 37), (29, 38), (30, 7), (30, 12), (30, 25), (30, 34), (30, 36), (30, 38), (30, 40), (31, 3), (31, 4), (31, 8), (31, 12), (31, 15), (31, 18), (31, 22), (31, 29), (31, 30), (31, 32), (31, 34), (31, 35), (31, 36), (32, 9), (32, 11), (32, 14), (32, 19), (32, 20), (32, 21), (32, 23), (32, 30), (32, 34), (32, 36), (32, 38), (33, 6), (33, 11), (33, 15), (33, 20), (33, 21), (33, 24), (33, 30), (33, 31), (33, 38), (34, 6), (34, 12), (34, 19), (34, 35), (35, 6), (35, 7), (35, 10), (35, 23), (35, 25), (35, 27), (36, 4), (36, 11), (36, 14), (36, 23), (36, 24), (36, 26), (36, 34), (36, 38), (36, 39), (37, 6), (37, 8), (37, 11), (37, 15), (37, 17), (37, 22), (37, 24), (37, 25), (37, 30), (37, 31), (37, 38), (38, 1), (38, 3), (38, 4), (38, 5), (38, 7), (38, 8), (38, 10), (38, 14), (38, 20), (38, 27), (38, 39), (38, 40), (39, 1), (39, 6), (39, 7), (39, 11), (39, 12), (39, 15), (39, 22), (39, 30), (39, 33), (40, 8), (40, 10), (40, 13), (40, 16), (40, 19), (40, 22), (40, 23), (40, 27), (40, 31), (40, 32), (40, 37), (40, 39)])

start_time = time.time()

# Find the minimum vertex cover, S
S = dnx.min_vertex_cover(G, sampler=sampler, lagrange=5, num_reads=10, label='MVC-40')
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
original_name = "pipelines_plot_original_40.png"
nx.draw_networkx(G, pos=pos, with_labels=True)
plt.savefig(original_name, bbox_inches='tight')

# Save solution graph
# Note: red nodes are in the set, blue nodes are not
solution_name = "pipelines_plot_solution_40.png"
nx.draw_networkx(k, pos=pos, with_labels=True, node_color='r', font_color='k')
nx.draw_networkx(othersubgraph, pos=pos, with_labels=True, node_color='b', font_color='w')
plt.savefig(solution_name, bbox_inches='tight')

print("Your plots are saved to {} and {}".format(original_name, solution_name))
