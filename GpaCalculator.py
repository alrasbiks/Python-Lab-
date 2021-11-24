'''
* The purpose of this program is to test the calculator the GPA  using loop statement in python
*
* Author : Khalid Al Rasbi
* last Edit Date : 03/31/2021
'''

#this first methold to calculate the GPA
def calculateGPA (totalgrade, totalcredits):
    return totalgrade/totalcredits

#this is second methlod to print the result
def printresults(finalgba, result):
    print("Grade     Hours\n", result)
    print("Resulting in a GPA of " + str(finalgba))

# to know how many classes the user have
classnumbers= int (input(" How many classes are you taking? "))
x = 0
totalcredits =0
totalgrade = 0
table = ""

#here to make the while loops
while (x < classnumbers ):

    classgrade = input("Enter the grade : ")
    classhours = int (input("Enter the hours : "))
    if classgrade == 'A+' or classgrade == 'A' or classgrade == 'a+' or classgrade == 'a':
        points = 4.0
    elif classgrade == 'A-' or classgrade == 'a-':
        points = 3.7
    elif classgrade == 'B+' or classgrade == 'B+':
        points = 3.3
    elif classgrade == 'B' or classgrade == 'b':
        points = 3.0
    elif classgrade == 'B-' or classgrade =='b-':
        points = 2.7
    elif classgrade == 'C+' or classgrade == 'c+':
        points = 2.3
    elif classgrade == 'C' or classgrade == 'c':
        points = 2.0
    elif classgrade == 'C-' or classgrade == 'c-':
        points = 1.7
    elif classgrade == 'D+' or classgrade == 'd+':
        points = 1.3
    elif classgrade == 'D-' or classgrade == 'd-':
        points = 1.0
    elif classgrade == 'F' or classgrade == 'f':
        points = 0.0

    x+=1
    totalcredits += classhours
    totalgrade += points * classhours
    table += (classgrade +"        " + str(classhours) + "\n")

# to call the methlod and to print the results
finalgpa = calculateGPA(totalgrade, totalcredits)
printresults(finalgpa, table)

