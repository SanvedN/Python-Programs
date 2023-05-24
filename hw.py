def input_details() :
    n = int(input("Enter number of students : "))
    list_of_all_students = []
    for i in range(n) :
        d = {}
        print("Enter details for student number ",i+1,"  ")
        d['name'] = input("Enter name : ")
        d['roll number'] = int(input("Enter roll no : "))
        list_of_all_students.append(d)
    return list_of_all_students
def edit_details(list_of_all_students) :
    parameter = input('''Enter which parameter you want to edit :
    Enter N or n for name 
    Enter R or r for roll number : ''')
    if parameter[0].upper() == 'N' :
        n = input("Enter the name which you want to edit : ")
        for i in range(0,len(list_of_all_students)) :
            if list_of_all_students[i]['name'] == n :
                change = input("Enter the value to replace : ")
                list_of_all_students[i]['name'] = change
                print("Name Replaced Successfully !")
                return list_of_all_students
        print("Name not found")
    elif parameter[0].upper() == 'R' :
        n = int(input("Enter the roll number which you want to edit : "))
        for i in range(0,len(list_of_all_students)) :
            if list_of_all_students[i]['roll number'] == n :
                change = input("Enter the value to replace : ")
                list_of_all_students[i]['roll number'] = change
                print("Roll number Replaced Successfully !")
                return list_of_all_students    
        print("Roll number not found")
    else :
        print("Invalid Parameter")

if __name__ == "__main__" : 
    list_of_all_students = input_details()
    while True :
        command = int(input('''Enter the number according to the command to be performed : 
        1 - Edit details 
        2 - Display Details
        3 - Exit : '''))
        if command == 1 :
            edit_details(list_of_all_students)
        elif command == 2 :
            print(list_of_all_students)
        elif command == 3 :
            break
        else : 
            print("Invalid Command Specified Try Again")