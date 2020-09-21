import random
#generating random numbers to place the ship
row=random.randint(0,9)
col=random.randint(0,9)
#generating random location point for horizental and vertical
randomnumber= random.randint(0,1)
#letters and numbers for the table
letrange = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
numrange = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
table = []
hiddenBoard=[]
let=0
num=0
win=False
numhit=0
numfired=0
print("Welcome to Battleship Game")
print("There is a ship that is located in 4 spots, either horziantly or verticlly, try choosing the four spots to hit to sink the ship and win")
print("H=Hit, M=Miss")
#first function is to build a hidden board that would be compared to the actual board on the screen
def buildhiddenboard():
        for x in range (10):
                y = []
                for a in range(10): 
                        y.append(" ")
                hiddenBoard.append(y)
#second function is to build a board on the screen
def buildboard():
        for x in range (10):
                y = []
                for a in range(10): 
                        y.append(" ")
                table.append(y)
#third function is to print the board made in the previous function
def printboard():
        for x in range (65,75):
                print ('  '+chr(x)+' ', end='')
        print()
        for row in range(10):
                print(row, end=' ')
                for col in range(10):
                        print(table[row][col]+' | ', end='')
                print("\n "+"---+"*10)
#this function is to generate the ship randomly, it is also to make sure that the 4 random points would be inside the table
def shipgenerator():
        global row
        global col
        if randomnumber==1:
              if  col <= 6:
                      for i in range(4):
                              hiddenBoard[row][col]="X"
                              col=col+1
              else:
                      for i in range(4):
                              hiddenBoard[row][col]="X"
                              col=col-1
        if randomnumber==0:
              if  row <= 6:
                      for i in range(4):
                              hiddenBoard[row][col]="X"
                              row=row+1
              else:
                      for i in range(4):
                              hiddenBoard[row][col]="X"
                              row=row-1
#this function is to ask the user for the input, and his guess for the place of the ship
def userinput(numfired):
        x=False
        while x==False:
                guess=input("Try to find the ship, inorder to shoot the missile, type the letter capital and number of grid. For example: I8 ")
                let=guess[0]
                num=guess[1]
                numfired=numfired+1
                if len(guess)==2:
                        if (let in letrange) and (num in numrange):
                                x=True
                        else:
                                print("the input is Invalid, please print a valid input")
                else:
                        print("the input is Invalid, please print a valid input")
        return let,num, numfired
#this function is to check if the hit done by the user matches the hit on the hiddenboard, if it does, then H would appear on the spot, if it doesn't then M would appear on the spot
def checkhit(table, hiddenBoard, numhit, win):
        if hiddenBoard[int(num)][int(ord(let))-65]=="X":
                table[int(num)][int(ord(let))-65]="H"
                numhit=numhit+1
        else:
                table[int(num)][int(ord(let))-65]="M"
        return numhit
#this function is to check when the user spot the four cells, so the user would win
def checkwin(win,numhit):
        if numhit==4:
                win=True
        return win

#this is the main function
buildboard()
buildhiddenboard()
shipgenerator()
#print(win, hiddenBoard)
print(numhit, numfired)
#while loop to keep the game going on when the user choose the wrong spot until the user wins the game
while win==False:
        printboard()
        let,num, numfired=userinput(numfired)
        numhit=checkhit(table, hiddenBoard, numhit, win)
        win=checkwin(win,numhit)
        print(numhit)
        accuracy=(numhit/numfired)*100
        print("Your Accuracy Rate Is: "+str(accuracy)+"%")
printboard()
#if statement so if the user win, the game would show his winning msg
if win==True:
        print("Good Job on Winning the Game, YOUR ACCURACY RATE IS"+str(accuracy)+"%")
