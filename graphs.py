import networkx as nx
import matplotlib.pyplot as plt

from read_data import generate_movements

tile_movements = {
    "3": [(1, 0)],  # From left to right
    "5": [(1, 1)],  # From down to right (diagonal)
    "6": [(0, 1)],  # From left to down
    "7": [(1, 0), (0, 1), (1, 1)],  # Multiple directions
    "9": [(-1, 1)],  # From up to right (diagonal)
    "A": [(-1, 0)],  # From left to up
    "B": [(1, 0), (-1, 0)],  # From left to right and left to up
    "C": [(0, 1), (0, -1)],  # From up to down
    "D": [(0, 1), (-1, 1)],  # From up to down and up to right (diagonal)
    "E": [(-1, 0), (0, 1)],  # From left to up and left to down
    "F": [(1, 0), (0, 1), (-1, 0), (0, -1)],  # All straight directions
    # Adding 'C3' as an example, assuming it allows movement from left to right and up to down based on the 'C3' pattern
    "C3": [(1, 0), (0, 1)]  # From left to right and up to down
}


# Adjusting the parse_input_file function to handle the BOM
def parse_input_file_fixed(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as file:  # Using 'utf-8-sig' to handle BOM
        lines = file.readlines()

    grid_width, grid_height, num_golden_points, num_silver_points, num_tile_types = map(int, lines[0].strip().split())

    golden_points = [tuple(map(int, lines[i].strip().split())) for i in range(1, 1 + num_golden_points)]
    silver_points = {tuple(map(int, lines[i].strip().split()[:2])): int(lines[i].strip().split()[2]) for i in range(1 + num_golden_points, 1 + num_golden_points + num_silver_points)}
    tiles = {lines[i].strip().split()[0]: {'cost': int(lines[i].strip().split()[1]), 'quantity': int(lines[i].strip().split()[2])} for i in range(1 + num_golden_points + num_silver_points, 1 + num_golden_points + num_silver_points + num_tile_types)}

    return grid_width, grid_height, golden_points, silver_points, tiles

# Read and parse the input file
grid_width, grid_height, golden_points, silver_points, tiles = parse_input_file_fixed('./data/00-trailer.txt')

# Adjusting the function to use the weight (cost) of tiles as the edge weight in the graph
def create_nx_graph_with_tile_weight(grid_width, grid_height, tiles, movements):
    G = nx.DiGraph()

    for y in range(grid_height):
        for x in range(grid_width):
            node = (x, y)
            G.add_node(node)

            for tile, dirs in movements.items():
                for dx, dy in dirs:
                    neighbor = (x + dx, y + dy)
                    # Ensure the neighbor is within grid bounds
                    if 0 <= neighbor[0] < grid_width and 0 <= neighbor[1] < grid_height:
                        if G.has_edge(node, neighbor):
                            # If the edge already exists, update the weight dictionary
                            G[node][neighbor][tile] = tiles.get(tile, {}).get('cost', float('inf'))
                        else:
                            # Otherwise, add a new edge with the initial weight dictionary
                            G.add_edge(node, neighbor, **{tile: tiles.get(tile, {}).get('cost', float('inf'))})

    return G

# Create the graph with detailed tile cost as weights
G_tile_weight = create_nx_graph_with_tile_weight(grid_width, grid_height, tiles, tile_movements)

# Print the edges from the node (0, 0) to demonstrate the new weight format with costs
print("Edges and detailed weights (costs) from node (0, 0):")
for edge in G_tile_weight.edges((0, 0), data=True):
    print(edge)

# Use the detailed graph creation function
G_detailed = create_nx_graph_with_tile_weight(grid_width, grid_height, tiles, tile_movements)

# Display basic information about the detailed graph
print(f"Number of nodes: {G_detailed.number_of_nodes()}")
print(f"Number of edges: {G_detailed.number_of_edges()}")

# Example: print edges from the node (0, 0) to demonstrate actual weights
print("Edges and actual weights from node (0, 0):")
for edge in G_detailed.edges((0, 0), data=True):
    print(edge)

# Position nodes using a grid layout for visualization
pos = {(x, y): (x, -y) for y in range(grid_height) for x in range(grid_width)}

plt.figure(figsize=(12, 8))
nx.draw(G_detailed, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10)
plt.title("Graph Representation of the Grid")
plt.show()
