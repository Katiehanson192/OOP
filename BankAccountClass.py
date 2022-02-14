# The BankAccount class simulates a bank account.

class BankAccount:
    

# The __init__ method accepts an argument for
# the account's balance. It is assigned to
# the __balance attribute.

    def __init__(self, bal):
        self.__balance = bal #get bal from user?

      # The deposit method makes a deposit into the
      # account.

    def deposit(self, amount): #amount needs to be specified by user before any of the methods can be called (other than main)
        self.__balance += amount

      # The withdraw method withdraws an amount
      # from the account.

    def withdraw(self, amount): #set method (changing the value)
        if amount <= 0:
          print("can't withdraw a negative number")
        else:
          if self.__balance >= amount:
            self.__balance -= amount
          else:
            print('Error: Insufficient funds')

      # The get_balance method returns the
      # account balance.

    def get_balance(self): #accessor methods (get method)
        return self.__balance

  

    def __str__(self):
        return 'The balance is $' + format(self.__balance, ',.2f')
  