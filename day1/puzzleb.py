myfile = open("./puzzleInputA.txt")
array = []
array1 = [] 

for line in myfile:
    array.append(int(line))

for x in range(len(array)):
    sum = 0
    if x > 1997:
        break 
    for y in range(3):
        numbertosum = x + y
        # print("x:", x)
        # print("y:", y)
        # print("array:", array[(numbertosum)])
        sum = sum + array[(numbertosum)]
    # print(sum)
    array1.append(sum)

print(array1)

increased = 0

for x in range(len(array1)):
    # print(x)
    if x > 1996:
        break
    if array1[x] < array1[(x+1)]:
        # print("yes")
        increased = increased + 1
    else:
        continue

print(increased)