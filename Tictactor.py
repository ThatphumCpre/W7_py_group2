class Board() :
    def __init__(self):
        self.listBoard = [[" "," "," "],[" "," "," "],[" "," "," " ]]
        self.player="o"
        self.round=1
        self.text = TextInput();
    def start(self) :
        while(True) :
            self.text.placeMarker(self.player,self)
            print(self.listBoard)
            if self.round%2==1 :
                self.player = "o"
            else :
                self.player = "x"
    def getBoard(self,position_x,position_y) :
        return self.listBoard[position_x][position_y]
    def setBoard(self,position_x, position_y) :
        print(type(position_x))
        self.listBoard[position_x][position_y] = self.player
        self.round += 1
    def winCheck(self) :
        pass
    def clearBoard(self) :
        self.listBoard = [[" "," "," "],[" "," "," "],[" "," "," " ]]
class TextInput() :
    def placeMarker(self, player,obj) :
        x = int(input("insert x : "))
        y = int(input("insert y : "))
        if((x>2 or x<0 or y>2 or y<2) and (obj.getBoard(x,y)!=" ")) :
            print("Error Insert again")
        elif(obj.getBoard(x,y)=="o" or obj.getBoard(x,y)=="x") :
            print("Overlap Please try again")
        else :
            obj.setBoard(x, y)

class Printer() :
    def drawBoard(self) :
        pass

game1=Board()
game1.start()
