#triangle

def triangle(n):
    count = 1
    subcount = 1
    triList = []
    
    while count <= n:
        while subcount <= count:
            space = "   " * (n - subcount)
            rev = triList[::-1]
            triList.append(subcount)
            
            print("{}{}".format( space, triList + rev))
            subcount += 1
        count += 1
        
triangle(10)
