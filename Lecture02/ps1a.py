'''
Problem Set 1 : Problem 1
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month. 
Use raw_input() to ask for the following three floating point numbers: 
        1. the outstanding balance on the credit card 
        2. annual interest rate 
        3. minimum monthly payment rate 
For each month, print the minimum monthly payment,remaining balance, principle paid in the format shown in the test cases below. 
All numbers should be rounded to the nearest penny. 
Finally, print the result, which should include the total amount paid that year and the remaining balance. 
'''
#!/usr/bin/env python2.7
def printVals():
    if months != 11:
        print 'Month: ', months+1
        print 'Minimum Monthly Payment: $', minimumMonthlyPayment
        print 'Principle Paid: $', principlePaid
        print 'Remaining Balance: $', remainingBalance
    else:
        print 'Month: ', months+1
        print 'Minimum Monthly Payment: $', minimumMonthlyPayment
        print 'Principle Paid: $', principlePaid
        print 'Remaining Balance: $', remainingBalance
        print
        print 'RESULT'
        print 'Total Amount Paid: $', totalAmountPaid
        print 'Remaining Balance: $', balance

balance = float(input('Please enter the outstanding balance on your credit card: '))
annualInterestRate = float(input('Please enter the Annual Interest Rate as a decimal: '))
minimumPaymentRate = float(input('Please enter the Minimum Monthly Payment Rate as a decimal: '))

totalAmountPaid = 0
months = 12

for months in range(0, 12):
        minimumMonthlyPayment = round(minimumPaymentRate * balance, 2)
        interestPaid = round(annualInterestRate / 12 * balance, 2)
        principlePaid = round(minimumMonthlyPayment - interestPaid, 2)
        remainingBalance = round(balance - principlePaid, 2)
        balance = remainingBalance
        totalAmountPaid = totalAmountPaid + minimumMonthlyPayment
        printVals()
   
