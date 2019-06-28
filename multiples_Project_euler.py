def multiples(n):
    given = 0
    for value in range(1,n):
        if(value % 3 == 0):
            print("value of 3 ", value)
            given += value
			
        elif(value % 5 == 0):
            print("value of 5 ", value)
            given += value
			
    return print("total sum of 3 and 5 ", given)
    

if __name__ == '__main__':
	multiples(1000)
