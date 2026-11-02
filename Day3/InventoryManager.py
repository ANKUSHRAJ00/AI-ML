# Inventory Manager: Dictionary mein products aur unki quantities store karo.
# Product add, update, delete aur display karne ka program banao. 

store = {
  "Biscuits" : 20,
  "Chocolate" : 30,
  "Coke" : 50,
  "Lassi" : 35
}

# add a product
store["Icecream"] = 40
store["Lays"] = 15

# update a product
store.update(Biscuits = 10)
store.update(Coke = 38)

# Delete a product
store.pop("Lays")

# Display Products (normal way)
# print(store.items())

# better way to display products
for product,quantity in store.items() :
  print(product,":",quantity)