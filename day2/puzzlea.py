myfile = open("./day2/puzzleInputA.txt")
array = []

for line in myfile:
    array.append(str(line.replace('\n', '')))

# print(array)
 
dept = 0
forward = 0

for x in range(len(array)):
    direction = ""
    delta = 0
    split = array[x].split()
    direction = split[0]
    delta = int(split[1])
    if direction == "up":
        dept = dept - delta
        print(dept, "up")
    if direction == "down":
        dept = dept + delta
        print(dept, "down")
    if direction == "forward":
        forward = forward + delta

print(dept * forward)
