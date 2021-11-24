'''
* The purpose of this program is to English Spanhish Program in python
*
* Author : Khalid Al Rasbi
* last Edit Date : 04/7/2021
'''

#intro for this program that the user could see
intro = "This program will read the data in from the\n" \
        "file \"spanishDictionary.csv\" and will determine which\n" \
        "the meaning for the word you enter in Spanish\n\n "
print(intro)

import csv

# while loop statement
while True:
    #to ask input from the user
    input_word = input(" Enter word to translate to Spanish: ")
    # to quit the program
    if input_word.lower() != 'q':
    # if the user it not quit it
        word_check = True
    # the bonus one to scan all the characters and check the word
        for each_char in input_word:
            if 65 <= ord(each_char) <= 122:
                pass
            else:
                word_check = False
                break
        if word_check == True :
            #to read the file that have the words
             with open("spanishDictionary.csv", 'r+') as fd:
                  found = False
                  for each in fd:
                      each_list = each.split()
                      if len(each_list) == 2 and each_list[0] == input_word:
       # part to print the result with both English and Spanish words
                       print('English: "'+each_list[0]+'" translated to spanish as "'+each_list[1]+'"')
                       found = True
                       break
              # part for the second bouns to work to add word that wasn't in the file
                  if found == False :
                      print("word could not be found")
                      enter_word = input ("Would you like to enter new word to translate to Spanish, this word.(y/n)\n")
                      if enter_word.lower() == 'y':
                          spanish_translation = input("Enter the spanish translation: ")
                          csv.writer(fd).writerow([input_word+" "+spanish_translation])
                         
                      elif enter_word.lower() == 'n':
                       print("Thank you, have a good day")
    else:
     break




