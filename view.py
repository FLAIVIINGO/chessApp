from tkinter import Tk, FALSE, Menu, Canvas, Frame, Label, RIGHT

class View():

    def __init__(self, root):
        self.root = root
        self.color1 = "#7F00FF"
        self.color2 = "#00FF00"
        self.createChessWindow()

    def createChessWindow(self):
        self.root.option_add('*tearOff', FALSE)
        self.createMenubar()

    def createMenubar(self):
        self.menubar = Menu(self.root)
        self.createFileMenu()
        self.createEditMenu()
        self.createHelpMenu()
        self.root['menu'] = self.menubar
        self.createCanvas()
        self.drawChessboard()
        self.createGameInfo()

    def createFileMenu(self):
        menuFile = Menu(self.menubar)
        self.menubar.add_cascade(menu=menuFile, label='File')

    def createEditMenu(self):
        menuEdit = Menu(self.menubar)
        self.menubar.add_cascade(menu=menuEdit,label='Edit')

    def createHelpMenu(self):
        menuHelp = Menu(self.menubar)
        self.menubar.add_cascade(menu=menuHelp, label='About')

    def createCanvas(self):
        squareDimensions = 64 # in pixels
        numSquares = 8 # square's rows and cols
        canvasSize = squareDimensions * numSquares
        self.canvas = Canvas(self.root, width=canvasSize, height=canvasSize, background='gray75')
        self.canvas.pack(padx=8, pady=8)

    def createGameInfo(self):
        self.gameInfoFrame = Frame(self.root, height=128)
        self.infoLabel = Label(self.gameInfoFrame, text="      White to Start     ", fg='black')
        self.infoLabel.pack(side=RIGHT, padx=8, pady=5)
        self.gameInfoFrame.pack(fill="x", side="bottom")

    def drawChessboard(self):
        currentColor = self.color2
        for row in range(8):
            currentColor = self.getColor(currentColor)
            for col in range(8):
                x1 = self.getXCoordinate(col)
                y1 = self.getYCoordinate(row)
                x2 = x1 + 64
                y2 = y1 + 64
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=currentColor)
                currentColor = self.getColor(currentColor)

    def getColor(self, currentColor):
        if currentColor == self.color2:
            nextColor = self.color1
        else:
            nextColor = self.color2
        return nextColor


    def getXCoordinate(self, col):
        return (col * 64)

    def getYCoordinate(self, row):
        return (7 - row) * 64


def main():
    root = Tk()
    root.title("Chess")
    View(root) 
    root.mainloop()


def init_new_game():
    main()

if __name__ == "__main__":
    init_new_game()