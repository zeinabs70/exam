import student_operations as stdop


while True:
    stdop.clear()
    print("*******************************************")
    print("press a to add new student")
    print("press c to change courses of student")    
    print("press s to search student")   
    print("press l to show list of all student")
    print("press d to delete student")
    print("press q to quit application")
    print("*******************************************")
    select = input("please enter your selection : ").upper()
    if select == 'A':
        stdop.add_student()
    elif select == 'C':
        stdop.change_info()
    elif select == 'S':
        stdop.search_student()
    elif select == 'L':
        stdop.list_student()
    elif select == 'D':
        stdop.delete_student()
    elif select == 'Q':
        stdop.save_info()
        break
    else:
        input("wrong selection!!!")