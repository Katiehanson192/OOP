import random

#class creation object

# The Coin class simulates a coin that can
# be flipped.

class Coin:
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.

    def __init__(self):  #first method of EVERY CLASS CREATION FILE (means all our coins are starting heads up)
        self.__sideup = 'Heads'  #one attribute for this class. sideup = instance that's calling the class

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def toss(self):
        if random.randint(0, 1) == 0:  #value of sideup can only be changed when the toss method is used 
            self.__sideup = 'Heads' # 2 underscores = hides data
        else:
            self.__sideup = 'Tails' #need to apply it to EVERYWHERE the attribute is used 

    # The get_sideup method returns the value
    # referenced by sideup.

    def get_sideup(self):
            return self.__sideup
