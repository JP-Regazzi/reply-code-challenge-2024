import networkx as nx
from read_data import read_input

def bellman_ford(graph, source, quantities):  # dict key:quantity
    # Initialize distances
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    # Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor in graph[node]:

                min_weight = float('inf')
                min_quantity = float('inf')
                min_tile = None

                # Find the smallest weight for which the quantity is > 0
                for tile, temp_weight in graph[node][neighbor]['weight'].items():
                    if quantities.get(tile) > 0 and temp_weight < min_weight:
                        min_weight = temp_weight
                        min_tile = tile

                if min_tile:
                    quantities[min_tile] -= 1
                else:
                    "ERROR NO LEFT TILES"

                weight = min_weight

                if weight < 0: # Chegamos no silver
                    pass # Fazer algo pra +inf nele

                # weight do original
                #weight = graph[node][neighbor]['weight']
                
                # Do codigo original
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances

# Example usage
filename = './data/00-trailer.txt'  # Change this to your input file
W, H, golden_points, silver_points, tiles = read_input(filename)

"""
# Create a NetworkX graph
G = nx.Graph()
for tile in tiles:
    for movement in tile.movements:
        for gp1 in golden_points:
            for gp2 in golden_points:
                if gp1 != gp2:
                    distance = abs(gp1.x - gp2.x) + abs(gp1.y - gp2.y)
                    if str(distance) in movement:
                        G.add_edge(gp1, gp2, weight=tile.cost)
"""

# Assuming the first golden point as the source
source = (0, 0)
visited_golden_points = set()

# Go through all golden points
while len(visited_golden_points) < len(golden_points):
    shortest_paths = bellman_ford(G, source)
    closest_golden_point = min(golden_points, key=lambda gp: shortest_paths[(gp.x, gp.y)])
    visited_golden_points.add(closest_golden_point)
    print(f"Visited golden point at ({closest_golden_point.x}, {closest_golden_point.y}")
    print(f"Distance from {(source.x, source.y)} to {(closest_golden_point.x, closest_golden_point.y)} : {distance}")
    source = (closest_golden_point.x, closest_golden_point.y)