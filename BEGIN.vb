BEGIN
     DECLARE students AS DICTIONARY
studens = {}

     FUNCTION add_student()
         PRINT "Enter student name: "
         INPUT name
         PRINT "Enter student age: "
         INPUT age
         PRINT "Enter student marks: "
         INPUT marks
         SET students[name] TO {"age": age, "marks": marks}
         PRINT name + " added successfully!"

def add_student():
    name = input("Enter student name:")
    age = int(input("Enter student name:"))
    marks = float(input("Enter student name:"))
    studens["name"] = {"age": age, "marks": marks}
    print(name + " added successfully!")
    FUNCTION show_students()
        IF students IS EMPTY THEN
            PRINT "No students found!"
            RETURN
        PRINT "Student Records:"
        FOR EACH name, data IN students
            PRINT "Name: " + name + ", Age: " + data["age"] + ", Marks: " + data["marks"]
    
    FUNCTION update_marks()
        PRINT "Enter student name to update marks: "
        INPUT name
        IF name EXISTS IN students THEN
            PRINT "Enter new marks: "
            INPUT new_marks
            SET students[name]["marks"] TO new_marks
            PRINT name + "'s marks updated!"
        ELSE
            PRINT "Student not found!"

    FUNCTION show_failed_students()
        PRINT "Students Who Failed:"
        FOR EACH name, data IN students
            IF data["marks"] < 40 THEN
                PRINT name + ": " + data["marks"]

    WHILE TRUE
        PRINT "1. Add Student"
        PRINT "2. Show Students"
        PRINT "3. Update Marks"
        PRINT "4. Show Failed Students"
        PRINT "5. Exit"
        
        PRINT "Choose an option: "
        INPUT choice

        IF choice == "1" THEN
            CALL add_student()
        ELSE IF choice == "2" THEN
            CALL show_students()
        ELSE IF choice == "3" THEN
            CALL update_marks()
        ELSE IF choice == "4" THEN
            CALL show_failed_students()
        ELSE IF choice == "5" THEN
            PRINT "Exiting..."
            BREAK
        ELSE
            PRINT "Invalid choice! Try again."

END