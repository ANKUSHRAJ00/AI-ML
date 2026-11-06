# Safe Calculator: Do numbers input lo aur division perform karo. 
# try-except se zero division aur invalid input handle karo.

try :

  num1 = int(input("Enter First Number : "))
  num2 = int(input("Enter Second Number : "))

  # Addition
  addition = num1 + num2
  print("Addition : ",addition)

  # Subtraction 
  subtraction = num1 - num2
  print("Subtraction : ",subtraction)

  # multiplication 
  multiplication = num1 * num2
  print("Multiplication : ",multiplication)

  # division
  division = num1/num2
  print("Division : ",division)

except ZeroDivisionError :
  print("Number can not be Divided by Zero")

except ValueError :
  print("Enter number instead of text")

finally :
  print("this Message is end line of code")