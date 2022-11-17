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
G.add_edges_from([(1, 6), (1, 7), (1, 10), (1, 13), (1, 18), (1, 19), (1, 20), (1, 21), (1, 23), (1, 24), (1, 25), (1, 32), (1, 38), (1, 46), (1, 49), (1, 50), (1, 55), (1, 58), (1, 63), (1, 67), (2, 5), (2, 6), (2, 10), (2, 14), (2, 15), (2, 19), (2, 25), (2, 32), (2, 33), (2, 34), (2, 41), (2, 45), (2, 46), (2, 48), (2, 51), (2, 52), (2, 54), (2, 56), (2, 57), (2, 62), (2, 69), (3, 6), (3, 8), (3, 19), (3, 25), (3, 26), (3, 27), (3, 29), (3, 34), (3, 38), (3, 41), (3, 46), (3, 47), (3, 51), (3, 59), (3, 60), (3, 61), (3, 62), (3, 63), (3, 66), (3, 70), (4, 2), (4, 3), (4, 10), (4, 11), (4, 13), (4, 14), (4, 20), (4, 21), (4, 23), (4, 32), (4, 35), (4, 36), (4, 37), (4, 43), (4, 44), (4, 45), (4, 47), (4, 48), (4, 52), (4, 53), (4, 55), (4, 64), (4, 65), (4, 69), (4, 70), (5, 1), (5, 6), (5, 8), (5, 9), (5, 10), (5, 14), (5, 15), (5, 17), (5, 18), (5, 20), (5, 21), (5, 24), (5, 28), (5, 33), (5, 34), (5, 36), (5, 41), (5, 45), (5, 49), (5, 53), (5, 55), (5, 60), (5, 66), (5, 70), (6, 7), (6, 8), (6, 12), (6, 13), (6, 14), (6, 19), (6, 22), (6, 23), (6, 24), (6, 25), (6, 27), (6, 29), (6, 30), (6, 32), (6, 34), (6, 36), (6, 37), (6, 41), (6, 46), (6, 49), (6, 52), (6, 53), (6, 56), (6, 61), (6, 63), (6, 67), (6, 68), (7, 2), (7, 8), (7, 10), (7, 13), (7, 18), (7, 19), (7, 25), (7, 26), (7, 27), (7, 29), (7, 30), (7, 37), (7, 39), (7, 42), (7, 49), (7, 52), (7, 56), (7, 57), (7, 63), (7, 65), (7, 66), (7, 67), (7, 70), (8, 1), (8, 2), (8, 9), (8, 18), (8, 21), (8, 22), (8, 27), (8, 28), (8, 31), (8, 32), (8, 33), (8, 34), (8, 35), (8, 36), (8, 37), (8, 38), (8, 41), (8, 44), (8, 47), (8, 50), (8, 54), (8, 56), (8, 58), (8, 60), (8, 61), (8, 63), (8, 66), (8, 67), (8, 68), (8, 70), (9, 4), (9, 14), (9, 15), (9, 20), (9, 25), (9, 28), (9, 31), (9, 32), (9, 44), (9, 47), (9, 48), (9, 57), (9, 63), (9, 69), (10, 3), (10, 9), (10, 11), (10, 15), (10, 18), (10, 19), (10, 20), (10, 23), (10, 26), (10, 31), (10, 35), (10, 37), (10, 39), (10, 41), (10, 44), (10, 46), (10, 55), (10, 58), (10, 61), (10, 70), (11, 3), (11, 5), (11, 13), (11, 21), (11, 22), (11, 31), (11, 35), (11, 37), (11, 38), (11, 40), (11, 44), (11, 48), (11, 49), (11, 51), (11, 53), (11, 57), (11, 59), (11, 60), (11, 61), (11, 63), (11, 65), (12, 3), (12, 5), (12, 7), (12, 25), (12, 26), (12, 28), (12, 34), (12, 35), (12, 41), (12, 42), (12, 43), (12, 47), (12, 52), (12, 54), (12, 56), (12, 60), (12, 64), (12, 67), (12, 68), (13, 12), (13, 14), (13, 18), (13, 20), (13, 22), (13, 23), (13, 26), (13, 27), (13, 30), (13, 31), (13, 36), (13, 37), (13, 42), (13, 45), (13, 54), (13, 57), (13, 58), (13, 59), (13, 60), (13, 65), (13, 66), (13, 67), (13, 68), (13, 69), (14, 10), (14, 15), (14, 16), (14, 17), (14, 21), (14, 22), (14, 26), (14, 37), (14, 40), (14, 43), (14, 44), (14, 45), (14, 46), (14, 47), (14, 50), (14, 51), (14, 57), (14, 61), (14, 66), (14, 67), (14, 69), (14, 70), (15, 6), (15, 11), (15, 17), (15, 20), (15, 24), (15, 25), (15, 26), (15, 31), (15, 34), (15, 35), (15, 40), (15, 45), (15, 47), (15, 51), (15, 53), (15, 62), (15, 67), (15, 68), (15, 70), (16, 1), (16, 2), (16, 4), (16, 9), (16, 12), (16, 17), (16, 21), (16, 22), (16, 23), (16, 24), (16, 27), (16, 28), (16, 31), (16, 32), (16, 33), (16, 38), (16, 39), (16, 42), (16, 46), (16, 48), (16, 50), (16, 52), (16, 54), (16, 55), (16, 56), (16, 57), (16, 59), (16, 67), (16, 69), (17, 1), (17, 6), (17, 9), (17, 12), (17, 13), (17, 18), (17, 23), (17, 24), (17, 25), (17, 26), (17, 27), (17, 28), (17, 30), (17, 34), (17, 38), (17, 40), (17, 44), (17, 45), (17, 50), (17, 52), (17, 53), (17, 62), (17, 63), (17, 64), (17, 67), (17, 68), (17, 70), (18, 2), (18, 9), (18, 14), (18, 19), (18, 22), (18, 25), (18, 29), (18, 30), (18, 33), (18, 34), (18, 36), (18, 37), (18, 41), (18, 43), (18, 44), (18, 45), (18, 46), (18, 49), (18, 50), (18, 51), (18, 54), (18, 62), (18, 66), (19, 13), (19, 14), (19, 15), (19, 23), (19, 26), (19, 32), (19, 33), (19, 38), (19, 44), (19, 46), (19, 48), (19, 55), (19, 56), (19, 64), (19, 70), (20, 6), (20, 11), (20, 12), (20, 18), (20, 19), (20, 21), (20, 24), (20, 26), (20, 30), (20, 36), (20, 40), (20, 42), (20, 44), (20, 45), (20, 46), (20, 50), (20, 55), (20, 58), (20, 60), (20, 70), (21, 9), (21, 13), (21, 15), (21, 17), (21, 18), (21, 19), (21, 22), (21, 24), (21, 32), (21, 39), (21, 40), (21, 41), (21, 42), (21, 51), (21, 53), (21, 54), (21, 56), (21, 59), (21, 61), (21, 63), (21, 65), (21, 66), (21, 70), (22, 2), (22, 15), (22, 17), (22, 19), (22, 25), (22, 28), (22, 31), (22, 33), (22, 36), (22, 38), (22, 40), (22, 46), (22, 48), (22, 49), (22, 50), (22, 51), (22, 53), (22, 54), (22, 58), (22, 60), (22, 62), (22, 64), (22, 70), (23, 7), (23, 8), (23, 15), (23, 24), (23, 37), (23, 39), (23, 43), (23, 44), (23, 47), (23, 50), (23, 51), (23, 57), (23, 61), (23, 62), (23, 63), (23, 65), (23, 67), (23, 68), (24, 2), (24, 4), (24, 7), (24, 12), (24, 13), (24, 18), (24, 19), (24, 34), (24, 37), (24, 39), (24, 40), (24, 47), (24, 48), (24, 49), (24, 53), (24, 54), (24, 58), (24, 61), (24, 62), (24, 65), (24, 67), (24, 68), (24, 70), (25, 20), (25, 26), (25, 27), (25, 38), (25, 43), (25, 45), (25, 53), (25, 56), (25, 63), (25, 65), (25, 69), (26, 16), (26, 31), (26, 34), (26, 35), (26, 36), (26, 37), (26, 39), (26, 45), (26, 48), (26, 50), (26, 53), (26, 56), (26, 57), (26, 58), (26, 59), (26, 60), (26, 61), (26, 62), (26, 64), (26, 65), (27, 2), (27, 11), (27, 12), (27, 14), (27, 22), (27, 23), (27, 29), (27, 30), (27, 31), (27, 32), (27, 34), (27, 39), (27, 41), (27, 42), (27, 45), (27, 50), (27, 51), (27, 52), (27, 62), (27, 66), (28, 15), (28, 24), (28, 26), (28, 27), (28, 30), (28, 31), (28, 34), (28, 36), (28, 39), (28, 47), (28, 51), (28, 52), (28, 53), (28, 57), (28, 59), (28, 63), (29, 12), (29, 13), (29, 21), (29, 26), (29, 28), (29, 38), (29, 40), (29, 48), (29, 51), (29, 58), (29, 59), (29, 62), (29, 66), (29, 69), (29, 70), (30, 10), (30, 14), (30, 16), (30, 22), (30, 23), (30, 33), (30, 37), (30, 40), (30, 41), (30, 45), (30, 47), (30, 49), (30, 51), (30, 53), (30, 56), (30, 60), (30, 63), (30, 64), (30, 65), (30, 68), (30, 70), (31, 2), (31, 4), (31, 12), (31, 18), (31, 21), (31, 23), (31, 34), (31, 35), (31, 37), (31, 42), (31, 45), (31, 50), (31, 51), (31, 54), (31, 56), (31, 57), (31, 58), (31, 60), (31, 64), (31, 66), (31, 67), (32, 3), (32, 5), (32, 17), (32, 23), (32, 25), (32, 30), (32, 33), (32, 35), (32, 37), (32, 39), (32, 44), (32, 45), (32, 48), (32, 50), (32, 53), (32, 56), (32, 60), (32, 63), (32, 65), (32, 69), (33, 6), (33, 7), (33, 13), (33, 14), (33, 15), (33, 20), (33, 24), (33, 25), (33, 28), (33, 35), (33, 36), (33, 39), (33, 44), (33, 46), (33, 49), (33, 50), (33, 51), (33, 52), (33, 54), (33, 55), (33, 56), (33, 58), (33, 62), (33, 63), (33, 64), (33, 68), (33, 69), (34, 1), (34, 7), (34, 10), (34, 11), (34, 13), (34, 25), (34, 29), (34, 30), (34, 36), (34, 37), (34, 38), (34, 40), (34, 41), (34, 48), (34, 50), (34, 52), (34, 54), (34, 55), (34, 59), (34, 67), (34, 70), (35, 9), (35, 13), (35, 14), (35, 21), (35, 23), (35, 28), (35, 34), (35, 38), (35, 43), (35, 45), (35, 48), (35, 49), (35, 50), (35, 58), (35, 59), (35, 61), (35, 64), (35, 65), (35, 67), (36, 3), (36, 12), (36, 19), (36, 23), (36, 30), (36, 40), (36, 41), (36, 43), (36, 46), (36, 49), (36, 56), (36, 58), (36, 60), (36, 61), (36, 66), (36, 67), (37, 2), (37, 3), (37, 12), (37, 15), (37, 16), (37, 17), (37, 38), (37, 40), (37, 45), (37, 46), (37, 47), (37, 51), (37, 52), (37, 53), (37, 56), (37, 60), (37, 63), (37, 65), (38, 6), (38, 7), (38, 9), (38, 13), (38, 18), (38, 20), (38, 21), (38, 26), (38, 28), (38, 32), (38, 36), (38, 41), (38, 42), (38, 51), (38, 53), (38, 56), (38, 57), (38, 58), (38, 65), (38, 69), (39, 3), (39, 4), (39, 5), (39, 17), (39, 18), (39, 19), (39, 20), (39, 25), (39, 30), (39, 37), (39, 42), (39, 44), (39, 45), (39, 47), (39, 49), (39, 50), (39, 51), (39, 53), (39, 54), (39, 58), (39, 61), (39, 63), (39, 65), (39, 66), (39, 68), (40, 2), (40, 6), (40, 7), (40, 8), (40, 16), (40, 19), (40, 23), (40, 25), (40, 28), (40, 31), (40, 32), (40, 39), (40, 42), (40, 44), (40, 50), (40, 51), (40, 52), (40, 55), (40, 57), (40, 58), (40, 61), (40, 63), (40, 68), (40, 69), (41, 1), (41, 11), (41, 15), (41, 16), (41, 17), (41, 23), (41, 24), (41, 25), (41, 39), (41, 40), (41, 42), (41, 54), (41, 60), (41, 61), (41, 65), (41, 69), (42, 1), (42, 3), (42, 9), (42, 11), (42, 17), (42, 18), (42, 19), (42, 22), (42, 23), (42, 24), (42, 26), (42, 33), (42, 36), (42, 46), (42, 47), (42, 49), (42, 54), (42, 56), (42, 58), (42, 63), (42, 69), (43, 2), (43, 5), (43, 8), (43, 9), (43, 11), (43, 15), (43, 16), (43, 26), (43, 27), (43, 32), (43, 34), (43, 46), (43, 50), (43, 55), (43, 56), (43, 65), (43, 68), (44, 2), (44, 3), (44, 7), (44, 13), (44, 16), (44, 22), (44, 25), (44, 26), (44, 27), (44, 31), (44, 43), (44, 46), (44, 47), (44, 48), (44, 50), (44, 53), (44, 55), (44, 56), (44, 57), (44, 58), (44, 59), (44, 62), (44, 66), (45, 3), (45, 7), (45, 12), (45, 16), (45, 22), (45, 29), (45, 36), (45, 38), (45, 40), (45, 41), (45, 42), (45, 44), (45, 47), (45, 48), (45, 53), (45, 54), (45, 59), (45, 66), (45, 69), (46, 4), (46, 21), (46, 23), (46, 24), (46, 31), (46, 34), (46, 35), (46, 40), (46, 49), (46, 50), (46, 52), (46, 54), (46, 64), (46, 66), (46, 69), (46, 70), (47, 5), (47, 17), (47, 26), (47, 36), (47, 49), (47, 59), (47, 65), (47, 69), (48, 1), (48, 6), (48, 8), (48, 10), (48, 12), (48, 18), (48, 39), (48, 40), (48, 41), (48, 47), (48, 50), (48, 55), (48, 59), (48, 64), (48, 68), (49, 4), (49, 9), (49, 10), (49, 13), (49, 17), (49, 19), (49, 20), (49, 27), (49, 28), (49, 29), (49, 31), (49, 32), (49, 34), (49, 40), (49, 41), (49, 45), (49, 51), (49, 57), (49, 61), (49, 65), (50, 5), (50, 9), (50, 10), (50, 12), (50, 15), (50, 24), (50, 25), (50, 41), (50, 42), (50, 52), (50, 53), (50, 55), (50, 56), (50, 60), (50, 61), (50, 64), (50, 66), (50, 69), (51, 9), (51, 10), (51, 19), (51, 20), (51, 25), (51, 26), (51, 32), (51, 35), (51, 36), (51, 45), (51, 46), (51, 47), (51, 48), (51, 53), (51, 54), (51, 55), (51, 57), (51, 61), (51, 65), (51, 66), (51, 67), (51, 69), (51, 70), (52, 1), (52, 14), (52, 15), (52, 19), (52, 23), (52, 26), (52, 29), (52, 38), (52, 39), (52, 47), (52, 49), (52, 51), (52, 55), (52, 56), (52, 58), (52, 61), (52, 62), (52, 69), (53, 3), (53, 7), (53, 12), (53, 14), (53, 16), (53, 19), (53, 33), (53, 35), (53, 41), (53, 46), (53, 47), (53, 48), (53, 55), (53, 62), (53, 69), (53, 70), (54, 3), (54, 5), (54, 6), (54, 7), (54, 9), (54, 15), (54, 20), (54, 25), (54, 28), (54, 38), (54, 40), (54, 44), (54, 53), (54, 58), (54, 59), (54, 61), (54, 62), (54, 63), (54, 66), (54, 68), (55, 15), (55, 22), (55, 24), (55, 31), (55, 32), (55, 39), (55, 41), (55, 42), (55, 45), (55, 46), (55, 49), (55, 63), (55, 64), (55, 66), (56, 1), (56, 3), (56, 11), (56, 15), (56, 17), (56, 20), (56, 23), (56, 27), (56, 28), (56, 40), (56, 47), (56, 51), (56, 66), (56, 68), (57, 3), (57, 4), (57, 8), (57, 12), (57, 24), (57, 29), (57, 30), (57, 32), (57, 33), (57, 34), (57, 37), (57, 43), (57, 45), (57, 46), (57, 52), (57, 55), (57, 58), (57, 63), (57, 64), (57, 66), (57, 67), (57, 68), (58, 2), (58, 5), (58, 11), (58, 14), (58, 16), (58, 21), (58, 28), (58, 30), (58, 47), (58, 53), (58, 55), (58, 67), (58, 70), (59, 9), (59, 18), (59, 20), (59, 37), (59, 39), (59, 41), (59, 52), (60, 2), (60, 7), (60, 10), (60, 17), (60, 18), (60, 21), (60, 28), (60, 33), (60, 40), (60, 42), (60, 43), (60, 45), (60, 49), (60, 52), (60, 53), (60, 56), (60, 59), (60, 62), (60, 69), (61, 7), (61, 9), (61, 15), (61, 16), (61, 19), (61, 25), (61, 30), (61, 32), (61, 38), (61, 44), (61, 45), (61, 47), (61, 48), (61, 53), (61, 56), (61, 60), (61, 62), (61, 65), (61, 66), (61, 68), (62, 5), (62, 6), (62, 12), (62, 13), (62, 19), (62, 20), (62, 25), (62, 37), (62, 40), (62, 41), (62, 43), (62, 46), (62, 47), (62, 49), (62, 51), (62, 55), (62, 65), (62, 70), (63, 4), (63, 5), (63, 24), (63, 38), (63, 52), (63, 58), (63, 59), (63, 60), (63, 62), (63, 67), (63, 69), (63, 70), (64, 1), (64, 3), (64, 5), (64, 6), (64, 10), (64, 18), (64, 24), (64, 27), (64, 36), (64, 41), (64, 44), (64, 49), (64, 52), (64, 53), (64, 54), (64, 56), (64, 58), (64, 60), (64, 61), (64, 66), (65, 2), (65, 16), (65, 17), (65, 18), (65, 19), (65, 20), (65, 33), (65, 42), (65, 44), (65, 45), (65, 48), (65, 54), (65, 57), (65, 63), (65, 66), (65, 69), (66, 2), (66, 11), (66, 15), (66, 28), (66, 30), (66, 33), (66, 35), (66, 38), (66, 42), (66, 47), (66, 49), (66, 58), (66, 63), (66, 70), (67, 2), (67, 9), (67, 19), (67, 21), (67, 22), (67, 27), (67, 29), (67, 30), (67, 32), (67, 33), (67, 37), (67, 40), (67, 42), (67, 43), (67, 47), (67, 59), (67, 60), (67, 61), (67, 62), (67, 64), (67, 69), (67, 70), (68, 1), (68, 7), (68, 10), (68, 16), (68, 18), (68, 19), (68, 20), (68, 25), (68, 31), (68, 34), (68, 35), (68, 38), (68, 51), (68, 55), (68, 60), (68, 62), (68, 65), (69, 1), (69, 6), (69, 11), (69, 15), (69, 19), (69, 24), (69, 30), (69, 31), (69, 36), (69, 37), (69, 43), (69, 59), (69, 64), (69, 66), (70, 1), (70, 6), (70, 12), (70, 13), (70, 16), (70, 26), (70, 33), (70, 37), (70, 38), (70, 43), (70, 45), (70, 48), (70, 50), (70, 55), (70, 57), (70, 59), (70, 61), (70, 65)])

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
original_name = "pipelines_plot_original_70.png"
nx.draw_networkx(G, pos=pos, with_labels=True)
plt.savefig(original_name, bbox_inches='tight')

# Save solution graph
# Note: red nodes are in the set, blue nodes are not
solution_name = "pipelines_plot_solution_70.png"
nx.draw_networkx(k, pos=pos, with_labels=True, node_color='r', font_color='k')
nx.draw_networkx(othersubgraph, pos=pos, with_labels=True, node_color='b', font_color='w')
plt.savefig(solution_name, bbox_inches='tight')

print("Your plots are saved to {} and {}".format(original_name, solution_name))
