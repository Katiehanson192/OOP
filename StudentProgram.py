
import StudentClass as s


def main():
    
    IdNumber = float(input('Enter student ID '))
    FLName = str(input('Enter first and last name '))
    birthDate = str(input('Enter DOB. Please format it mm dd yyyy '))
    gradeClass = str(input('Enter Classification. Freshman, Sophomore, Junior, Senior. '))

    info = s.StudentClass(IdNumber,FLName,birthDate,gradeClass)

    #Display age of student
    #info.set_age(birthDate)  #need to call the set function in order to have the age printed 
    print("Student's current age: ")
    info.set_age(birthDate)
   #Display when they can register
    info.set_grade(gradeClass)
    

main()