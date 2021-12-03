myfile = open("./day2/puzzleInputA.txt")
array = []

for line in myfile:
    array.append(str(line.replace('\n', '')))

# print(array)
 
dept = 0
forward = 0
aim = 0

for x in range(len(array)):
    direction = ""
    delta = 0
    split = array[x].split()
    direction = split[0]
    delta = int(split[1])
    if direction == "up":
        aim = aim - delta
        # print(dept, "up")
    if direction == "down":
        aim = aim + delta
        # print(dept, "down")
    if direction == "forward":
        change = delta * aim
        forward = forward + delta
        dept = dept + change

print(dept * forward)
