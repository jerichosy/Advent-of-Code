with open("input.txt") as f:
    lines = f.read().splitlines()

safe_cnt = 0

for line in lines:
    report = list(map(int, line.split()))

    ascending = None
    for i in range(len(report) - 1):
        if abs(report[i] - report[i+1]) not in [1, 2, 3]:
            break  # get the next report

        if ascending is None:
            if report[i] < report[i+1]:
                ascending = True
            elif report[i] > report[i+1]:
                ascending = False

            assert ascending is not None

        if ascending:
            if report[i] > report[i+1]:
                break  # get the next report
        elif not ascending:
            if report[i] < report[i+1]:
                break  # get the next report

        if i == len(report) - 2:
            safe_cnt += 1

print(safe_cnt)
