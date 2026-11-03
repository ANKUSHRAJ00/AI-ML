# Even Number Filter: filter() aur lambda ka use karke list se saare even numbers nikalo. 

numbers = []

# taking 5 inputs 
for i in range(5) :
  number = int(input("Enter numbers : "))
  numbers.append(number)

even_number = filter(lambda x : x % 2 == 0,numbers)
print("Even Number :",list(even_number))