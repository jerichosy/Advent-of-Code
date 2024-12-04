with open("input.txt") as f:
    lines = f.read().splitlines()

mul_regex_string = r"mul\(\d*,\d*\)"
do_regex_string = r"do\(\)"
dont_regex_string = r"don't\(\)"
n_regex_string = r"(\d*),(\d*)"

import re

all_mul = re.finditer(mul_regex_string, "".join(lines))
all_do = re.finditer(do_regex_string, "".join(lines))
all_dont = re.finditer(dont_regex_string, "".join(lines))
all_mul = {match.start(): match.group(0) for match in all_mul}
all_do = {match.start(): True for match in all_do}
all_dont = {match.start(): False for match in all_dont}

all_matches = {**all_mul, **all_do, **all_dont}
all_matches = {k: v for k, v in sorted(all_matches.items(), key=lambda item: item[0])}

total = 0
# print(all_matches)
mul_enabled = True
for start, match in all_matches.items():
    # print(start, match)
    # pass
    if isinstance(match, bool):
        if match:
            mul_enabled = True
        else:
            mul_enabled = False
    elif mul_enabled:
        n = re.search(n_regex_string, match)
        total += int(n.group(1)) * int(n.group(2))

print(total)
