#print("Hello, world!")

#print ('Hello')


keep_going = "y"
while keep_going == "y":
    sales =input ('Amount of sales :')
    sales =int(sales)
    #comm_rate = input('Enter the commission rate')
    #commission = float(comm_rate)
    comm_rate = float (input('Enter the commission rate :'))
    commission = sales * comm_rate
    print (commission)
    #cont = sales * commission
    #print(cont)
    keep_going2 = input("Do you want to calculate another commission Enter y for yes: ")
    if keep_going2=='y':
        keep_going="y"
    else:
        keep_going2="n"


