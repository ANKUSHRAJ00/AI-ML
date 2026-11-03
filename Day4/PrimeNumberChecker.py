# Prime Number Checker: Function banao jo check kare ki diya gaya number prime hai ya nahi. 

number  = int(input("Enter a number : "))

def primeNumber(inputNumber) :

  if inputNumber <= 1 :
    print("the given number is not prime")
    return

  for i in range(2,inputNumber) :
    if inputNumber % i == 0 :
      print("the given number is not prime")
      break
  else:
    print("the given number is prime")


primeNumber(number) 