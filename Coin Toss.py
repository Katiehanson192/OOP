import CoinClass as c #need to import the coinclass file (ALWAYS IMPORT THE NAME OF THE FILE )


# The main function.
def main():
       # Create an object from the Coin class.
       my_coin = c.Coin()   # this creates an INSTANCE called 'my_coin' of the class 'Coin()'
                    #c = an alias 
       # Display the side of the coin that is facing up.
       print('This side is up:', my_coin.get_sideup())    # notice you do not have to supply the argument/parameter
                #this will always be heads b/c we initiated the class to always be heads firsts
       # Toss the coin.
       print('I am going to toss the coin ten times:')
       for count in range(10):
           my_coin.toss()
           
           # Display the side of the coin that is facing up.
           print('This side is up:', my_coin.get_sideup())

           


       

# Call the main function.

main()
