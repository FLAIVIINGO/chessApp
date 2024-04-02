from tkinter import Tk, FALSE, Menu, Canvas, Frame, Label, RIGHT

class View():

    def __init__(self, root):
        self.root = root
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
        squareDimensions = 100 # in pixels
        numSquares = 8 # square's rows and cols
        canvasSize = squareDimensions * numSquares
        self.canvas = Canvas(self.root, width=canvasSize, height=canvasSize, background='gray75')
        self.canvas.pack(padx=8, pady=8)

    def createGameInfo(self):
        self.gameInfoFrame = Frame(self.root, height=128)
        self.infoLabel = Label(self.gameInfoFrame, text="      White to Start     ", fg='black')
        self.infoLabel.pack(side=RIGHT, padx=8, pady=5)
        self.gameInfoFrame.pack(fill="x", side="bottom")

def main():
    root = Tk()
    root.title("Chess")
    View(root) 
    root.mainloop()


def init_new_game():
    main()

if __name__ == "__main__":
    init_new_game()