import random

class Insect:
    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.flight = 0  #need to first initialize it to start at 0

    def flight(self):
        random.randint(1, 10)

    def get_flight(self):
        return self.flight #need a second method to return the value of the flight
