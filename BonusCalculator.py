'''
* The purpose of this program is to test the knowlagment about input and if and else if statement in python
*
* Author : Khalid Al Rasbi
* last Edit Date : 03/10/2021
'''

# first part to print the welcoming statnment
print(" *** WELCOME TO YEAR END BONUS CALCULATOR ***")

# Now this part is for input statnment for the user
know_code = int (input(" Please Enter the position code (1,2,or3)" "\n"))
# part that Weekly Salary of the employee from user
weekSalary =  int (input(" Please Enter weekly Salary of the employee" "\n"))
# part to find time
employed_time =float (input(" Please Enter the time if the employee""\n"))
# this part is to find the base bonus by using IF
baseBonus = weekSalary


if know_code ==1 :
    baseBonus = baseBonus
elif know_code == 2:
    baseBonus = 2*baseBonus
    if baseBonus <= 700:
        baseBonus = baseBonus
    elif baseBonus > 700:
        baseBonus = 700
elif know_code ==3:
    baseBonus = (1.5*baseBonus)
# this part is for others calculting

if employed_time <2:
    totalBonus = (baseBonus/2)
elif employed_time >10:
    totalBonus = baseBonus + 100
else :
    totalBonus = baseBonus
#dispaly the total bonus of the employee
print("The total bonus of the employee is ", totalBonus, "$")