#This program demonstrates the BankAccount class.

import BankAccountClass as bc

def main():
    
   # Get the starting balance.
   start_bal = float(input('Enter your starting balance: '))

   # Create a BankAccount object.
   savings = bc.BankAccount(start_bal) #this puts the user input as the starting balance

   # Deposit the user's paycheck.
   pay = float(input('How much were you paid this week? '))
   print('I will deposit that into your account.')
   savings.deposit(pay)

   # Display the balance.
   print('Your account balance is $', format(savings.get_balance(), ',.2f'),
        sep='')

   # Get the amount to withdraw.
   cash = float(input('How much would you like to withdraw? ')) #if you type a negative number here, it will actually add to your account
   print('I will withdraw that from your account.')
   savings.withdraw(cash)

   # Display the balance.
   print('Your account balance is $', 
        format(savings.get_balance(), ',.2f'), 
        sep='')

   print(savings)  #this will print out non-sense if the def_str_(self): was commented out

# Call the main function.
main()