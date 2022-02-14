class Student:
    def __init__(self, ID, name, DOB, clf):
        self.__Student_ID = ID
        self.__Student_name = name
        self.__Student_DOB = DOB
        self.__Student_classification = clf

    def set_age(self, DOB):
        year = self.__Student_DOB.split(2)
        CurrentYear = date.today.split(2)
        age = CurrentYear - year
        
    def get_age(self):
        return self.__Student_DOB

    def set_grade(self, clf):
        