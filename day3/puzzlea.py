myfile = open("./day3/puzzleInputA.txt")
array = []

for line in myfile:
    array.append(str(line.replace('\n', '')))

# PN stands for positive negative
PNcount = []

# Make PNcount string zeroed
for x in range(len(str(array[0]))):
    PNcount.append(int(0))
    
# loop trough all binaries and if some are positive add a point
for y in range(len(array)):
    for z in range(len(str(array[0]))):
        # print("z", z)
        if str(array[y])[z] == "1":
            PNcount[z] = PNcount[z] + 1
        if str(array[y])[z] == "0":
            PNcount[z] = PNcount[z] - 1

# Decode PNcount
decodedPNcount = []
for q in range(len(PNcount)):
    if PNcount[q] > 0:
        decodedPNcount.append(int(1))
    if PNcount[q] < 0:
        decodedPNcount.append(int(0))

def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += str(ele) 
    return str1 

def toEpsilon(binary):
    str1 = "" 
    for ele in binary: 
        if ele == 1:
            str1 += str(0)
        if ele == 0:
            str1 += str(1)
    return str1 


# print(array)

print(len(str(array[0]))) 
print(PNcount)
print(decodedPNcount)
gammaInDecimal = int(listToString(decodedPNcount), 2)
EpsilonInDeciaml = int(listToString(toEpsilon(decodedPNcount)), 2)

print(gammaInDecimal * EpsilonInDeciaml)





