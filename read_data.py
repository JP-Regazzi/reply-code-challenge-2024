tile_movements = {
    "3": ["left-right"],
    "5": ["down-right"],
    "6": ["left-down"],
    "7": ["left-right", "left-down", "down-right"],
    "9": ["up-right"],
    "96": ["left-down", "up-right"],
    "A": ["left-up"],
    "A5": ["left-up", "down-right"],
    "B": ["left-right", "left-up", "up-right"],
    "C": ["up-down"],
    "C3": ["left-right", "up-down"],
    "D": ["up-down", "up-right", "down-right"],
    "E": ["left-up", "left-down", "up-down"],
    "F": ["left-right", "left-down", "left-up", "up-down", "down-right", "up-right"]
}

def generate_movements(tile_id):
    movements = []
    if tile_id in tile_movements:
        movements = tile_movements[tile_id]
    
    generated_coords = set()
    for movement in movements:
        for direction in movement.split('-'):
            if direction == "left":
                generated_coords.add((-1, 0))
            elif direction == "right":
                generated_coords.add((1, 0))
            elif direction == "up":
                generated_coords.add((0, -1))
            elif direction == "down":
                generated_coords.add((0, 1))
    
    return generated_coords


class GoldenPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SilverPoint:  
    def __init__(self, x, y, score):
        self.x = x
        self.y = y
        self.score = score

class Tile:
    def __init__(self, tid, cost, quantity, movements):
        self.tid = tid
        self.cost = cost
        self.quantity = quantity
        self.movements = movements

def read_input(filename):
    with open(filename, 'r', encoding='utf-8-sig') as file:  # specifying 'utf-8-sig' for encoding
        W, H, GN, SM, TL = map(int, file.readline().split())

        golden_points = []
        for _ in range(GN):
            gx, gy = map(int, file.readline().split())
            golden_points.append(GoldenPoint(gx, gy))

        silver_points = []
        for _ in range(SM):
            sx, sy, score = map(int, file.readline().split())
            silver_points.append(SilverPoint(sx, sy, score))

        tiles = []
        while True:
            line = file.readline()
            if not line.strip():
                break
            tid, cost, quantity = line.split()
            movements = tile_movements[tid]
            
            tiles.append(Tile(tid, int(cost), int(quantity), movements))

    return W, H, golden_points, silver_points, tiles


# Example usage
filename = './data/00-trailer.txt'  # Change this to your input file
W, H, golden_points, silver_points, tiles = read_input(filename)

# Example printing
print("Width:", W)
print("Height:", H)
print("Golden Points:")
for point in golden_points:
    print("  x:", point.x, "y:", point.y)
print("Silver Points:")
for point in silver_points:
    print("  x:", point.x, "y:", point.y, "score:", point.score)
print("Tiles:")
for tile in tiles:
    print("  TID:", tile.tid, "cost:", tile.cost, "quantity:", tile.quantity, tile.movements)
