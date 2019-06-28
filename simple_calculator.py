#simple calculator;


arith_Operation = input("Choose Arithmetic Operation: ")
first_input = int(input("Enter the First Value:\t"))
second_input = int(input("Enter the Second Value:\t"))

if(arith_Operation == "+"):
	sum = first_input + second_input
	print(sum)

elif(arith_Operation == "-"):
	diff = first_input - second_input
	print(diff)

elif(arith_Operation == "*"):
	product = first_input * second_input
	prinf(product)

elif(arith_Operation == "/"):
	quotient = first_input / second_input
	print(quotient)

else:
	print("Pls. Enter a valid Value")




