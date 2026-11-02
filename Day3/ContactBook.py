# Contact Book: Dictionary ka use karke names aur phone numbers store karo.
# User name enter kare toh uska number show karo. 


contact_book = {
"Ankush" : 1234,
"Rishu" : 5678,
"Nirbhay" : 6565
}

name = input("Enter a name to search in contact : ")

# Displaying Number
if name in contact_book :
  print("Phone no : ",contact_book.get(name))
else :
  print("No contact found")

