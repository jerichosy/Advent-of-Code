with open("input.txt") as f:
    lines = f.read().splitlines()

mul_regex_string = r"mul\(\d*,\d*\)"
n_regex_string = r"(\d*),(\d*)"

import re

all_matches = re.findall(mul_regex_string, "".join(lines))

# print(all_matches)

total = 0
for match in all_matches:
    n = re.search(n_regex_string, match)
    total += int(n.group(1)) * int(n.group(2))

print(total)
