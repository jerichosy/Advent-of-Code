with open("input.txt") as f:
    lines = f.read().splitlines()

# print(lines)

WORD = "XMAS"

start_coords = []
for idx, line in enumerate(lines):
    for idy, c in enumerate(line):
        if c == WORD[0]:
            start_coords.append((idx, idy))

directions = [
    (0, 1),  # right
    (-1, 1),  # up-right
    (-1, 0),  # up
    (-1, -1),  # up-left
    (0, -1),  # left
    (1, -1),  # bottom-left
    (1, 0),  # bottom
    (1, 1),  # bottom-right
]

def search_from(r, c, direction, idx):
    if idx == len(WORD):
        return True

    dr, dc = direction
    nr, nc = r + dr, c + dc

    within_bounds = nr >=0 and nr < len(lines) and nc >= 0 and nc < len(lines[0])
    # print(within_bounds, nr, nc)

    if within_bounds and lines[nr][nc] == WORD[idx]:
        return search_from(nr, nc, direction, idx+1)

    return False

count = 0
for r, c in start_coords:
    # print(r, c)
    for direction in directions:
        if search_from(r, c, direction, 1):
            # print(r, c)
            count += 1

print(count)
