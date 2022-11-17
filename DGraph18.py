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
G.add_edges_from([(1, 2), (1, 4), (1, 5), (1, 8), (1, 9), (1, 13), (1, 16), (1, 18), (2, 4), (2, 5), (2, 9), (2, 14), (2, 17), (3, 6), (3, 8), (3, 12), (4, 3), (4, 5), (4, 10), (4, 14), (4, 15), (4, 16), (4, 17), (4, 18), (5, 7), (5, 8), (5, 10), (5, 12), (5, 13), (5, 14), (5, 15), (5, 16), (5, 17), (5, 18), (6, 11), (6, 13), (6, 15), (7, 3), (7, 4), (7, 6), (7, 9), (7, 11), (7, 15), (8, 2), (8, 4), (8, 13), (8, 17), (8, 18), (9, 6), (9, 8), (9, 12), (9, 13), (9, 14), (9, 17), (9, 18), (10, 1), (10, 7), (10, 11), (10, 13), (11, 4), (11, 13), (11, 16), (12, 6), (12, 8), (12, 18), (13, 2), (13, 7), (13, 18), (14, 3), (14, 7), (14, 15), (14, 16), (14, 18), (15, 1), (15, 8), (15, 10), (16, 2), (16, 3), (16, 6), (16, 7), (16, 8), (16, 9), (16, 15), (17, 14), (18, 2), (18, 16), (18, 17)])

start_time = time.time()

# Find the minimum vertex cover, S
S = dnx.min_vertex_cover(G, sampler=sampler, lagrange=5, num_reads=10, label='MVC-18')
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
original_name = "pipelines_plot_original_18.png"
nx.draw_networkx(G, pos=pos, with_labels=True)
plt.savefig(original_name, bbox_inches='tight')

# Save solution graph
# Note: red nodes are in the set, blue nodes are not
solution_name = "pipelines_plot_solution_18.png"
nx.draw_networkx(k, pos=pos, with_labels=True, node_color='r', font_color='k')
nx.draw_networkx(othersubgraph, pos=pos, with_labels=True, node_color='b', font_color='w')
plt.savefig(solution_name, bbox_inches='tight')

print("Your plots are saved to {} and {}".format(original_name, solution_name))
