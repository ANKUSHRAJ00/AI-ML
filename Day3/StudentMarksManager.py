# Student Marks Manager: 5 students ke marks list mein store karo. 
# Highest, lowest aur average marks find karo. 


marks = []

for i in range(5) :
  inputMark = int(input("Enter marks : "))
  marks.append(inputMark)

print("Marks you have Entered : ",marks)

# Highest marks
highest_marks = max(marks)
print("Highest Marks : ",highest_marks)

# Lowest marks
lowest_marks = min(marks)
print("Lowest marks : ",lowest_marks)

# Avarage Marks

total_marks = sum(marks)
print("Avarage Marks : ",total_marks/len(marks))