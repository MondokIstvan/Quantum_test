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
from dwave.system import LeapHybridBQMSampler
from dwave.system import LeapHybridSampler
from hybrid.reference.kerberos import KerberosSampler

sampler = LeapHybridBQMSampler(solver={'category': 'hybrid'})
#sampler = LeapHybridSampler()
#sampler = KerberosSampler()

# Create empty graph
G = nx.Graph()

# Add edges to graph - this also adds the nodes
G.add_edges_from([(1, 5), (1, 8), (1, 13), (2, 4), (2, 5), (2, 10), (2, 12), (3, 2), (3, 6), (3, 7), (3, 11), (3, 13), (4, 7), (4, 9), (4, 13), (5, 6), (5, 7), (5, 13), (5, 15), (6, 1), (6, 9), (6, 10), (7, 2), (7, 8), (7, 13), (7, 15), (8, 6), (8, 15), (9, 3), (9, 7), (9, 8), (9, 13), (10, 3), (10, 5), (10, 11), (10, 14), (11, 8), (11, 13), (12, 5), (12, 6), (12, 10), (12, 13), (12, 15), (13, 6), (13, 10), (13, 14), (13, 15), (14, 3), (14, 4), (14, 11), (14, 12), (14, 15), (15, 6), (15, 11)])

start_time = time.time()

# Find the minimum vertex cover, S
#S = dnx.min_vertex_cover(G, sampler=sampler, lagrange=5, num_reads=10, label='MVC-15')
#S = dnx.min_vertex_cover(G, sampler=sampler, qpu_reads=10)
S = dnx.min_vertex_cover(G, sampler=sampler)
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
original_name = "pipelines_plot_original_15.png"
nx.draw_networkx(G, pos=pos, with_labels=True)
plt.savefig(original_name, bbox_inches='tight')

# Save solution graph
# Note: red nodes are in the set, blue nodes are not
solution_name = "pipelines_plot_solution_15.png"
nx.draw_networkx(k, pos=pos, with_labels=True, node_color='r', font_color='k')
nx.draw_networkx(othersubgraph, pos=pos, with_labels=True, node_color='b', font_color='w')
plt.savefig(solution_name, bbox_inches='tight')

print("Your plots are saved to {} and {}".format(original_name, solution_name))
