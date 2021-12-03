myfile = open("./puzzleInputA.txt")
array = []

for line in myfile:
    array.append(int(line))

print(array)
increased = 0

for x in range(len(array)):
    print(x)
    if x > 1998:
        break
    if array[x] < array[(x+1)]:
        print("yes")
        increased = increased + 1
    else:
        continue

print(increased)