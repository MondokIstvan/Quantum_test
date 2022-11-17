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
G.add_edges_from([(1, 2), (1, 4), (1, 7), (1, 12), (1, 17), (1, 18), (1, 21), (1, 23), (1, 26), (1, 30), (2, 6), (2, 11), (2, 13), (2, 18), (2, 20), (2, 21), (2, 24), (2, 25), (2, 27), (3, 5), (3, 6), (3, 7), (3, 9), (3, 10), (3, 14), (3, 19), (3, 21), (3, 24), (4, 5), (4, 7), (4, 17), (4, 18), (4, 20), (4, 27), (4, 28), (5, 1), (5, 8), (5, 10), (5, 15), (5, 20), (5, 21), (5, 26), (5, 27), (5, 28), (5, 30), (6, 1), (6, 5), (6, 11), (6, 12), (6, 13), (6, 17), (6, 22), (6, 30), (7, 8), (7, 10), (7, 15), (7, 16), (7, 17), (7, 18), (7, 21), (7, 22), (7, 26), (7, 27), (7, 28), (7, 29), (8, 1), (8, 2), (8, 4), (8, 11), (8, 13), (8, 15), (8, 19), (8, 20), (8, 24), (8, 25), (8, 27), (8, 28), (9, 2), (9, 4), (9, 5), (9, 7), (9, 8), (9, 13), (9, 14), (9, 16), (9, 20), (9, 21), (9, 22), (9, 24), (9, 26), (10, 1), (10, 4), (10, 6), (10, 8), (10, 9), (10, 19), (10, 20), (10, 22), (10, 27), (10, 29), (11, 1), (11, 18), (11, 25), (11, 26), (12, 2), (12, 4), (12, 7), (12, 8), (12, 9), (12, 11), (12, 19), (12, 24), (12, 25), (12, 26), (12, 27), (12, 29), (13, 1), (13, 3), (13, 4), (13, 17), (13, 18), (13, 19), (13, 24), (13, 25), (14, 5), (14, 6), (14, 15), (14, 16), (14, 22), (14, 23), (14, 26), (14, 27), (15, 2), (15, 18), (15, 21), (15, 23), (15, 24), (15, 28), (16, 1), (16, 10), (16, 13), (16, 19), (16, 23), (16, 24), (16, 27), (17, 11), (17, 12), (17, 15), (17, 18), (17, 20), (17, 24), (17, 25), (17, 30), (18, 3), (18, 8), (18, 14), (18, 20), (18, 24), (18, 25), (18, 28), (18, 30), (19, 1), (19, 20), (19, 22), (19, 27), (19, 28), (19, 29), (19, 30), (20, 6), (20, 16), (20, 26), (20, 28), (20, 29), (21, 17), (21, 18), (21, 20), (21, 22), (21, 25), (21, 28), (21, 30), (22, 3), (22, 11), (22, 15), (22, 17), (22, 28), (22, 29), (23, 4), (23, 6), (23, 7), (23, 10), (23, 11), (23, 21), (23, 24), (23, 27), (23, 28), (23, 29), (24, 1), (24, 5), (24, 6), (24, 10), (24, 11), (24, 20), (24, 25), (24, 28), (25, 5), (25, 14), (25, 16), (25, 28), (26, 2), (26, 3), (26, 4), (26, 13), (26, 15), (26, 22), (26, 24), (26, 27), (26, 30), (27, 1), (27, 3), (27, 9), (27, 22), (27, 25), (27, 30), (28, 1), (28, 11), (28, 26), (29, 1), (29, 6), (29, 8), (29, 14), (29, 15), (29, 25), (29, 27), (29, 30), (30, 3), (30, 4), (30, 13), (30, 14), (30, 15), (30, 24)])

start_time = time.time()

# Find the minimum vertex cover, S
S = dnx.min_vertex_cover(G, sampler=sampler, lagrange=5, num_reads=10, label='MVC-30')
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
original_name = "pipelines_plot_original_30.png"
nx.draw_networkx(G, pos=pos, with_labels=True)
plt.savefig(original_name, bbox_inches='tight')

# Save solution graph
# Note: red nodes are in the set, blue nodes are not
solution_name = "pipelines_plot_solution_30.png"
nx.draw_networkx(k, pos=pos, with_labels=True, node_color='r', font_color='k')
nx.draw_networkx(othersubgraph, pos=pos, with_labels=True, node_color='b', font_color='w')
plt.savefig(solution_name, bbox_inches='tight')

print("Your plots are saved to {} and {}".format(original_name, solution_name))
