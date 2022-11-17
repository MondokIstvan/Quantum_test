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
G.add_edges_from([(1, 3), (1, 8), (1, 11), (1, 19), (2, 11), (2, 12), (3, 5), (3, 6), (3, 10), (3, 16), (3, 18), (4, 1), (4, 13), (4, 17), (5, 6), (5, 9), (5, 11), (5, 16), (5, 17), (5, 18), (5, 19), (6, 1), (6, 2), (6, 8), (6, 11), (6, 12), (6, 19), (6, 20), (7, 1), (7, 6), (7, 12), (7, 13), (7, 14), (7, 15), (7, 17), (7, 18), (8, 5), (8, 7), (8, 10), (8, 12), (8, 15), (8, 19), (8, 20), (9, 2), (9, 3), (9, 8), (9, 11), (9, 19), (10, 9), (10, 13), (10, 14), (10, 18), (10, 19), (11, 4), (11, 14), (11, 15), (11, 17), (11, 18), (11, 20), (12, 3), (12, 4), (12, 11), (12, 15), (12, 19), (13, 2), (13, 3), (13, 5), (13, 6), (13, 8), (13, 9), (13, 11), (13, 12), (13, 15), (13, 16), (13, 20), (14, 1), (14, 6), (14, 12), (14, 13), (14, 19), (14, 20), (15, 2), (15, 3), (15, 4), (15, 5), (15, 14), (15, 18), (15, 19), (16, 1), (16, 7), (16, 8), (16, 9), (17, 2), (17, 3), (17, 8), (17, 14), (17, 15), (17, 16), (17, 19), (17, 20), (18, 8), (18, 9), (18, 12), (18, 14), (18, 17), (18, 19), (18, 20), (19, 2), (19, 4), (19, 16), (19, 20), (20, 2), (20, 5), (20, 10), (20, 12), (20, 16)])

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
original_name = "pipelines_plot_original_20.png"
nx.draw_networkx(G, pos=pos, with_labels=True)
plt.savefig(original_name, bbox_inches='tight')

# Save solution graph
# Note: red nodes are in the set, blue nodes are not
solution_name = "pipelines_plot_solution_20.png"
nx.draw_networkx(k, pos=pos, with_labels=True, node_color='r', font_color='k')
nx.draw_networkx(othersubgraph, pos=pos, with_labels=True, node_color='b', font_color='w')
plt.savefig(solution_name, bbox_inches='tight')

print("Your plots are saved to {} and {}".format(original_name, solution_name))
