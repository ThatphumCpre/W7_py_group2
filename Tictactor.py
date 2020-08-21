class Board() :
    def __init__(self):
        self.listBoard = [[" "," "," "],[" "," "," "],[" "," "," " ]]
        self.player="o"   #start player
        self.round=1        #starter round
        self.text = TextInput()  #instance from class  to Input and drawBoard
        self.printed = Printer()

    def start(self) :
        self.printed.drawBoard(self)      #draw empty board
        while(self.winCheck()) :       #check if someone win
            if self.round > 9:         #if round over 9 then stop
                break
            if self.round%2==1 :        #swap player
                self.player = "o"
            else :
                self.player = "x"
            print("Player",self.player,"Turn ")  #display turn
            self.text.placeMarker(self.player, self)  #input to the board
            self.printed.drawBoard(self)          #draw new board
        if not self.winCheck():                 #if someone wins
            print("Player",self.player,"win.")
        else:       #if draw
            print("Draw")

        if int(input("""Enter "1" to play  again else to stop """))==1 :
            self.clearBoard()
            self.start()

    def getBoard(self,position_x,position_y) :  #getter method
        return self.listBoard[position_x][position_y]

    def setBoard(self,position_x, position_y) :     #setter setBoard
        self.listBoard[position_x][position_y] = self.player
        self.round += 1

    def winCheck(self) :  #if someone wins return false to stop loop
        if self.listBoard[0][0] == self.listBoard[0][1] == self.listBoard[0][2] and self.listBoard[0][2] != " ":
            return False
        elif self.listBoard[1][0] == self.listBoard[1][1] == self.listBoard[1][2] and self.listBoard[1][2] != " ":
            return False
        elif self.listBoard[2][0] == self.listBoard[2][1] == self.listBoard[2][2] and self.listBoard[2][2] != " ":
            return False
        elif self.listBoard[0][0] == self.listBoard[1][0] == self.listBoard[2][0] and self.listBoard[2][0] != " ":
            return False
        elif self.listBoard[0][1] == self.listBoard[1][1] == self.listBoard[2][1] and self.listBoard[2][1] != " ":
            return False
        elif self.listBoard[0][2] == self.listBoard[1][2] == self.listBoard[2][2] and self.listBoard[2][2] != " ":
            return False
        elif self.listBoard[0][0] == self.listBoard[1][1] == self.listBoard[2][2] and self.listBoard[2][2] != " ":
            return False
        elif self.listBoard[0][2] == self.listBoard[1][1] == self.listBoard[2][0] and self.listBoard[2][0] != " ":
            return False
        else:
            return True

    def clearBoard(self) :
        self.listBoard = [[" "," "," "],[" "," "," "],[" "," "," " ]]

class TextInput() :
    def placeMarker(self, player,obj) :  #input
        x = int(input("insert x : "))
        y = int(input("insert y : "))
        if((x>2 or x<0 or y>2 or y<0)) :  #if is over bound
            print("Error Insert again")
        elif (obj.getBoard(x,y)!=" ") :  #if it's overlap
            print("Overlap Insert again")
        else :
            obj.setBoard(x, y)  #set to board

class Printer() :
    def drawBoard(self,obj) :  #preview board
        print(obj.listBoard[0][0] + " | " + obj.listBoard[0][1] + " | " + obj.listBoard[0][2])
        print("----------")
        print(obj.listBoard[1][0] + " | " + obj.listBoard[1][1] + " | " + obj.listBoard[1][2])
        print("----------")
        print(obj.listBoard[2][0] + " | " + obj.listBoard[2][1] + " | " + obj.listBoard[2][2]+"\n")

game1=Board()#instance obj from Board
game1.start()#start game
