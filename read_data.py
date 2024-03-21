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
    def __init__(self, tid, cost, quantity):
        self.tid = tid
        self.cost = cost
        self.quantity = quantity

# Read input from file
def read_input(filename):
    with open(filename, 'r') as file:
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
        for _ in range(TL):
            tid, cost, quantity = file.readline().split()
            tiles.append(Tile(tid, int(cost), int(quantity)))

    return W, H, golden_points, silver_points, tiles

# Example usage
filename = 'input.txt'  # Change this to your input file
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
    print("  TID:", tile.tid, "cost:", tile.cost, "quantity:", tile.quantity)
