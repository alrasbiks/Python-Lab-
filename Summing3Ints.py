'''
* The purpose of this program is to test the knowlagment about input in python
*
* Author : Khalid Al Rasbi
* last Edit Date : 02/17/2021
'''
# in this part is creating the input
x1= input("Enter the first 4-digit number:")
x2= input("Enter the second 4-digit number:")
x3= input("Enter the third 4-digit number:")
print " ", x1
print " ", x2
print "+", x3
print " ", ("----")
# here making the sum function for the input that user did
sum = x1+x2+x3
print sum
# here making the average function for the input that user did
Ave = sum/3.0

print "\nThe average is:", Ave
print "Program Terminating."