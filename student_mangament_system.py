student_details = {}
def add_student_details():
    name = input("Enter student name:")
    roll_number = int(input("Enter student rollno:"))
    marks1 = int(input('Enter math marks:'))
    marks2 = int(input('Enter english marks:'))
    
    student = {
        'Name':name,
        'Roll Number':roll_number,
        'Math':marks1,
        'English':marks2
    }
    students.append(student)
    print('Student details added ')
def display_student_details():
    print()
    for student in students:
        print('Name',student['Name'])
        print('Roll Number',student['Roll Number'])
        print('Math',student['Math'])
        print('English',student['English'])
        print()
def search_student_details():
    roll_number = int(input('Enter Roll Number to search student details:'))
    for student in students:
        if student['Roll Number'] == roll_number:
                    print('Name',student['Name'])
                    print('Roll Number',student['Roll Number'])
                    print('Math',student['Math'])
                    print('English',student['English'])
                    break
        else:
            print("No record for this Roll Number")
def delete_student_details():
   roll_number = int(input('Enter Roll Number to search student details:'))
   for student in students:
    if student['Roll Number'] == roll_number:
        students.remove(student)
        print("Student record remove sucessfully")
        break
    else:
        print("No record for this Roll Number")
students=[]

print('1. for adding student details')
print('2. for display students details')
print('3. for search student details')
print('4. for delete student details')
print('q. for exit')
print()
while True:   
    choice = input('Enter your choice between (1-4) for quit press q:')
    if choice =='1':
        add_student_details()
    elif choice =='2':
        display_student_details()
    elif choice =='3':
        search_student_details()
    elif choice =='4':
        delete_student_details()
    elif choice == 'q':
        print("Thanks for using your application")
        break
    else:
        print('Enter a valid details')

        