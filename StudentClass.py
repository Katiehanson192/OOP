from datetime import date

class StudentClass:    
    def __init__(self, num, First_Last, birthday, clf):
        self.__Student_ID = num
        self.__Student_name = First_Last
        self.__Student_DOB = birthday
        self.__Student_classification = clf

    
    
    def set_age(self,age):
        year = self.__Student_DOB.split(' ')
        year = int(year[2])
        
        CurrentYear = date.today().year
        age = CurrentYear - year
        print(str(age))
        
    def get_age(self):
        return self.__Student_DOB
        return age
        

    
    def set_grade(self, clf):
        self.__Student_classification = str(clf)
        if self.__Student_classification == "Freshman":
            print("As a freshman, you can register for classes between 4/10 - 4/12")
        elif self.__Student_classification == "Sophomore":
            print("As a sophomore, you can register for classes between 4/7 - 4/9")
        elif self.__Student_classification =="Junior":
            print("As a junior, you can register for classes between 4/4 - 4/6")
        elif self.__Student_classification == "Senior":
            print("As a senior, you can register for classes between 4/1 - 4/3")
        


    def get_grade(self):
        return self.__Student_classification