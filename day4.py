# Part 1
def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [
        (0, 1),    # right
        (0, -1),   # left
        (1, 0),    # down
        (-1, 0),   # up
        (1, 1),    # down-right diagonal
        (1, -1),   # down-left diagonal
        (-1, 1),   # up-right diagonal
        (-1, -1)   # up-left diagonal
    ]
    
    xmas_locations = set()
    
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols
    
    def check_word(start_r, start_c, dr, dc):
        word = ''
        coords = []
        r, c = start_r, start_c
        
        for _ in range(4):
            if not is_valid(r, c):
                return None
            word += grid[r][c]
            coords.append((r, c))
            r += dr
            c += dc
        
        return coords if word == 'XMAS' else None
    
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                result = check_word(r, c, dr, dc)
                if result:
                    xmas_locations.add(tuple(result))
    
    return xmas_locations

def solve_word_search(file_path):
    with open(file_path, 'r') as file:
        grid = [list(row.strip().replace(' ', '')) for row in file.readlines() if row.strip()]
    
    
    xmas_instances = find_xmas(grid)
    
    print(len(xmas_instances))


    return len(xmas_instances)

file_path = 'input.txt'
solve_word_search(file_path)