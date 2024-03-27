import networkx as nx
from read_data import read_input
import graphs
import math

def bellman_ford(graph, source, quantities):  # dict key:quantity
    # Initialize distances
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    print(source)
    # Relax edges repeatedly
    for _ in range(len(graph) - 1):
        
        for node in graph:
            for neighbor in graph[node]:

                min_weight = float('inf')
                min_quantity = float('inf')
                min_tile = None

                # Find the smallest weight for which the quantity is > 0
                for tile, temp_weight in graph[node][neighbor].items():
                    if math.isinf(temp_weight):
                        continue
                    if quantities.get(tile) > 0 and temp_weight < min_weight:
                        min_weight = temp_weight
                        min_tile = tile

                if min_tile:

                    weight = min_weight

                    if weight < 0: # Chegamos no silver
                        pass # Fazer algo pra +inf nele
                    
                    if distances[node] + weight < distances[neighbor]:
                        distances[neighbor] = distances[node] + weight
                        quantities[min_tile] -= 1
                else:
                    "ERROR NO LEFT TILES"

    return distances

# Example usage
filename = './data/00-trailer.txt'  # Change this to your input file
grid_width, grid_height, golden_points, silver_points, tiles = graphs.parse_input_file_fixed(filename)


G = graphs.create_nx_graph_with_tile_weight(grid_width, grid_height, tiles, graphs.tile_movements)

# Assuming the first golden point as the source
source = golden_points[0]
visited_golden_points = set()

quantities = {key: values["quantity"] for key, values in tiles.items()}

# Go through all golden points
while len(visited_golden_points) < len(golden_points):
    shortest_paths = bellman_ford(G, source, quantities)
    visited_golden_points.add(source)
    closest_golden_point = min(set(golden_points) - visited_golden_points, key=lambda gp: shortest_paths[gp])
    visited_golden_points.add(closest_golden_point)
    print(f"Visited golden point at (closest_golden_point")
    print(f"Distance from {source} to {closest_golden_point} : {shortest_paths[closest_golden_point]}")
    source = closest_golden_point