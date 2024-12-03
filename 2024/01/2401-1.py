with open("input.txt") as f:
    lines = f.read().splitlines()

l = []
r = []

for line in lines:
    left, right = line.split()
    l.append(int(left))
    r.append(int(right))

total_diff = 0
for left, right in zip(sorted(l), sorted(r)):
    total_diff += abs(left - right)

print(total_diff)
