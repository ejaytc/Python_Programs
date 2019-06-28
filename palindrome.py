# palindrome

def palindrom(userInput):
    stringList = []
    stringLenght = len(userInput) -2
    while stringLenght >= 0:
        stringList.append(userInput[stringLenght])
        stringLenght -= 1
        
    print( list(userInput) + stringList)

if __name__ == "__main__":

    userInput = input("Input String: ")
    palindrom(userInput)
