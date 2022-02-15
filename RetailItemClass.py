#: item description, units in inventory, and price.

class RetailItemClass:
    def __init__(self, describe, inv, cost):
        self.__Item_Description = describe
        self.__Inventory_Units = inv
        self.__Price = cost

#create 3 objects and store description, unit, and price for each
#create a list for each object


    def get_descrip(self):
        return self.__Item_Description


    def get_unit(self):
        return self.__Inventory_Units

    def get_money(self):
        return self.__Price

#get input for each attribute + store in list

#ask for the next list
