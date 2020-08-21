class Board() :
    def __init__(self):
        self.listBoard = [[" "," "," "],[" "," "," "],[" "," "," " ]]
        self.player="o"
        self.round=1
    def setBoard(self) :
        pass
    def getValues(self) :
        pass
    def setValues(self) :
        pass
    def winCheck(self) :
        pass
    def clearBoard(self) :
        pass
class TextInput() :
    def put(self) :
        x = int(input("insert x : "))
        y = int(input("insert y : "))

class Printer() :
    def drawBoard(self) :
        pass
text = TextInput();
text.put()
