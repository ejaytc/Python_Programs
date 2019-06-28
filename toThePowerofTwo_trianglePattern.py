#Binary Triangle



Range = int(input("Input binary triangle range: "))
binList = []
count = 1
subcount = 1
binary = 1

while count <= Range:
    
    while subcount <= count:
        
        space = "   " *(Range - subcount)
        binRev = binList[::-1]
        binList.append(binary)
        binary += binary
        print("{}{}".format(space ,binList + binRev))
        
        subcount += 1
    count += 1
