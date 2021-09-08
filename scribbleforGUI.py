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


class Window3(QMainWindow):
    def __init__(self):
        super().__init__()

        W = Window()

        self.setWindowTitle("bankCore version(2.5)")
        self.setGeometry(200, 200, 600, 600)

        self.txt = QtWidgets.QTextBrowser(self)
        W.textbrowser(self.txt, "Please type the informations below.", 10, 125, 100, 350, 50)

        self.namelabel = QtWidgets.QLabel(self) 
        W.label(self.namelabel, "Name:", 85, 210, 120, 25)

        self.nameline = QtWidgets.QLineEdit(self)
        W.linedit(self.nameline, 200, 200, 200, 50, 13)

        self.snamelabel = QtWidgets.QLabel(self) 
        W.label(self.snamelabel, "Surname:", 85, 266, 120, 25)

        self.snameline = QtWidgets.QLineEdit(self)
        W.linedit(self.snameline, 200, 256, 200, 50, 13) # for surname, 13 char may not be sufficient

        self.idlabel = QtWidgets.QLabel(self) 
        W.label(self.idlabel, "TCK Number:", 85, 322, 120, 25)

        self.idline = QtWidgets.QLineEdit(self)
        W.linedit(self.idline, 200, 312, 200, 50, 11)

        self.passwlabel = QtWidgets.QLabel(self) 
        W.label(self.passwlabel, "Password:", 85, 378, 120, 25)

        self.passwline = QtWidgets.QLineEdit(self)
        W.linedit(self.passwline, 200, 368, 200, 50, 15) # for password, 13 char may not be sufficient

        self.signinButton = QtWidgets.QPushButton(self)
        W.button(self.signinButton, "Sign In", 199, 425, 100, 50) # this must send variables to sql if variables are valid

        self.returnButton = QtWidgets.QPushButton(self)
        W.cbutton(self.returnButton, "Return", 301, 425, 100, 50, self.returnWindow)

    def returnWindow(self):
        self.a = Window()
        self.a.show()
        self.hide()


class Window4(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("bankCore version(2.5)")
        self.setGeometry(200, 200, 600, 600)



class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("bankCore version(2.5)")
        self.setGeometry(200, 200, 600, 600)

        self.txt = QtWidgets.QTextBrowser(self)
        self.textbrowser(self.txt, "Welcome to bankCore!", 20, 125, 100, 350, 50)

        self.logButton = QPushButton(self)
        self.cbutton(self.logButton, "Log In", 200, 200, 200, 50, self.loginWindow)

        self.signButton = QtWidgets.QPushButton(self)
        self.cbutton(self.signButton, "Sign In", 200, 275, 200, 50, self.signWindow)

        self.aboutButton = QtWidgets.QPushButton(self)
        self.cbutton(self.aboutButton, "About bankCore", 200, 350, 200, 50, self.aboutWindow)

        self.exitButton = QtWidgets.QPushButton(self)
        self.cbutton(self.exitButton, "Exit", 200, 425, 200, 50, self.exitWindow)

        self.show()
    
    def loginWindow(self):
        self.w = Window2()
        self.w.show()
        self.hide()

    def signWindow(self):
        self.s = Window3()
        self.s.show()
        self.hide()

    def aboutWindow(self):
        self.a = Window4()
        self.a.show()
        self.hide()

    
    def exitWindow(self):
        self.close() # I do NOT know if that is the solution
        # the code is terminating due to closure of the window

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