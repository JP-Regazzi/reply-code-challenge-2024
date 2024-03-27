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

def main(input_file):
      # Change this to your input file
    W, H, golden_points, silver_points, tiles = read_input(input_file)
    
    graph = {
         'A': [('B', 3), ('C', 5)],
         'B': [('C', -2)],
         'C': [('D', 7)],
         'D': []
    }

    source = 'A'
    visited_golden_points = set()

    while len(visited_golden_points) < len(golden_points):
        shortest_paths = bellman_ford(graph, source)
        closest_golden_point = min(golden_points, key=lambda gp: shortest_paths[(gp.x, gp.y)])
        visited_golden_points.add(closest_golden_point)
        source = (closest_golden_point.x, closest_golden_point.y)
        print(f"Visited golden point at ({closest_golden_point.x}, {closest_golden_point.y})")


if __name__ == "__main__": # So para teste, vamos criar 
    
    input_file = './data/00-trailer.txt'
    main(input_file)
    print([gp.x for gp in golden_points])
    print([gp.y for gp in golden_points])


