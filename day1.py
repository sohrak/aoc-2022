# Part 1
with open('input-1.txt', 'r') as f:
    lines = f.readlines()

maxCalories = 0
currentCalories = 0

for line in lines:
    if line.isspace():
        maxCalories = max(maxCalories, currentCalories)
        currentCalories = 0
    else:
        currentCalories += int(line)

maxCalories = max(maxCalories, currentCalories)
print(f'Part 1: {maxCalories}')

# Part 2
with open('input-1.txt', 'r') as f:
    lines = f.readlines()

calorieList = []
currentCalories = 0

for line in lines:
    if line.isspace():
        calorieList.append(currentCalories)
        currentCalories = 0
    else:
        currentCalories += int(line)

if currentCalories > 0:
    calorieList.append(currentCalories)

print(f'Part 2: {sum(sorted(calorieList)[-3:])}')
