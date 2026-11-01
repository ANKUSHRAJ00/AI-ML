print()
print("------Guess this secret number------")
print()
print("HINT : it is a 4 digit number")

number = 1793
print()

while True :
  inputNumber = int(input("Guess that number : "))

  if inputNumber < number :
      print("Nah! bro, Guess High ")

  elif inputNumber > number :
        print("Nah! bro, Guess Low ")
  else :
        print("Woohoo!, Correct")
        break