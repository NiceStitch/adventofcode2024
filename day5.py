# Part 1
with open("input.txt") as f:
    test, updates = f.read().strip().split("\n\n")
    rules = []
    for line in test.split("\n"):
        st, nd = line.split("|")
        rules.append((int(st), int(nd)))
    updates = [list(map(int, line.split(","))) for line in updates.split("\n")]
def check(update):
    index = {}
    for i, num in enumerate(update):
        index[num] = i
    for st, nd in rules:
        if st in index and nd in index and not index[st] < index[nd]:
            return False, 0
    return True, update[len(update) // 2]
result = 0
for update in updates:
    good, mid = check(update)
    if good:
        result += mid
print(result)

# Part 2
