# List Transformer: map() aur lambda ka use karke list ke har number ka square nikalo. 

numbers = []

# taking 5 input number
for i in range(5) :
  number = int(input("Enter a number : "))
  numbers.append(number)

square = map(lambda x : x * x,numbers)

print("Square :",list(square))