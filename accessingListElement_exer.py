# accessing list elements.

colors = ["red","yellow", "blue", "green", "violet"]

print("List length ",len(colors))

print("\nPrint the colors one by one: \n")
for i in range(0,5):
	print(colors[i]) 
	
print("\nPrint all colors by red upto violet: \n")
for listDown in range(1,6):
	print(colors[0:listDown]) 
	
print("\nPrint the colors one by one in list using while statement: \n")

i = 1
lowerLimit = 0
while(i <= 5):
	print(colors[lowerLimit:i])
	lowerLimit, i = i, i + 1

print("\nprintin the colors one by one in list using for statement")
Limit = 0
for colorList in range(1,6):
	print(colors[Limit:colorList])
	Limit +=1