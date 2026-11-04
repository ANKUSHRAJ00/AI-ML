# Squares Generator: List comprehension ka use karke 1 se 20 tak ke numbers ke squares ki list banao. 


number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# using list comprehension to find out square
square_number = [x * x for x in number]

# printing square
print("Squares :",square_number)