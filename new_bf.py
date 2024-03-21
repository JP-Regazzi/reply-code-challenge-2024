import networkx as nx
from read_data import read_input

def bellman_ford(graph, source):
    # Initialize distances
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    # Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor in graph[node]:
                weight = graph[node][neighbor]['weight']
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    # Check for negative cycles
    for node in graph:
        for neighbor in graph[node]:
            weight = graph[node][neighbor]['weight']
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative cycle")

    return distances

# Example usage
filename = './data/00-trailer.txt'  # Change this to your input file
W, H, golden_points, silver_points, tiles = read_input(filename)

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

# Assuming the first golden point as the source
source = golden_points[0]

# Finding shortest paths from the source to all other golden points
shortest_distances = bellman_ford(G, source)

# Printing shortest distances
for point, distance in shortest_distances.items():
    print("Distance from", (source.x, source.y), "to", (point.x, point.y), ":", distance)
