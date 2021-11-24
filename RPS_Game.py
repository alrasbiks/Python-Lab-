'''
* The purpose of this program is to build RPS game coding Program in python
*
* Author : Khalid Al Rasbi
* last Edit Date : 04/14/2021
'''

from random import randint
# making a list of game
t = ["R", "P", "S"]
#-1 computer wins; 0 tie : 1 user wins

# function for greeting the user
def Greeting ():
    print(" Welcome to RPS game")
# function to play for the computers
def generateComputuresChoice ():
    return t[randint(0,2)]
# function to play for the user
def enterPlayersChoice(gameNumber) :
    player= input("Please enter your selection for game #"+str(gameNumber)+"\n"
                   "Enter:\n"
                   "'R' for rock,\n"
                   "'P' for paper, or \n"
                   "'S' for scissors.\n")
    return player
# needing to make everyting = 0 in ordr to count them latter
userWins = 0
totalGames = 0
Greeting()
scores = []
# making a while loop for the game so it will repat after game 3
while True:

  for i in range(3):
      gameNumber = i+1
      while True:
        player = enterPlayersChoice(gameNumber)
        if player in t:
          break
        else:
          print("That's not a valid play.")
      computer = generateComputuresChoice()

      if player == computer:
          print("Tie!")
          scores.append(0)
      elif player == "P":
          if computer == "R":
              print("You win! Paper covers Rock")
              scores.append(1)
          else:
              print("You lose! Scissors cut Paper")
      elif player == "R":
          if computer == "P":
              print("You lose! Paper covers Rock")
              scores.append(-1)
          else:
              print("You win! Rock smashes Scissors")
              scores.append(1)
      elif player == "S":
          if computer == "R":
              print("You lose! Rock smashes Scissors")
              scores.append(-1)
          else:
              print("You win! Scissors cut Paper" )
              scores.append(1)

   # to print the result
  print("Total games=3")
  print("Total ties=",scores.count(0))

  userWins += scores.count(1)
  totalGames +=3

  # after finshing the first 3 round to countune after 3 games 
  x = input("Press any key to continue or q to quit \n")
  if x.lower() == 'q':
    break

# to keep track on the total games and total wins
print("Total Games cumulative:",totalGames)
print("Total wins that you had:",userWins)
print("Total wins that computer had:", scores.count(-1))
print("total tie you had: ", scores.count(0))