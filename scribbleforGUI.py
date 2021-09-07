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
        self.setWindowTitle("bankCore version(2.5)")
        self.setGeometry(200, 200, 600, 600)
        # self.loginWindow()


    def loginWindow(self): # login window when pressed login
        # win.setWindowTitle("bankCore version(2.5)")
        # win.setGeometry(200, 200, 600, 600)

        self.txt = QtWidgets.QTextBrowser("Please type your identity number and password.", self)
        self.txt.setText("Please type your identity number and password.")
        self.txt.setFont(QFont("Arial", 10))
        self.txt.move(125, 100)
        self.txt.resize(350, 50)

        self.idlabel = QtWidgets.QLabel("Identity Number: " ,self) # string intersects with the box
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


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("bankCore version(2.5)")
        self.setGeometry(200, 200, 600, 600)

        self.txt = QtWidgets.QTextEdit("Welcome to bankCore!", self)
        self.txt.setFont(QFont("Arial", 20))
        self.txt.move(125, 100)
        self.txt.resize(350, 50)

        self.logButton = QPushButton("Log In", self)
        self.logButton.resize(200, 50)
        self.logButton.move(200, 200)
        self.logButton.clicked.connect(self.loginWindow)

        # ^ above command is for connecting a method with the button

        self.signButton = QtWidgets.QPushButton("Sign In", self)
        self.signButton.move(200, 275)
        self.signButton.resize(200, 50)
        # self.signButton.clicked.connect() # loginWindow() ?

        self.aboutButton = QtWidgets.QPushButton("About bankCore", self)
        self.aboutButton.move(200, 350)
        self.aboutButton.resize(200, 50)
        # self.aboutButton.clicked.connect()

        self.exitButton = QtWidgets.QPushButton("Exit", self)
        self.exitButton.move(200, 425)
        self.exitButton.resize(200, 50)

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())