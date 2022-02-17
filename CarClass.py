

class CarClass:
    def __init__(self, mod, make):
        self.__year_model = str(mod)
        self.__make = str(make)
        self.__speed = 0

    def get_model(self):
        return self.__year_model
    
    def get_make(self):
        return self.__make


    #speed
    def accelerate(self):
        self.__speed += 5

    def brake (self):
        self.__speed -=5


    def get_speed(self):
        return self.__speed
    
    
    

    
