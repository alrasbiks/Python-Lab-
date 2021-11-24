'''
* The purpose of this program is to test the knowlagment about loop statement in python
*
* Author : Khalid Al Rasbi
* last Edit Date : 03/22/2021
'''



#this function returns the number of chars in string
def countChars (str1, ch):
    count = 0
    for n in range(len(str1)):
        if (str1[n]==ch):
            count = count + 1
    return count
#this part is to welcome the user
# ask the user enter his string from here
userinput = input("Enter the string: ")
letter_count = input ("Enter the character to count: ")

# this part is to making the program to know how to count th a charaters
cnt = countChars(userinput, letter_count)

# this function to print the result
def printresult (charcount):
    print(letter_count, "appears ", cnt, "time(s) in", userinput)

# to print the final result
printresult(cnt)
