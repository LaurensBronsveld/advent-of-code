
def count_surrounding_rolls(grid, x, y):
    adjacent_tiles = [(x-1, y-1), (x, y-1), (x+1, y-1),
                      (x-1, y),             (x+1, y),
                      (x-1, y+1), (x, y+1), (x+1, y+1)]
    
    count = 0
    for adj_x, adj_y in adjacent_tiles:
        if 0 <= adj_y < len(grid) and 0 <= adj_x < len(grid[0]):
            count += grid[adj_y][adj_x]
    return count

def remove_rolls(grid):
    accessable_rolls = 0
    for y, row in enumerate(grid):
        for x, roll in enumerate(row):
            if roll == 0:
                continue
            
            if count_surrounding_rolls(grid, x, y) < 4:
                print(f"Roll at ({x}, {y}) is accessable.")
                grid[y][x] = 0
                accessable_rolls += 1
    return accessable_rolls

def main():
    grid = []
    with open("day4/input.txt", "r") as f:
        for line in f:
            row = [0 if c == '.' else 1 for c in line.strip()]
            grid.append(row)  
    
    total_removed_rolls = 0
    while True: 
        removed_rolls = remove_rolls(grid)
        if removed_rolls == 0:  
            break
        total_removed_rolls += removed_rolls


    print(f"There are {total_removed_rolls} accessable rolls in the grid.")
if __name__ == '__main__':
    main()
