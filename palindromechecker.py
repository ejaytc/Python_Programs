#palindrome checker;

def palindrome():
    global userInput
    strList = [ i.lower for i in userInput]
    strRev = strList[::-1]
    if strRev == strList:
        print("{} is a Palindrome\n".format(userInput))
    else:
        print("{} not a Palindrome\n".format(userInput))


while True:
    userInput = input("Input String: ")
    palindrome()
    run = input("Try Again(Y/n): ")
    if run == "N" or run == "n":
        quit()
        break;
