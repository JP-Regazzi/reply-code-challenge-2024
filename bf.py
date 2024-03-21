from read_data import read_input
# Example usage
filename = './data/00-trailer.txt'  # Change this to your input file
W, H, golden_points, silver_points, tiles = read_input(filename)


def bellman_ford(graph, source):
    # Initialize distances
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    # Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    # Check for negative cycles
    for node in graph:
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative cycle")

    return distances

graph = {
     'A': [('B', 3), ('C', 5)],
     'B': [('C', -2)],
     'C': [('D', 7)],
     'D': []
 }
source = 'A'
shortest_paths = bellman_ford(graph, source)
print(shortest_paths)
print([gp.x for gp in golden_points])
print([gp.y for gp in golden_points])


