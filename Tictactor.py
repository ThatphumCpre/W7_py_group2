class Board() :
    def __init__(self):
        self.listBoard = [[" "," "," "],[" "," "," "],[" "," "," " ]]
        self.player="o"
        self.round=1
        self.text = TextInput()
        self.print = Printer()

    def start(self) :
        self.print.drawBoard(self)
        while(self.winCheck()) :
            if self.round > 9:
                break
            if self.round%2==1 :
                self.player = "o"
            else :
                self.player = "x"
            print("Player",self.player,"Turn ")
            self.text.placeMarker(self.player, self)
            self.print.drawBoard(self)
        if not self.winCheck():
            print("Player",self.player,"win.")
        else:
            print("Draw")

    def getBoard(self,position_x,position_y) :
        return self.listBoard[position_x][position_y]

    def setBoard(self,position_x, position_y) :
        self.listBoard[position_x][position_y] = self.player
        self.round += 1

    def winCheck(self) :
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
    def placeMarker(self, player,obj) :
        x = int(input("insert x : "))
        y = int(input("insert y : "))
        if((x>2 or x<0 or y>2 or y<0)) :
            print("Error Insert again")
        elif (obj.getBoard(x,y)!=" ") :
            print("Overlap Insert again")
        else :
            obj.setBoard(x, y)

class Printer() :
    def drawBoard(self,obj) :
        print(obj.listBoard[0][0] + " | " + obj.listBoard[0][1] + " | " + obj.listBoard[0][2])
        print("----------")
        print(obj.listBoard[1][0] + " | " + obj.listBoard[1][1] + " | " + obj.listBoard[1][2])
        print("----------")
        print(obj.listBoard[2][0] + " | " + obj.listBoard[2][1] + " | " + obj.listBoard[2][2]+"\n")

game1=Board()
game1.start()
