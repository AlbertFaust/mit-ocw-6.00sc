'''
Problem Set 0

Write a program that does the following in order: 
Asks the user to enter his/her date of birth. 
Asks the user to enter his/her last name. 
Prints out the user’s last name and date of birth, in that order. 
'''
#!/usr/bin/env python2.7

dateOfBirth = (raw_input('What is your date of birth? '))
lastName = (raw_input('What is your last name? '))

print (lastName + ' ' + dateOfBirth)
