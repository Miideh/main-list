names = []
max_length = 3

while len(names)<max_length:
   New_selected=input("enter the list of names")
   names.append(New_selected.lower())
   new_name = [New_selected.lower() for New_selected in names]
   print(new_name)
new_selected=input("name")
if new_selected.lower() in names:
    print ("True. The name is in the list")
else:
    print("False. The name cannot be found in the list")
 