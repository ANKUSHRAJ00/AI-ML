# Factorial Calculator: Function ka use karke kisi number ka factorial calculate karo. 

number = int(input("Enter a number : "))

def factorial(inputNumber) :
  
  factor =  1

  for i in  range(1,inputNumber+1):
    factor = factor*i
  return factor

result = factorial(number)
print("factorial of",number,"is :",result)