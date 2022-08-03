import random
from tabulate import tabulate

class football:
# initialising positiong with each player at goalpost and the ball in the centre
    def __init__(self):
        self.start = (2,1)
        self.ball = (2,1)
        self.goal1 = (0,1)
        self.goal2 = (4,1)
        self.player1 = (0,1)
        self.player2 = (4,1)
        self.move = 1

# place the player who is startin gthe game in the centre with the ball
    def startGame(self):
        self.ball = self.start
        self.startingPlayer = int(input("Which Player starts?\nPlayer "))
        if self.startingPlayer == 1:
            self.player1 = self.start
            self.move = 1
        elif self.startingPlayer == 2:
            self.player2 = self.start
            self.move = 2
        else:
            print("Wrong Input, Try Again")
            return self.startGame()

# random kick to left of the player
    def player2Kick(self, currentPos):
        newPos1 = 4
        if currentPos==0:
            print("Kick not possible")
            return currentPos
        while newPos1>currentPos[0]:
            newPos1 = random.randint(0,4)
        return (newPos1, random.randint(0,2))

# random kick to right of the player
    def player1Kick(self, currentPos):
        newPos1 = 0
        if currentPos==4:
            print("Kick not possible")
            return currentPos
        while newPos1<currentPos[0]:
            newPos1 = random.randint(0,4)
        return (newPos1, random.randint(0,2))

# move to left with the ball
    def player2MoveWBall(self, currentPos): # similar function to move, but with an added filter that the player can only go "forward"
        print("Player 2", currentPos)
        possibleMoves = [(currentPos[0]-1, i) for i in range(0,3)]
        if currentPos[1] == 0:
            possibleMoves.pop(2)
        elif currentPos[1] == 2:
            possibleMoves.pop(0)
        print("Possible moves:\nEnter the corresponding number to move to that location")
        for i in range(len(possibleMoves)):
            print(possibleMoves[i],"-",i)
        while True:
            choice = int(input("Choice: "))
            if choice >=0 and choice < len(possibleMoves):
                return possibleMoves[choice]
            print("Wrong Input.\nTry Again")

# move to the right with the ball
    def player1MovewBall(self, currentPos): # similar function to move, but with an added filter that the player can only go "forward"
        print("Player 1", currentPos)
        possibleMoves = [(currentPos[0]+1, i) for i in range(0,3)]
        if currentPos[1] == 0:
            possibleMoves.pop(2)
        elif currentPos[1] == 2:
            possibleMoves.pop(0)
        print("Possible moves:\nEnter the corresponding number to move to that location")
        for i in range(len(possibleMoves)):
            print(possibleMoves[i],"-",i)
        while True:
            choice = int(input("Choice: "))
            if choice >=0 and choice < len(possibleMoves):
                return possibleMoves[choice]
            print("Wrong Input.\nTry Again")

# move to any available position
    def player2Move(self, currentPos):
        print("Player 2", currentPos)
        lMoves = [currentPos[0]+i for i in range(-1, 2)] # creates a range of coordinates move one block forward or backward
        bMoves = [currentPos[1]+i for i in range(-1, 2)] # create a range of coordinate move one block upward or below
        possibleMoves = []
        for i in lMoves:
            if i >= 0 and i < 5:
                for j in bMoves:
                    if j >=0 and j < 3:
                        possibleMoves.append((i, j)) # combine above two lists to compute all valid new locations
        print("Possible moves:\nEnter the corresponding number to move to that location")
        possibleMoves.remove(currentPos)
        for i in range(len(possibleMoves)): # list out all possible moves
            print(possibleMoves[i],"-",i)
        while True: # check for valid choices
            choice = int(input("Choice: "))
            if choice >=0 and choice < len(possibleMoves):
                return possibleMoves[choice]
            print("Wrong Input.\nTry Again")

# move to any available position
    def player1Move(self, currentPos):
        print("Player 1", currentPos)
        lMoves = [currentPos[0]+i for i in range(-1, 2)] # creates a range of coordinates move one block forward or backward
        bMoves = [currentPos[1]+i for i in range(-1, 2)] # create a range of coordinate move one block upward or below
        possibleMoves = []
        for i in lMoves:
            if i >= 0 and i < 5:
                for j in bMoves:
                    if j >=0 and j < 3:
                        possibleMoves.append((i, j)) # combine above two lists to compute all valid new locations
        print("Possible moves:\nEnter the corresponding number to move to that location")
        possibleMoves.remove(currentPos)
        for i in range(len(possibleMoves)): # list out all possible moves
            print(possibleMoves[i],"-",i)
        while True: # check for valid choices
            choice = int(input("Choice: "))
            if choice >=0 and choice < len(possibleMoves):
                return possibleMoves[choice]
            print("Wrong Input.\nTry Again")

# ask human player about their decision
    def returnChoice(self)
        kOrM = str(input("Enter k to kick or m to move with the ball\nEnter: "))
        if kOrM == 'k':
            return 1
        if kOrM == 'm':
            return 0
        else:
            print('Invalid Selection')
            return self.returnChoice()

# main driving logic of the code
# move decides who will play, 1 for player1 and 2 for player2
# if the player deos not have the ball then they do not have the option to kick
# if th eplayer moves with the ball then they should have the same co-ordinates
# check if any of the players have won the game
# take next turn
    def takeTurns(self):
        if self.move == 1:
            self.move = 2
            if self.ball == self.player1: # if player has the ball, they can either kick or move
                choice = self.returnChoice()
            else:
                choice = -1 # has to move if they do not have the ball
            if choice == 1:
                self.ball = self.player1Kick(self.player1)
            elif choice == 0:
                self.player1 = self.player1MovewBall(self.player1) # ball will have the same new coordinate as the player
                self.ball = self.player1
            else:
                self.player1 = self.player1Move(self.player1)
        elif self.move == 2:
            self.move = 1
            if self.ball == self.player2: # if player has the ball, they can either kick or move
                choice = self.returnChoice()
            else:
                choice = -1 # has to move if they do not have the ball
            if choice == 1:
                self.ball = self.player2Kick(self.player2)
            elif choice == 0:
                self.player2 = self.player2MoveWBall(self.player2) # ball will have the same new coordinate as the player
                self.ball = self.player2
            else:
                self.player2 = self.player2Move(self.player2)
        if self.player2 == self.ball and self.ball == self.player1:
            if self.move == 1:
                self.move = 2
            else:
                self.move = 1
        if self.ball == (0,1) and self.player1 != (0,1): # if ball is in the goal cell and P1 is no there to block it
            print("Player 2 Wins\n")
            exit(0)
        elif self.ball == (4,1) and self.player2 != (4,1): # if ball is in the goal cell and P2 is not there to block it
            print("Player 1 Wins\n")
            exit(0)

# print the position of the players and ball on the field after every turn for visual representation
    def printField(self):
        field = [ # co-ordinates of the field as displayed in the original question
        ["- 0,0 -", "- 1,0 -", "- 2,0 -", "- 3,0 -", "- 4,0 -"],
        ["- 0,1 -", "- 1,1 -", "- 2,1 -", "- 3,1 -", "- 4,1 -"],
        ["- 0,2 -", "- 1,2 -", "- 2,2 -", "- 3,2 -", "- 4,2 -"],
        ]
        p1y, p1x = self.player1
        p2y, p2x = self.player2
        by, bx = self.ball
        field[p1x][p1y] = "P1"
        if field[p2x][p2y][0] != "-": # if P1 is already there
            field[p2x][p2y] += " + P2"
        else:
            field[p2x][p2y] = "P2"
        if field[bx][by][0] != "-": # if P1 or P2 or both are already there
            field[bx][by] += " + B"
        else:
            field[bx][by] = "B"
        print(tabulate(field, tablefmt="fancy_grid"))

# start the code by creating a objecting and calling funcitons
    def main():
        classOBJ = football()
        classOBJ.startGame()
        while True:
            classOBJ.printField() # print field ot know the position of P1, P2 and the Ball
            classOBJ.takeTurns()

if __name__ == '__main__':
    football.main()
