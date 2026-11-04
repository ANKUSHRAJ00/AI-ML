# Positive Number Filter: Ek list mein positive aur negative numbers hain. 
# List comprehension se sirf positive numbers nikalo. 

numbers = [-10, 20, -30, 40, 50, -60]

# using list conprehension for filtering positive number
positive_number = [x for x in numbers if x > 0]

# printing positive number
print("positive numbers :",positive_number)