# Check if it's increasing or decreasing and if the distance is correct
def is_safe(report):
    increasing = all(
        report[i + 1] - report[i] > 0 and 1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(
        report[i] - report[i + 1] > 0 and 1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing
# Load data and run the function
with open('data.txt', 'r') as file:
    reports = [list(map(int, line.split())) for line in file.readlines()]
safe = sum(1 for report in reports if is_safe(report))
print(safe)
# Part 2

def is_safe2(report):
    # Recheck for the first condition
    def is_increasing(arr):
        return all(arr[i + 1] - arr[i] > 0 and 1 <= arr[i + 1] - arr[i] <= 3 for i in range(len(arr) - 1))
    def is_decreasing(arr):
        return all(arr[i] - arr[i + 1] > 0 and 1 <= arr[i] - arr[i + 1] <= 3 for i in range(len(arr) - 1))
    if is_increasing(report) or is_decreasing(report):
        return True
    # Check for all possible options in a level
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_increasing(modified_report) or is_decreasing(modified_report):
            return True
    return False
# Reloads the data and runs the part 2 function
with open('data.txt', 'r') as file:
    reports = [list(map(int, line.split())) for line in file.readlines()]
safe_reports = sum(1 for report in reports if is_safe2(report))

print(safe_reports)