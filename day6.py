# Part 1
with open("input.txt") as f:
    grid = f.read().strip().split("\n")
r = len(grid)
c = len(grid[0])
# Find the starting position
found = False
for i in range(r):
    for j in range(c):
        if grid[i][j] == "^":
            found = True
            break
    if found:
        break
# Moving part
dir = 0
dd = [[-1, 0], [0, 1], [1, 0], [0, -1]]
# Loop through
seen = set()
while True:
    seen.add((i, j))
    next_i = i + dd[dir][0]
    next_j = j + dd[dir][1]
    if not (0 <= next_i < r and 0 <= next_j < c):
        break
    if grid[next_i][next_j] == "#":
        dir = (dir + 1) % 4
    else:
        i, j = next_i, next_j
print(len(seen))
