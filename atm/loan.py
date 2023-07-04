import sqlite3
loan_conn = sqlite3.connect('Loan.db')
cursor_loan = loan_conn.cursor()

# cursor_loan.execute('create table loan_users (loan_balance real,loan_names text)')
# cursor_loan.execute('insert into loan_users values(10000000.0,"")')
# loan_conn.commit() 
# print('done')
# cursor_loan.execute('select * from loan_users')
# # print('done')
# loaners = cursor_loan.fetchall()
# print(loaners)
