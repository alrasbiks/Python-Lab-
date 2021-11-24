'''
* The purpose of this program is to build program to calculete Standrd Deviation in python
*
* Author : Khalid Al Rasbi
* last Edit Date : 04/20/2021
'''


import numpy as np

# method
def calculateSTD(arr):  # function -> argument arr
    # sqrt((sum(x-avg)^2)/len)
    average = arr.mean()
    total = 0
    #for inside the method
    for each_element in arr:
        total = total + (each_element - average) ** 2
    std_deviation = np.sqrt(total / len(arr))
    return std_deviation

# to make the display result

#for number1 file
number1 = np.genfromtxt("numbers1.csv")
std_number1 = round(calculateSTD(number1), 3)
print("The average of the numbers in file: numbers1.csv is {:.3f}".format(round(number1.mean(), 3)),
      " and standard deviation:{:.3f}".format(std_number1))

print()
print("Program terminating.")
print()

#for number2 file

number2 = np.genfromtxt("numbers2.csv")
std_number2 = round(calculateSTD(number2), 3)
print("The average of the numbers in file: numbers2.csv is ", round(number2.mean(), 3),
      "and standard deviation: {:.3f}".format(std_number2))
print()
print("Program terminating.")
print()