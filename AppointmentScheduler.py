'''
* The purpose of this program is to test the knowlagment about input and if and else if statement in python
*
* Author : Khalid Al Rasbi
* last Edit Date : 03/03/2021
'''

# this first part is for the first input function
Appointment_day = input ("For your next vist to our office, would you prefer Monday or Friday?"
                     "\n For Monday, enter 'm'"
                     "\n For Friday enter 'f'" "\n" )
# in this part thr program will start working on if statement according to what user enter
# if the user enter m to the day
if Appointment_day == 'm':
# the prgram would start asking the second queation releted the time
    Appointment_time = input ("On Monday, would you prefer the morning or afternoon?"
          "\n For morning, enter 'm'"
          "\nFor afternoon, enter 'a'" "\n" )
# depeding on the user answer the prgram will work
# if it m
    if Appointment_time =='m':
      Appointment_hour = int (input ("On Monday morning between 8:00 and 12:00, what time would you like?" "\n" ))
# the system print the final result
      print("Your next appointment is on Monday morning at", Appointment_hour)
# if it a
    elif Appointment_time =='a':
        Appointment_hour = int (input("On Monday afternoon between 1:00 and 4:00, what time would you like?"))
# the system print the final result
        print("Your next appointment is on Monday morning at", Appointment_hour)
    else: print("this input is not exit ")

# if the user enter f to the day
elif Appointment_day == 'f':
    Appointment_time = input ("On Friday, would you prefer the morning or afternoon?"                     
          "\n For morning, enter 'm'"
          "\nFor afternoon, enter 'a'" "\n" )
# the program would work according to what the user might enter
# if the answer m
    if Appointment_time =='m':
      Appointment_hour = int (input ("On Monday morning between 8:00 and 12:00, what time would you like?" "\n" ))
# the system print the final result
      print("Your next appointment is on Monday morning at", Appointment_hour)
# if the answer a
    elif Appointment_time =='a':
        Appointment_hour = int (input ("On Monday afternoon between 1:00 and 4:00, what time would you like?"))
# the system print the final result
        print("Your next appointment is on Monday morning at", Appointment_hour)
    else: print("this input is not exit")
# if the answer it not exit
else: print("this input is not exit ")