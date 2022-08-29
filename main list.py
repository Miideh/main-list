names = []
max_length = 3

while len(names)<max_length:
   cleaned_names=input("enter the list of names")
   names.append(cleaned_names)
   new_name = [cleaned_names.lower() for cleaned_names in names]
   print(new_name)
#for i in range(len(names)):
 #    names[i]=names[i].lower()
selected_names=input("names")
if selected_names in names:
    print ("True. The name is in the list")
else:
    print("False. The name cannot be found in the list")