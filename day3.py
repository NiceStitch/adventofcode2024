# Part 1
import re

def mul(a, b):
    return a * b

with open('input2.txt', 'r') as file:
    content = file.read()  

regex = r'mul\((\d+),(\d+)\)'

matches = re.findall(regex, content)
print(len(matches))
sum = 0
for match in matches:
    a, b = map(int, match) 
    sum += a * b  

print(f"Total sum of all mul results: {sum}")
