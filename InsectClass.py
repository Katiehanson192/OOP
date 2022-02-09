import random

class Insect:
    def __init__(self, w,l): #if don't assign w and l to a value, need to include it in the ()
        self.wings = w
        self.legs = l
        self.flight = 0  #need to first initialize it to start at 0

    def length_flight(self):
        self.flight = random.randint(1, 10)

    def get_flight(self):
        return self.flight #need a second method to return the value of the flight