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
G.add_edges_from([(1, 4), (1, 5), (1, 9), (1, 10), (1, 11), (1, 13), (1, 15), (1, 18), (1, 21), (1, 25), (1, 31), (1, 34), (2, 5), (2, 10), (2, 24), (2, 25), (2, 27), (2, 28), (2, 32), (2, 33), (2, 34), (3, 2), (3, 8), (3, 14), (3, 16), (3, 18), (3, 19), (3, 21), (3, 22), (3, 24), (3, 28), (3, 34), (4, 3), (4, 5), (4, 6), (4, 7), (4, 11), (4, 17), (4, 22), (4, 26), (4, 30), (4, 31), (4, 35), (5, 7), (5, 10), (5, 16), (5, 22), (5, 32), (5, 33), (5, 35), (6, 9), (6, 16), (6, 17), (6, 19), (6, 21), (6, 26), (6, 27), (6, 29), (6, 35), (7, 2), (7, 10), (7, 12), (7, 15), (7, 16), (7, 18), (7, 19), (7, 20), (7, 25), (7, 26), (7, 28), (7, 29), (7, 31), (7, 32), (7, 35), (8, 7), (8, 9), (8, 11), (8, 16), (8, 23), (8, 24), (8, 25), (8, 30), (8, 32), (8, 33), (8, 35), (9, 3), (9, 4), (9, 10), (9, 11), (9, 14), (9, 19), (9, 20), (9, 21), (9, 26), (9, 29), (9, 30), (10, 4), (10, 6), (10, 15), (10, 16), (10, 18), (10, 19), (10, 20), (10, 26), (10, 27), (10, 30), (10, 33), (11, 7), (11, 10), (11, 12), (11, 13), (11, 16), (11, 19), (11, 23), (11, 31), (12, 1), (12, 4), (12, 9), (12, 10), (12, 13), (12, 15), (12, 20), (12, 25), (12, 27), (12, 29), (12, 30), (12, 31), (13, 6), (13, 9), (13, 16), (13, 17), (13, 18), (13, 19), (13, 20), (13, 24), (13, 30), (13, 33), (13, 34), (13, 35), (14, 10), (14, 11), (14, 12), (14, 15), (14, 16), (14, 18), (14, 20), (14, 21), (14, 23), (14, 27), (14, 28), (14, 29), (14, 30), (14, 35), (15, 2), (15, 5), (15, 11), (15, 16), (15, 18), (15, 20), (15, 21), (15, 22), (15, 30), (15, 32), (15, 33), (15, 35), (16, 1), (16, 17), (16, 20), (16, 24), (16, 27), (16, 30), (17, 24), (17, 25), (17, 27), (18, 5), (18, 9), (18, 11), (18, 20), (18, 24), (18, 27), (18, 35), (19, 4), (19, 14), (19, 16), (19, 18), (19, 22), (19, 30), (19, 32), (20, 1), (20, 2), (20, 8), (20, 11), (20, 22), (20, 23), (20, 25), (20, 29), (20, 33), (21, 4), (21, 5), (21, 10), (21, 12), (21, 17), (21, 22), (21, 23), (21, 25), (21, 27), (21, 28), (21, 31), (22, 8), (22, 9), (22, 12), (22, 14), (22, 17), (22, 25), (22, 29), (22, 30), (22, 33), (22, 34), (22, 35), (23, 1), (23, 2), (23, 3), (23, 16), (23, 17), (23, 18), (23, 24), (23, 25), (23, 26), (23, 28), (23, 29), (23, 31), (23, 34), (24, 5), (24, 7), (24, 9), (24, 14), (24, 19), (24, 21), (24, 22), (24, 31), (24, 32), (25, 3), (25, 10), (25, 11), (25, 13), (25, 18), (25, 24), (25, 26), (25, 28), (25, 32), (25, 35), (26, 1), (26, 2), (26, 5), (26, 17), (26, 20), (26, 22), (26, 24), (26, 28), (26, 31), (26, 33), (26, 34), (27, 25), (27, 28), (27, 30), (27, 32), (27, 33), (27, 35), (28, 4), (28, 8), (28, 9), (28, 12), (28, 13), (28, 20), (28, 22), (28, 30), (28, 32), (29, 1), (29, 8), (29, 24), (29, 25), (29, 30), (29, 32), (30, 2), (30, 3), (30, 6), (30, 18), (30, 24), (30, 25), (30, 32), (30, 34), (31, 2), (31, 5), (31, 9), (31, 13), (31, 16), (31, 28), (31, 29), (31, 33), (32, 3), (32, 4), (32, 6), (32, 11), (32, 14), (32, 17), (32, 22), (32, 31), (32, 34), (32, 35), (33, 11), (33, 18), (33, 19), (33, 24), (33, 28), (33, 29), (33, 34), (34, 9), (34, 10), (34, 12), (34, 17), (34, 18), (34, 19), (34, 21), (34, 28), (34, 35), (35, 1), (35, 11), (35, 12), (35, 17), (35, 20), (35, 21), (35, 23), (35, 24), (35, 26), (35, 33)])

start_time = time.time()

# Find the minimum vertex cover, S
S = dnx.min_vertex_cover(G, sampler=sampler, lagrange=5, num_reads=10, label='MVC-35')
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
original_name = "pipelines_plot_original_35.png"
nx.draw_networkx(G, pos=pos, with_labels=True)
plt.savefig(original_name, bbox_inches='tight')

# Save solution graph
# Note: red nodes are in the set, blue nodes are not
solution_name = "pipelines_plot_solution_35.png"
nx.draw_networkx(k, pos=pos, with_labels=True, node_color='r', font_color='k')
nx.draw_networkx(othersubgraph, pos=pos, with_labels=True, node_color='b', font_color='w')
plt.savefig(solution_name, bbox_inches='tight')

print("Your plots are saved to {} and {}".format(original_name, solution_name))
