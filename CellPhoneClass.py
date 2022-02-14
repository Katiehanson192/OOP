class CellPhone:
    
        def __init__(self, mfg, mod, cost):
            self.__manufact = mfg
            self.__model = mod
            self.__retail_price = cost

        def set_manufact(self, mfg): # need to always include the "self" arguement when seting a function/attribute
            self.__manufact= str(mfg)


        def get_manufact(self): 
            return self.__manufact




        def set_model (self, mod):
            self.__model = str(mod)


        def get_model (self):
            return self.__model




        def set_retail_price(self, cost):
            self.__retail_price = cost

        def get_retail_price(self):
            return self.__retail_price
        