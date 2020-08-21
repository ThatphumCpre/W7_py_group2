class Board() :
    def __init__(self):
        self.listBoard = [[" "," "," "],[" "," "," "],[" "," "," " ]]
        self.player="o"
        self.round=1
        self.text = TextInput()
		self.Print = Printer()

    def start(self) :
        while(True) :
            print("Player",self.player,"Turn ")
            self.text.placeMarker(self.player, self)
            print(self.listBoard)
            if self.round%2==1 :
                self.player = "o"
            else :
                self.player = "x"
				self.Print.drawBoard(self)

    def getBoard(self,position_x,position_y) :
        return self.listBoard[position_x][position_y]

    def setBoard(self,position_x, position_y) :
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
        if((x>2 or x<0 or y>2 or y<2)) :
            print("Error Insert again")
        elif (obj.getBoard(x,y)!=" ") :
            print("Overlap Insert again")
        else :
            obj.setBoard(x, y)

class Printer() :
    def drawBoard(self,obj) :
        println(obj.listBoard[0][0] + " | " + obj.listBoard[0][1] + " | " + obj.listBoard[0][2])
		println("-------------")
		println(obj.listBoard[0][0] + " | " + obj.listBoard[0][1] + " | " + obj.listBoard[0][2])
        println("-------------")
		println(obj.listBoard[0][0] + " | " + obj.listBoard[0][1] + " | " + obj.listBoard[0][2]+"\n")

game1=Board()
game1.start()
