# Part 1
import re

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
# Part 2
def process_instructions(text):
    enabled = True #Enabled by default for the first line
    total_sum = 0
    
    
    do_dont_regex = r'do\(\)|don\'t\(\)'
    # Split on do or don't
    instructions = re.split(f'({do_dont_regex})', text)
    for instruction in instructions:
        instruction = instruction.strip() # Remove whitespaces just to be sure
        
        if instruction == "do()": # Switch to true if do()
            enabled = True
        
        elif instruction == "don't()": # Switch to false if don't
            enabled = False
        
        else: # Iterate thorough all the slices, if it comes after do() enabled is true and it will be counted, if after don't enabled is false so it won't be included in the count
            mul_matches = re.findall(regex, instruction)
            for match in mul_matches:
                if enabled:
                    a, b = map(int, match)
                    total_sum += a * b
    
    return total_sum

text = content # Lazy fix to reimplmement content after testing 
result = process_instructions(text)
print(f"Sum of enabled multiplications: {result}")
