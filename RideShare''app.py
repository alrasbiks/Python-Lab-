'''
* The purpose of this program is to test is for the first lab assignment
*
* Author : Khalid Al Rasbi
* last Edit Date : 02/24/2021
'''
# this part is to write the intro the user will see before enter his data
print ("$$$$$$$$$$$$  RideShare APP $$$$$$$$$$$$")
print ("\n \n GIVEN THIS DATA")
print ("\n---------------------")

#this the first part to make input  with asking this user to enter his data about class info
print ("\n Class info:")
number_class_meets = int(input("  number days/week class meets: "))
number_weeks = int(input("  number weeks in the semester: "))

#this is the second part for the user to enter his data about gas info
print ("\n Gas info:")
average_mpg = int(input("  car's average mpg: "))
price_gas_per_gallon = float(input("  price of gas per gallon: "))

#this is the thrid part for asking the user to enter his data about journey info
print ("\n Journey info:")
distance_to_discovery_hall = int(input("  1-way distance to Discovery Hall: "))

# after this part we have all the data needed to collecte for the user and the work will start to cont
print ("\n \n THE RESULTS")
print ("----------------")

# now it all about finding the function we need
# since we ask the user for one way we need to make it for 2 way by *2
Way_distance_to_discovery = distance_to_discovery_hall * 2

# this function is to know the number roud trip
number_roud_trips = (number_class_meets * number_weeks)
#here is to display it to the user
print ("Number of roud trips/semester: ", number_roud_trips)

#this function is to know the total number of miles
total_number_miles = Way_distance_to_discovery * number_roud_trips
#here is to display it to the user
print ("Total number of miles/semester: ", total_number_miles)

#this function to cost for 1 roud
# need to do it in two different function, 1 to find the average mpg, 2 to find the cost for 1 roud
way_to_find_average_mpg = (float(Way_distance_to_discovery) / average_mpg)
cost_for_1_roud = round ((way_to_find_average_mpg * price_gas_per_gallon), 2)
#here is to display it to the user
print ("Cost for 1 roud-trip (for gas): ", cost_for_1_roud)

# this function to know the total cost for one semester
total_cost_for_semester = cost_for_1_roud * number_roud_trips
# here is to display it to the user
print ("Total cost for semster (for gas): ", total_cost_for_semester)

# this is last part in the programing to know the cost for 1,2,3 persons
# here is to display the last part for the user to see
print ("\n \n Cost per person for the semester")
print ("\n -----------------------------------------")

#here is to make function to know the result that the user will see

# here is for one person
person = total_cost_for_semester
# here is to display the result
print ("For 1 person:", person)

# here is for 2 persons
person2 = total_cost_for_semester/2
# here is to diplay the result
print ("For 2 people sharing:", person2)

# here is for 3 persons
person3 = total_cost_for_semester/3
#here is to display the result
print ("For 3 people sharing:", person3)