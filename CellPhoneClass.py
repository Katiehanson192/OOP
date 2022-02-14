class CellPhone:
    
    def __init__(self, manu, mod, price):
        self.__manufact = manu
        self.__model = mod
        self.__retail_price = price

        def set_manufact(self, manu): # need to always include the "self" arguement when seting a function/attribute
            self.__manufact = manu


        def get_manufact(self): 
            return self.__manufact




        def set_model (self, mod):
            self.__model = mod


        def get_model (self):
            return self.__model




        def set__retail_price(self, price):
            self.__retail_price = price

        def get__retail_price(self):
            return self.__retail_price
        