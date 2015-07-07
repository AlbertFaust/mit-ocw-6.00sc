'''
Problem Set 1 : Problem 2
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. 
We will not be dealing with a minimum monthly payment rate. 
Take as raw_input() the following floating point numbers: 
      1.the outstanding balance on the credit card 
      2.annual interest rate as a decimal 
Print out the fixed minimum monthly payment, number of months (at most 12 and possibly less than 12) it takes to pay off the debt, and the balance (likely to be a negative number). 
Assume that the interest is compounded monthly according to the balance at the start of the month (before the payment for that month is made). 
The monthly payment must be a multiple of $10 and is the same for all months. 
Notice that it is possible for the balance to become negative using this payment scheme.
'''
#!/usr/bin/env python2.7
def printVals():
    print 'RESULT'
    print 'Monthly Payment to Pay Off Debt in 1 Year: $', minimumMonthlyPayment
   # print 'Number of Months Needed: ', numberOfMonths
    print 'Balance: $', balance
    return

def minMonth(balance, monthlyInterestRate, minimumMonthlyPayment, new):
    numberOfMonths = 0
    while balance > 0 and numberOfMonths < 12:
        minimumMonthlyPayment = minimumMonthlyPayment + 10
        new = new * (1 + monthlyInterestRate) - minimumMonthlyPayment
        numberOfMonths = numberOfMonths + 1
        print new

balance = float(input('Please enter the outstanding balance on your credit card: '))
annualInterestRate = float(input('Please enter the Annual Interest Rate as a decimal: '))
monthlyInterestRate = annualInterestRate / 12.0
minimumMonthlyPayment = 0
new = balance

while(balance > 0):
    minMonth(balance, monthlyInterestRate, minimumMonthlyPayment,new)
    if(new > 0):
        minimumMonthlyPayment = minimumMonthlyPayment + 10
        minMonth(balance,monthlyInterestRate, minimumMonthlyPayment,new)
        balance = new
    print balance
printVals()
