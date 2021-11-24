'''
* The purpose of this program is to test the knowlagment about if and else if statement and creating methods in python
*
* Author : Khalid Al Rasbi
* last Edit Date : 03/12/2021
'''

#here in this part the program will ask to create 5 diffrent methods
def Addition():
    # here to ask the user to enter his own numbers
    first_integer = int (input("Enter first integer: "))
    second_integer = int (input("Enter second integer: "))

    result = first_integer + second_integer
    print(first_integer, "add", second_integer, " is ", result)
def Subtraction():
    # here to ask the user to enter his own numbers
    first_integer = int (input("Enter first integer: "))
    second_integer = int (input("Enter second integer: "))

    result = first_integer - second_integer
    print(first_integer, "minus", second_integer, " is ", result)
def Multiplication():
    # here to ask the user to enter his own numbers
    first_integer = int (input("Enter first integer: "))
    second_integer = int (input("Enter second integer: "))

    result = first_integer * second_integer
    print(first_integer, "times", second_integer, " is ", result)
def Division():
    # here to ask the user to enter his own numbers
    first_integer = int (input("Enter first integer: "))
    second_integer = int (input("Enter second integer: "))

    result = first_integer / second_integer
    print(first_integer, "divided", second_integer, " is ", result)
def Modulus():
    # here to ask the user to enter his own numbers
    first_integer = int (input("Enter first integer: "))
    second_integer = int (input("Enter second integer: "))

    result = first_integer % second_integer
    print(first_integer, "mod", second_integer, " is ", result)
# to close all methods
flag = True

# this is the welcoming part of the program to start
while (flag == True) :
    menu = input ("Menu: \n"
              "     ""A: Addition\n" 
             "     ""S: Subtraction\n" 
             "     ""M: Multiplication \n"
             "     ""D: Division \n"
             "     ""R: Modulus \n"
             "     ""E: To Exit Program\n")

    # here is after what the user would enter
    #here to ask the user to enter his own numbers

    # if the user enter A or a it will add the numbers
    if menu == "A".lower():
        Addition()

    # if the user enter S or sit will sub the numbers
    elif menu == "S" .lower():
        Subtraction()

    elif menu == "M".lower():
        Multiplication()

    # if the user enter D or d it will divide the numbers
    elif menu == "D".lower():
        Division()

    # if the user enter R or r it will mod the numbers
    elif menu == "R".lower():
        Modulus()
# to close the if else statement
    else:
        print("Ending program!!!!:)")
        flag = False

