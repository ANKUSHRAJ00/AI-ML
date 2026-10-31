product1 = input("Enter product1 : ")
quantity1 = float(input("Enter quantity of product1 : "))
price1 = float(input("Enter price of product1 : "))

product2 = input("Enter product2 : ")
quantity2 = float(input("Enter quantity of product2 : "))
price2 = float(input("Enter price of product2 : "))

product3 = input("Enter product3 : ")
quantity3 = float(input("Enter quantity of product3 : "))
price3 = float(input("Enter price of product3 : "))

totalPrice1 = (quantity1 * price1)
totalPrice2 = (quantity2 * price2)
totalPrice3 = (quantity3 * price3)

finalTotal = totalPrice1 + totalPrice2 + totalPrice3
gst = finalTotal * 0.18

finalAmount = finalTotal + gst

print("-----------------BILL---------------------------")

print("Product 1st : ",product1)
print(product1, "Quantity : ",quantity1)
print("price of each unit of ",product1,"is : ",price1)
print("Total price of ",product1,"is : ",totalPrice1)

print()

print("Product 2nd : ",product1)
print(product2, "Quantity : ",quantity2)
print("price of each unit of ",product2,"is : ",price2)
print("Total price of ",product2,"is : ",totalPrice2)

print()

print("Product 2nd : ",product3)
print(product3, "Quantity : ",quantity3)
print("price of each unit of ",product3,"is : ",price3)
print("Total price of ",product3,"is : ",totalPrice3)

print()

print("Total Amount without GST : ",finalTotal)
print("GST : ",gst)
print("Your Final Amount is : ",finalAmount)

