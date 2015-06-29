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

balance = float(input('Please enter the outstanding balance on the credit card: '))
annualInterestRate = float(input('Please enter the Annual Interest Rate: '))
minimumPaymentRate = float(input('Please enter the Minimum Monthly Payment Rate: '))
totalAmountPaid = 0

for x in range(0, 12):
        minimumMonthlyPayment = round(minimumPaymentRate * balance, 2)
        interestPaid = round(annualInterestRate / 12 * balance, 2)
        principlePaid = round(minimumMonthlyPayment - interestPaid, 2)
        remainingBalance = round(balance - principlePaid, 2)
        balance = remainingBalance
        totalAmountPaid = totalAmountPaid + minimumMonthlyPayment
        print 'Month:',x+1,'\nMinimum monthly payment: $',minimumMonthlyPayment, '\nPrinciple paid: $',principlePaid, '\nRemaining balance: $',remainingBalance

print 'RESULT\nTotal amount paid:$',totalAmountPaid, '\nRemainingBalance:$',balance
