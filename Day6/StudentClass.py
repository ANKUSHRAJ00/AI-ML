# Student Class: Student class banao jisme name, roll number aur marks ho. 
# Ek method result calculate kare aur display kare.

class Student :

  # constructor
  def __init__(self, name, rollNumber, marks) :
    self.name = name
    self.rollNumber = rollNumber
    self.marks = marks

  # function to display student details
  def displayDetails(self) :
    print("Student Name : ",self.name)
    print("Student Roll Number : ",self.rollNumber)
    print("Student Marks : ",self.marks)

  # function to calculate grade

  def gradeCalculation(self) :
    if self.marks >= 90 :
      print("Grade : A")
    elif self.marks >= 80 :
      print("Grade : B")
    elif self.marks >= 70 :
      print("Grade : C")
    elif self.marks >= 60 :
      print("Grade : D")
    else :
      print("Grade : Fail")

  # object creation

Student1 = Student("Ankush", 24573, 80)
Student1.displayDetails()
Student1.gradeCalculation()
print()
Student2 = Student("Nirbhay", 24572, 90)
Student2.displayDetails()
Student2.gradeCalculation()
print()
Student3 = Student("Aditya", 24571, 85)
Student3.displayDetails()
Student3.gradeCalculation()