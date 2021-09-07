import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QWaitCondition
# from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtTest

class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        
        W = Window() # it provides access for methods (especially) of main class 
        self.validator = QDoubleValidator() # it can be used if digit only structure needed

        self.setWindowTitle("bankCore version(2.5)")
        self.setGeometry(200, 200, 600, 600)

        self.txt = QtWidgets.QTextBrowser(self)
        W.textbrowser(self.txt, "Please type your identity number and password.", 10, 125, 100, 350, 50)
        # self.txt.setReadOnly(1)
        # self.txt.setText("Please type your identity number and password.")
        # self.txt.setFont(QFont("Arial", 10))
        # self.txt.move(125, 100)
        # self.txt.resize(350, 50).

        self.idlabel = QtWidgets.QLabel(self) 
        W.label(self.idlabel, "Identity Number:", 75, 210, 120, 25)

        self.idtext = QtWidgets.QLineEdit(self)
        W.linedit(self.idtext, 200, 200, 200, 50, 11)
        self.idtext.setValidator(self.validator)

        self.pswlabel = QtWidgets.QLabel(self)
        W.label(self.pswlabel, "Password:", 113, 285, 80, 25)

        self.pswtext = QtWidgets.QLineEdit(self)
        W.linedit(self.pswtext, 200, 275, 200, 50, 15)

        self.logButton = QtWidgets.QPushButton(self)
        W.cbutton(self.logButton, "Log In", 200, 350, 200, 50, self.returnWindow) # connection will be self.interfaceWindow

        self.returnButton = QtWidgets.QPushButton(self)
        W.cbutton(self.returnButton, "Return", 200, 425, 200, 50, self.returnWindow)        

        # txt.setText(f"Logged in.") # if process is successful, this text will be shown
        # self.win.show()

        # sys.exit(app.exec_())

    def returnWindow(self):
        self.a = Window()
        self.a.show()
        self.hide()


"""
def loginWindow(self): # login window when pressed login
    # win.setWindowTitle("bankCore version(2.5)")
    # win.setGeometry(200, 200, 600, 600)

    self.txt = QtWidgets.QTextBrowser("Please type your identity number and password.", self)
    self.txt.setText("Please type your identity number and password.")
    self.txt.setFont(QFont("Arial", 10))
    self.txt.move(125, 100)
    self.txt.resize(350, 50)

    self.idlabel = QtWidgets.QLabel("Identity Number: ", self) # string intersects with the box
    self.idlabel.resize(120, 25) # idlabel.setFixedSize(120, 30) # --> an alternative
    self.idlabel.setFont(QFont("Arial", 10))
    self.idlabel.move(75, 210)

    self.idtext = QtWidgets.QLineEdit(self)
    self.idtext.setMaxLength(11)
    self.idtext.setFont(QFont("Arial", 18))
    self.validator = QDoubleValidator()
    self.idtext.setValidator(self.validator)
    # validator.setRange(10000000000, 99999999999) # try to fix this
    # input only accepts integer values, try to make it 11 digits limitation for the box
    self.idtext.move(200, 200)
    self.idtext.resize(200, 50)

    self.pswlabel = QtWidgets.QLabel("Password:", self)
    self.pswlabel.setText("Password:") # string intersects with the box
    self.pswlabel.resize(80, 25) # idlabel.setFixedSize(120, 30) # --> an alternative
    self.pswlabel.setFont(QFont("Arial", 10))
    self.pswlabel.move(113, 285)

    self.pswtext = QtWidgets.QLineEdit(self)
    self.pswtext.setMaxLength(15)
    self.pswtext.setFont(QFont("Arial", 18))
    # pswtext.setText("")
    # validator = QValidator()
    # pswtext.setValidator(validator)
    self.pswtext.move(200, 275)
    self.pswtext.resize(200, 50)

    self.logButton = QtWidgets.QPushButton("Log In", self)
    self.logButton.move(200, 350)
    self.logButton.resize(200, 50)

    self.returnButton = QtWidgets.QPushButton("Return", self)
    self.returnButton.move(200, 425)
    self.returnButton.resize(200, 50)

    # txt.setText(f"Logged in.") # if process is successful, this text will be shown
    self.win.show()

    # sys.exit(app.exec_())
"""

class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("bankCore version(2.5)")
        self.setGeometry(200, 200, 600, 600)

        self.txt = QtWidgets.QTextEdit("Welcome to bankCore!", self)
        self.txt.setReadOnly(1)
        self.txt.setFont(QFont("Arial", 20))
        self.txt.move(125, 100)
        self.txt.resize(350, 50)

        self.logButton = QPushButton(self)
        self.cbutton(self.logButton, "Log In", 200, 200, 200, 50, self.loginWindow)

        self.signButton = QtWidgets.QPushButton(self)
        self.button(self.signButton, "Sign In", 200, 275, 200, 50)

        self.aboutButton = QtWidgets.QPushButton(self)
        self.button(self.aboutButton, "About bankCore", 200, 350, 200, 50)

        self.exitButton = QtWidgets.QPushButton(self)
        self.button(self.exitButton, "Exit", 200, 425, 200, 50)

        self.show()
    
    def loginWindow(self):
        self.w = Window2()
        self.w.show()
        self.hide()

    def timer(self, x):
        QtTest.QTest.qWait(x)

    def button(self, buttoname, buttontext, xmove, ymove, xsize, ysize): # buttoname = QtWidgets.QPushButton(win) can be integrated
        buttoname.setText(buttontext)
        buttoname.move(xmove, ymove)
        buttoname.resize(xsize, ysize)

    def cbutton(self, buttoname, buttontext, xmove, ymove, xsize, ysize, connection):
        buttoname.setText(buttontext)
        buttoname.move(xmove, ymove)
        buttoname.resize(xsize, ysize)
        buttoname.clicked.connect(connection)

    def label(self, labelname, labeltext, xmove, ymove, xsize, ysize): # add variable for fontSize if needed
        labelname.setText(labeltext)
        labelname.move(xmove, ymove)
        labelname.resize(xsize, ysize)
        labelname.setFont(QFont("Arial", 10)) # if necessary add fontSize for different sizes

    def linedit(self, lineditname, xmove, ymove, xsize, ysize, maxlength):
        lineditname.move(xmove, ymove)
        lineditname.resize(xsize, ysize)
        lineditname.setMaxLength(maxlength)
        lineditname.setFont(QFont("Arial", 18)) # change the fontSize if necessary

    def textbrowser(self, textbname, textbtext, tfontsize, xmove, ymove, xsize, ysize):
        textbname.setReadOnly(1)
        textbname.setText(textbtext)
        textbname.setFont(QFont("Arial", tfontsize))
        textbname.move(xmove, ymove)
        textbname.resize(xsize, ysize)
        
        # validator = QValidator()
        # pswtext.setValidator(validator) # --> those can be useful
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())