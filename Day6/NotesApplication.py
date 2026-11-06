# Notes Application: User se note input lo aur text file mein save karo. 
# Ek option do jisse saved notes read kar sake. 

input_note = input("Enter text : ")

with open("notes.txt", "w") as file:
    file.write(input_note)

with open("notes.txt","r") as file :
    content = file.read()
    print(content)