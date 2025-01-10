# class Student:
#     name = 'Lakshay'
    
# s1 = Student()
# print(s1)


class Atm: 
    
    def __init__(self):
        self.pin = ''
        self.balance = 0
        
        self.menu()
        
    def menu(self):  
        user_input = input("""  
    Hello, how would you like to proceed?  
    1. Enter 1 to create pin  
    2. Enter 2 to deposit  
    3. Enter 3 to withdraw  
    4. Enter 4 to check balance  
    5. Enter 5 to exit  
    """)  

        if user_input == "1":  
            self.create_pin() 
        elif user_input == "2":  
            self.deposit_cash()  
        elif user_input == "3":  
            self.withdraw_cash()  
        elif user_input == "4":  
            self.check_balance()  
        else:  
            print('bye')
            
    def create_pin(self):
        self.pin = int(input('Enter your pin:'))
        print('Pin set successfully')
    
    def deposit_cash(self):
        temp = input('Enter your pin:')
        if temp == self.pin:
            deposit = int(input('Enter the amount you want to deposit: '))
            self.balance = self.balance + deposit
            print('Cash deposited successfully.')
        else:
            print('Invalid Pin')
            
        
    def withdraw_cash(self):
        temp = input('Enter your pin')
        if temp == self.pin:
            withdraw = input('Enter the amount you want to withdraw: ')
            if withdraw < self.balance:
                self.balance = self.balance - withdraw
                print('Cash withdrawn successfully.')
            else:
                print('Insufficient Balance')
        else:
            print('Invalid Pin')
        
    def check_balance(self):
        temp = input('Enter your pin')
        if temp == self.pin:
            print(self.balance)
        else:
            print('Invalid Pin')
            
