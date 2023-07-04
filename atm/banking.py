import sqlite3
from loan import loan_conn,cursor_loan
from datetime import  datetime
from check import total
conn = sqlite3.connect("banking.db")
cursor = conn.cursor()
import random
from random import randint

# cursor.execute("create table account_users(id integer primary key,first_name text ,last_name text,age integer,dob  integer, sex text,account_number text,pin text ,bank text,balance real, date text,login bool, onLoan bool)")
# print('done')
# cursor_loan.execute('select * from loan_users')
# loan_conn.commit()
# loaner = cursor_loan.fetchone()
# print(loaner)

# print(datetime.day())
# cursor.execute('select id from account_users')
# user= cursor.fetchall()
# print(user)


cursor.execute('select * from account_users')
user = cursor.fetchall()
if user == []:
    pass
else:
    print(user)
class Banking:
    def __init__(self,ac_b= 0.0,):
        a  = random.randint(1,100)
        b  =randint(1,100)
        self.box = []
        c = a + b
        self.id = c + total
        self.balances = ac_b
        cursor_loan.execute(f'select * from loan_users')
        self.lo_bal = cursor_loan.fetchone()
        self.loan_bal = self.lo_bal[0]
        self.choice =  ['yes','Yes','Y','y']
        print('Please insert your pin')
        pin = input("pin: ")
        cursor.execute(f"select * from account_users where pin = {pin}")
        user = cursor.fetchone()
        print(user)
        self.bal = 0
        if user is not None:
            print(f'Welcome back {user[1]} {user[2]}')
            ba =  user[9]
            self.bal = self.bal + ba
            self.options()
        else:
            self.user_not_found()
            print('an error occured')
            self.__init__()


        self.balance = self.balances
    def user_not_found(self):
        print('user not found')
        self.select = input("do you want to wish to create account(Y/N)? ")
        if self.select in self.choice:
             self.create_account()
        else:
            print('We will miss you😥 our yet registered customer')

    def options(self):
        self.option = int(input(f'1:deposit money\n2:transfer\n3:check balance\n4:withdraw money\n5:get loan\n6:close your account\nchoose:\t'))
        if self.option == 1:
            self.deposit()
        elif self.option == 2:
            self.transfer()
        elif self.option == 3:
            self.check_balance()
        elif self.option == 4:
            self.withdraw()
        elif self.option == 5:
            self.getLoan()
        elif self.option == 6:
            self.close_account()

    def create_account(self):
        self.tday = ''
        d = datetime.now()
        dates = d.date()
        min = d.minute
        hr = d.hour
        sec = d.second
        time = f'{hr}:{min}:{sec}'
        time_obj = datetime.strptime(time, '%H:%M:%S')
        self.PM_AM = time_obj.strftime('%I:%M:%S %p')
        self.date_time = f'{dates} {self.PM_AM}'
        self.weekdays = {'6':'Sunday','0':'Monday','1':'Tuesday','2':'Wednesday','3':'Thursday','4':'Friday','5':'Saturday'}
        banks = {1:'Uba bank',2:'Eco bank',3:'Sterling bank',4:'First bank',5:'Access bank',6:'Fidelity bank',7:'Union bank',8:'Zenith bank'}
        bank_list = ['','Uba bank','Eco bank','Sterling bank','First bank','Access bank','Fidelity bank','Union bank','Zenith bank']
        self.id = self.id
        self.fname = input("your first name: ")
        self.lname = input("your lname: ")
        self.age = int(input("your age: "))
        self.dob = int(input("your date of birth year e.g(2000): "))
        self.sex = input("your sex: ")
        self.acc_num = input("create account number (10 in length): ")
        self.pin = input("create pin (4 in length): ")
        is_loggedIn = False
        is_loaned = False
        bank = int(input("choose bank\n1:Uba\n2:Eco bank\n3:Sterling bank\n4:First bank\n5:Access bank\n6:Fidelity bnak\n7:Union bank\n8:Zenith bank\nEnter Value: "))
        for key,self.value in self.weekdays.items():
            if int(key) == datetime.now().weekday():
                self.tuday = self.tday + f"{self.value} {self.date_time}"
                self.box.append(self.tuday)
        if bank_list[bank] == banks[bank]:
            print(banks[bank])
            cursor.execute(f"insert into account_users values({self.id}, '{self.fname}', '{self.lname}',{self.age},{self.dob},'{self.sex}','{self.acc_num}', '{self.pin}','{banks[bank]}', {self.balances}, '{self.tuday}',{is_loggedIn},{is_loaned})")
            conn.commit()
            print('account created successfully on', self.tuday)
            self.__init__()
        else:
            print('there is an error in your bank input')        
            self.create_account()
    
    def another_transac(self,pin):
        question = input('do you want to make another transaction (Y/N)? ')
        yes_choice = ['yes','YES','Yes','Y','y']
        cursor.execute(f'select * from account_users where pin = {pin}')
        user = cursor.fetchone()
        if question in yes_choice:
            self.__init__(self.bal)
        else:
            print(f'Thank you for banking with us\nwe hope to see you next time {user[1]}')

    def transfer(self):
        pin = input('enter your pin: ')
        banks = {1:'Uba bank',2:'Eco bank',3:'Sterling bank',4:'First bank',5:'Access bank',6:'Fidelity bank',7:'Union bank',8:'Zenith bank'}
        bank_list = ['','Uba bank','Eco bank','Sterling bank','First bank','Access bank','Fidelity bank','Union bank','Zenith bank']
        cursor.execute(f'select * from account_users where pin ={pin}')
        user = cursor.fetchone()
        if user is not None:
            user_ba = user[9]
            b_acc_num = input('enter beneficial account number: ')
            bene_bank = int(input("beneficial bank\n1:Uba bank\n2:Eco bank\n3:Sterling bank\n4:First bank\n5:Access bank\n6:Fidelity bank\n7:Union bank\n8:Zenith bank\nEnter Value: "))
            cursor.execute(f'select * from account_users where account_number = {b_acc_num}')
            bene = cursor.fetchone()
            try:
                if bene is not None and bene[6] == b_acc_num and bene[8] == bank_list[bene_bank] and bene[6] != user[6]:
                    print(banks[bene_bank])
                    amount = int(input('enter amount: '))
                    cursor.execute(f'select * from account_users where pin = {pin}')
                    use = cursor.fetchone()
                    if use[9] < amount:
                        print('insufficient balance')
                        self.another_transac(pin)
                    else:
                        bene_bal = bene[9] + amount
                        cursor.execute(f'update account_users set balance = {bene_bal} where account_number = {b_acc_num}')
                        conn.commit()
                        print('transfer successfull')
                        print(f'you transfered {amount} to {banks[bene_bank]} customer\nname: {bene[1]} {bene[2]} ')
                        user_cu_ba = user_ba - amount
                        cursor.execute(f'update account_users set balance = {user_cu_ba} where pin = {pin}')
                        conn.commit()
                        cursor.execute(f'select * from account_users  where pin = {pin}')
                        owner = cursor.fetchone()
                        if owner is not None and owner[7] == pin:
                            print(f'your account has been debited with {amount}\nyour account balance is {user_cu_ba}')
                            self.another_transac(pin)
                        else:
                            print('no user with such pin found')
                            self.transfer()
                elif bene[6] == user[6]:
                    print(f"You can't tranfer money to yourself {user[1]}")
                    self.another_transac(pin)
                else:
                    print('beneficial not found')
                    self.transfer()
            except:
                print(f'such user with the account number {b_acc_num} doesn\'t exist')
                self.another_transac(pin)
    
    def check_balance(self):
        print('please input your pin')
        pin = input("enter your pin: ")
        cursor.execute(f'select * from account_users where pin = {pin}')
        user = cursor.fetchone()
        if user is not None and user[7] == pin:
            print(f'{user[1]} {user[2]} your account balance is {user[9]}')
            self.another_transac(pin)
        else:
            print('incorrect pin')
            self.check_balance()
            

    def deposit(self):
        pin = input("enter your pin: ")
        self.amount = float(input("enter amount: "))
        self.main_bal = self.bal + self.amount
        cursor.execute('update account_users set balance =? where pin = ?',(self.main_bal,pin))
        conn.commit()
        cursor.execute(f'select * from account_users where pin = {pin}')
        user = cursor.fetchone()
        if user is not None:
           print(f'{user[1]} your account has been credited with {self.amount}')
           self.another_transac(pin)
        else:
            print('user not found')

    def withdraw(self):
        self.pin = input("enter your pin: ")
        self.amount = float(input("enter amount: "))
        self.dp_name = input("enter your name: ")
        self.main_bal = self.bal - self.amount
        cursor.execute('select * from account_users')
        user = cursor.fetchone()
        if user is not None and user[7] == self.pin:
            if self.amount > self.bal:
                print('insufficient balance')
                print('hey we are sorry for you brokeness😥 go and hustle')
                self.another_transac(self.pin)
            else:
                cursor.execute('update account_users set balance =? where pin = ?',(self.main_bal,self.pin))
                conn.commit()
                print(f'{user[1]} your account has been debited with {self.amount}')
                print(f'your account balance is {self.main_bal}')
                self.another_transac(self.pin)
        else:
            self.user_not_found()

    def getLoan(self):
        pins = input("enter your pin: ")
        cursor.execute(f"select * from account_users where pin = {pins}")
        is_loaned = cursor.fetchone()
        user_b = is_loaned[9]
        if is_loaned is not None and is_loaned[12] == False:
                print('you are eligible for loan')
                self.amount_ = float(input("enter amount you wish to collect for loan: "))
                self.dp_name = input("enter your full bank name: ")
                self.acc_nums = input("enter your account number: ")
                self.bank = input('your bank name e.g(Zenith bank): ')
                # cursor.execute(f'select * from account_users where account_number = {self.acc_nums} ')
                # user = cursor.fetchone()
                print(is_loaned[9])
                try:
                    if is_loaned[6] == self.acc_nums and is_loaned[8] == self.bank:
                        loan_bal_left = self.loan_bal - self.amount_
                        cursor_loan.execute(f'update loan_users set loan_balance = {loan_bal_left}')
                        loan_conn.commit()
                        user_lo_bal = user_b + self.amount_
                        cursor.execute(f'update account_users set  balance ={user_lo_bal}, onLoan = {True} where pin = {pins}')
                        conn.commit()
                        cursor.execute(f'select * from account_users where pin = {pins}')
                        cur_user = cursor.fetchone()
                        cur_user_ba = cur_user[9]
                        print(f'{cur_user[1]} {cur_user[2]} your loan was successfull\nyour account balance is {cur_user_ba}')
                        self.another_transac(pins)
                    else:
                        print('such user does not exist')
                        self.another_transac(pins) 
                except:
                    print('error occured up there')
        else:
             print('you have not paid your last debt\nplease pay to collect another loan')
             self.another_transac(pins)   

    def close_account(self):
        pin = input('Ender your pin: ')
        f_name = input('Enter your full name:')
        acc_no = input('Enter your account number: ')
        self.yes_choice = ['yes','YES','Yes','Y','y']
        cursor.execute(f'select * from account_users')
        users = cursor.fetchone()
        if users is not None and users[7] == pin and users[6] == acc_no:
            are_you_sure = input(f'are you sure you want to delete your account {users[1]} (y/n)? ')
            if are_you_sure in self.yes_choice:
                cursor.execute(f'delete from account_users where pin = {pin}')
                conn.commit()
                print(f'account deleted successfully')
                self.another_transac(pin)
            else:
                print(f'Thank you for not closing your account\nwith us, we ♥ you {f_name}')
                self.another_transac(pin)
        else:
            self.user_not_found()


Banking()

cursor.close()