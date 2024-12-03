with open("input.txt") as f:
    lines = f.read().splitlines()

l = []
r = []

for line in lines:
    left, right = line.split()
    l.append(int(left))
    r.append(int(right))

from collections import Counter

r_counter = Counter(r)

total_similarity = 0
for num in l:
    total_similarity += r_counter[num] * num

print(total_similarity)
