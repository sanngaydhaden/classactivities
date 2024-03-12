#Excercise
print("Class Excercise")

#Initializing empty lists and dictionary
students_list = []
students_dict = {}

#Asking the user to input their name,age and grade
name = str(input("enter your name: "))
age = int(input("enter your age: "))
grade = int(input("enter your grade: "))

print("student information added successfully!")

# Adding student information to lists and dictionary
students_list.append("dhaden")
students_dict["dhaden"] = {'age': age, 'grade': grade}

print("Student details: ")
for name, info in students_dict.items():
    print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")
    
# Searching for student's name
name = input("Enter student name to search: ")
if name in students_dict:
    print(f"student found!: {students_dict[name]}")

# Removing the student's name
remove_name = input("Enter student name to removed: ") 
if remove_name in students_dict:
    remove_name=students_dict[remove_name]
    students_dict.remove(remove_name)
    del students_dict[remove_name]
    print("name removed successfully!")
    