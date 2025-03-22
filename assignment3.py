students: dict = {}


# function to add student in a dictionary
def add_student():
    studName = input("Please enter student's name\t").capitalize()
    studAge = int(input("Please enter student's age\t"))
    studMarks = int(input("Please enter student's marks under under 100\t"))
    students[studName] = {"name": studName, "age": studAge, "marks": studMarks}
    return "Student added successfully ✅"


# function to show all registered students
def showStudents():
    if len(students) < 1:
        print("No students found!")
    else:
        for stud in students.values():
            name, age, marks = stud.values()
            print(f"Name: {name}, Age: {age}, Marks: {marks}")


# update marks of the registered student
def updateMarks():
    inputStudName: str = input(
        "Write the name of the student of which you want to update marks"
    ).capitalize()
    if inputStudName in students:
        updatedMarks = float(input("Please write updated marks of the student"))
        oldRecord = students[inputStudName]
        students[inputStudName] = {**oldRecord, "marks": updatedMarks}
        print(f"{inputStudName}'s Marks updated successfully✅")
        print(students)
    else:
        print("Student not found")


# show failed studnts
def failedStudents():
    if len(students) < 1:
        print("No students found!")
    else:
        for stud in students.values():
            name = stud.get("name")
            marks = stud.get("marks")
            if marks < 40:
                print(f"Name: {name}, Marks: {marks}")


# start program
def studRecordHandling():
    while True:
        print(
            """\nWhat do you want to do?
        1. Add student
        2. Show Students
        3. Update Marks
        4. Show Failed Students
        5. Exit
            """
        )
        optionNum: int = int(input("Please select option number: "))
        if optionNum == 5:
            break
        elif optionNum == 1:
            print(add_student())
        elif optionNum == 2:
            showStudents()
        elif optionNum == 3:
            updateMarks()
        elif optionNum == 4:
            failedStudents()
        elif optionNum == 5:
            break
        else:
            print("Invalid choice. Try Again")


studRecordHandling()
