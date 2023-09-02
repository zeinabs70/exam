from os import system
clear = lambda : system("cls")
from pickle import load
try:
    with open("active_students" , "rb") as std_info:
        students = load(std_info)
except:
    students = []
try:
    with open("graduated_students" , "rb") as g_std_info:
        graduated_students = load(g_std_info)
except:
    graduated_students = []

def check_codemeli(codemeli):
    for student in students:
        if student["code_melli"] == codemeli:
            return False
    for student in graduated_students:
        if student["code_melli"] == codemeli:
            return False
        else:
            return True
        

def check_stdcode(stdcode):
    for student in students:
        if student["student_code"] == stdcode:
            return False
    for student in graduated_students:
        if student["student_code"] == stdcode:
            return False
        else:
            return True

def calculateAge(birthDate):
    from datetime import date
    import jdatetime
    today = date.today()
    shamsi_today = jdatetime.date.fromgregorian(day=today.day , month=today.month , year=today.year )
    age = shamsi_today.year - birthDate.year
    return age

def avg(*list_num):
    print(list_num)
    avg = round(sum(list_num) / len(list_num) , 2)
    return avg

def add_student():
    clear()
    from datetime import datetime
    global students
    student = dict()
    student["first_name"] = input("enter first name of student :")
    student["last_name"] = input("enter last name  :")
    try:
        student["birthday"] = datetime.strptime(input("enter birthday (xxxx/yy/zz) :"),f'%Y/%m/%d')
    except(ValueError):
        input("The entered value does not follow the format(xxxx/yy/zz), press any key to return to menu...")
        return True
    try:
        student["code_melli"] = int(input("enter code melli (10 digits) :"))
        if check_codemeli(student["code_melli"]) == False:
            input("A student with this code meli has been registered")
            return True
    except(ValueError):
        input(" code melli must be A 10-digit number , press any key to return to menu...")
        return True
    try:
        student["student_code"] = int(input("enter student code (5 digits) :")) 
        if check_stdcode(student["student_code"]) == False:
            input("A student with this student code has been registered")
            return True
    except(ValueError):
        input("student code must be A 5-digit number , press any key to return to menu...")
        return True
    # student["courses"] = input("enter courses :").split(" ")
    # student["grades"] = input("enter grades :").split(" ")
    student["courses"]= []
    student["grades"]= []
    addmore = "YES"
    for i in range(50):
        if addmore == "YES":
            student["courses"].append(input("enter course : "))
            student["grades"].append(int(input("enter grade : ")))
            addmore = input("Do you want to add a course again?(yes/no)").upper()
            i+=i
        else: 
            break
    students.append(student)
    input("add student has been successful ... ")
    pass

def change_info():
    clear()

    pass

def search_student():
    clear()
    std_number = int(input("please enter student number to find The desired student(5 digits): "))
    for student in students:
        if student['student_code'] == std_number:
            print("------------------------------------------------")
            print(f"first name :     {student['first_name']}")
            print(f"last name :      {student['last_name']}")
            print(f"cobe meli :      {student['code_melli']}")
            print(f"student nember : {student['student_code']}")
            print(f"age:             {calculateAge(student['birthday'])}")
            print(f"maximum grades:  {max(student['grades'])}")
            print(f"minimum grades:  {min(student['grades'])}")
            print(f"average :        {avg(*student['grades'])}")
            print("------------------------------------------------")
            input("press any key ....")
    

def list_student():
    clear()        
    print("")
    print("********************************************************active student**********************************************")
    count = 1
    for student in students:
        print(f"{count}  {student['first_name']}    {student['last_name']:10}    {student['birthday']}      {student['student_code']:10}    ")
        count += 1
    input("*******************************************************graduated student********************************************")
    for g_std in graduated_students:
        print(f"{count}  {g_std['first_name']}    {g_std['last_name']:10}    {g_std['birthday']}      {g_std['student_code']:10}    ")
        count += 1

def delete_student():
    clear()
    from pickle import dump
    std_number = int(input("please enter student number to delete The desired student(5 digits): "))
    for student in students:
        if student['student_code'] == std_number:
            y_n = input("Are you sure you want to delete this student from the list of active students?(yes/no)").upper()
            if y_n == 'YES':
                graduated_students.append(student)
                students.remove(student)
                input("The student has been deleted successfully ")
            else:
                input("The operation to delete the student was canceled")

def save_info():
    clear()
    from pickle import dump
    y_n = input("Do you want the changes to be saved?(yes/no)").upper()
    if y_n == 'YES':
        with open("active_students","wb") as std_info:
            dump(students,std_info)
        with open("graduated_students" , "wb") as g_std:
            dump(graduated_students , g_std)
        input("The changes have been successfully saved ")    
     

