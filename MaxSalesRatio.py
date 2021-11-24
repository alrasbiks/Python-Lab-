


intro = "This program will read the data in from the\n" \
        "file \"Shop_data.csv\" and will determine which\n" \
        "shop has the higest netSales to grosssales ratio.\n\n " \
        "For this demo, the user does not enter anything.\n" \
        "The shop with the highest ratio will be displayed"

print(intro)

#Initializing variable
maxCity = ""
maxID = ""
maxSales = 0
maxExpenses = 0
maxRatio = 0

# Initalizing file IO
file = open( "Shop_data.csv", 'r' )
line = file.readline()
# read in data and process
while line!='':
    id, city, sales, expenses= line.split(' ')
    sales = float(sales)
    expenses = float(expenses)
    ratio = (sales - expenses) / sales

if maxRatio < ratio:
        maxID = id
        maxCity = city
        maxSales = sales
        maxExpenses = expenses
        maxRatio = ratio

        line = file.readline()

# form display

ratio = (maxSales-maxExpenses)/maxSales
display = maxCity + " has the highest ratio: \n" \
                    "( "+'{0:.3f}'.format(maxSales) +" - "+'{0:.3f}'.format(maxExpenses) +") / "\
          +'{0:.3f}'.format(maxSales) +") = "+'{0:.3f}'.format(ratio)

print(display)
