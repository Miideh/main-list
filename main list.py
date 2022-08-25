names = []
max_length = 3

while len(names)<max_length:
    list = (input("enter the list of names"))
    names.append(list)
    print(names)
y = (input("names"))
if y in names:
    print("True. The name is in the list")
else:
    print("False. The name cannot be found in the list")