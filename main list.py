names = []
max_length = 3

while len(names)<max_length:
   cleaned_names=input("enter the list of names")
   names.append(cleaned_names)
   new_name = [cleaned_names.lower() for cleaned_names in names]
   print(new_name)
new_selected=input("name.lower() in list of names in lowercase")
if new_selected in names:
    print ("True. The name is in the list")
else:
    print("False. The name cannot be found in the list")
 