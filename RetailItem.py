#Once you have written the class, write a program that creates three RetailItem objects and stores the following data 


import RetailItemClass as ri

def main():
   
    

    for i in range(3):
        
        itemNum = str(input('Enter the item number. '))
        descript = str(input('Enter item description. '))
        Inventory = str(input('Enter inventory amount. '))
        cost = str(input('Enter item price. '))

        retail = ri.RetailItemClass(descript, Inventory, cost)


    
        
        #lists +=([itemNum,retail.get_descrip(), retail.get_unit(), retail.get_money()+'\n'])
        
        #print(lists)
        print('Item #'+'\t','Desc.'+'\t','Units'+'\t','Cost'+'\t')
        print(itemNum,'\t',retail.get_descrip(), retail.get_unit(),'\t', retail.get_money())
        
    
    #print(lists)

main()

