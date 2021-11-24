# in this lab I will lean more on how to work with test by using Python file as I already have the output
# but I will need to use two different way to get the job done
# first way I will print the five lines each one of them in a separate line and I will make sure about specing and how may number of * needed in one line
# second way I will create funcaton for each line with follwing the same way in the preive one, then I will use print to display the output and I will make sure there is new line btween the funcation

print (" *** " "  ** **  " " * " " ***** " " ***** ")
print ("  *  " " *  *  * " " * " "     * " " *   * ")
print ("  *  " "  *   *  " " * " " ***** " " *   * ")
print ("  *  " "   * *   " " * " "     * " " *   * ")
print (" *** " "    *    " " * " " ***** " " ***** ")
print (" *** " "  ** **  " " * " " ***** " " ***** ")
print ("  *  " " *  *  * " " * " "     * " " *     ")
print ("  *  " "  *   *  " " * " " ***** " " ***** ")
print ("  *  " "   * *   " " * " "     * " " *   * ")
print (" *** " "    *    " " * " " ***** " "  ***  ")

line1 = " *** " "  ** **  " " * " " ***** " " ***** "
line2 = "  *  " " *  *  * " " * " "     * " " *     \n"
line3 = "  *  " "  *   *  " " * " " ***** " " ***** \n"
line4 = "  *  " "   * *   " " * " "     * " " *   * \n"
line5 = " *** " "    *    " " * " " ***** " "  ***  "
print(line1 + "\n" +line2 + line3 + line4 + line5)