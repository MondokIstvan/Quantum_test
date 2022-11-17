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
from dimod.reference.samplers import ExactSolver


sampler = ExactSolver()

# Create empty graph
G = nx.Graph()

# Add edges to graph - this also adds the nodes
G.add_edges_from([(1, 3), (1, 6), (1, 8), (1, 13), (1, 18), (1, 20), (1, 21), (2, 8), (2, 10), (2, 13), (2, 18), (2, 19), (2, 22), (2, 25), (3, 2), (3, 6), (3, 9), (3, 13), (3, 14), (3, 17), (3, 20), (3, 22), (3, 23), (3, 24), (4, 8), (4, 10), (4, 15), (4, 18), (4, 19), (4, 22), (4, 23), (5, 3), (5, 6), (5, 9), (5, 10), (5, 11), (5, 20), (6, 2), (6, 4), (6, 11), (6, 12), (6, 15), (6, 25), (7, 1), (7, 3), (7, 5), (7, 6), (7, 10), (7, 21), (7, 22), (7, 23), (8, 9), (8, 14), (8, 20), (8, 21), (8, 24), (8, 25), (9, 1), (9, 2), (9, 6), (9, 7), (9, 14), (9, 21), (9, 22), (9, 24), (9, 25), (10, 14), (10, 17), (10, 22), (10, 25), (11, 1), (11, 8), (11, 12), (11, 18), (11, 25), (12, 5), (12, 8), (12, 9), (12, 10), (12, 15), (12, 17), (12, 18), (12, 23), (12, 25), (13, 4), (13, 9), (13, 10), (13, 12), (13, 15), (13, 16), (13, 17), (13, 19), (13, 21), (13, 22), (14, 7), (14, 13), (14, 18), (14, 19), (14, 23), (15, 2), (15, 3), (15, 9), (15, 10), (15, 18), (15, 25), (16, 2), (16, 3), (16, 5), (16, 10), (16, 17), (16, 18), (16, 19), (16, 22), (17, 1), (17, 2), (17, 7), (17, 18), (17, 19), (18, 5), (18, 7), (18, 10), (18, 13), (18, 22), (18, 23), (19, 5), (19, 10), (19, 22), (19, 25), (20, 6), (20, 15), (20, 22), (20, 25), (21, 3), (21, 5), (21, 11), (21, 14), (21, 18), (21, 23), (22, 6), (22, 15), (22, 23), (23, 1), (23, 2), (23, 10), (23, 13), (23, 16), (23, 17), (23, 19), (23, 20), (24, 1), (24, 2), (24, 11), (24, 14), (24, 15), (24, 18), (24, 21), (25, 5), (25, 14), (25, 16), (25, 18), (25, 24)])

start_time = time.time()

# Find the minimum vertex cover, S
S = dnx.min_vertex_cover(G, sampler=sampler, lagrange=5)
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
original_name = "pipelines_plot_original_25.png"
nx.draw_networkx(G, pos=pos, with_labels=True)
plt.savefig(original_name, bbox_inches='tight')

# Save solution graph
# Note: red nodes are in the set, blue nodes are not
solution_name = "pipelines_plot_solution_25.png"
nx.draw_networkx(k, pos=pos, with_labels=True, node_color='r', font_color='k')
nx.draw_networkx(othersubgraph, pos=pos, with_labels=True, node_color='b', font_color='w')
plt.savefig(solution_name, bbox_inches='tight')

print("Your plots are saved to {} and {}".format(original_name, solution_name))
