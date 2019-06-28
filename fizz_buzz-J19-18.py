#fizz buzz
while True:
    
    try:
        userInput = int(input("Input an integer: "))
        for num in list(range(userInput)):
            if num % 15 == 0:
                print("{} fizz buzz".format(num))
            elif num % 3 == 0:
                print("{} fizz".format(num))
            elif num % 5 == 0:
                print("{} buzz".format(num))
            else:
                print(num)
    except ValueError as valErr:
        print(valErr)
