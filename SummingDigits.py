'''
* The purpose of this program is to test the knowlagment about input number and being able to make function with it in python
*
* Author : Khalid Al Rasbi
* last Edit Date : 02/24/2021
'''
# this part is to make the start sentence for the user
number = input(" Enter a 4-digit number : ")
# this part is to make the 4-digit number separate by the last number
x1 = number//1000 %10
x2= number//100 %10
x3= number//10 %10
x4= number%10
# function to sum each digit from the 4-digit user did entered
x=x1+x2+x3+x4
# part to print last statement with numbers and sum each number togther
print (" The sum of digits of the number"), number," is" ,x1,"+", x2,"+",x3,"+",x4, "=", x
