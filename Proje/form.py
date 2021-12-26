# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from snakeinfo import Ui_Form_snake
from tankinfo import Ui_Form_tank

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(690, 518)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 691, 101))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(160, 30, 371, 51))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(0, 100, 701, 441))
        self.frame_2.setStyleSheet("\n"
"background-color: rgb(170, 255, 255);\n"
"\n"
"\n"
"QPushButton{ \n"
"border-radius: 25px;\n"
" border:3px solid #005500;\n"
"}\n"
"\n"
"QPushButton::hover{ \n"
"border-radius: 25px;\n"
" border:3px solid #005500;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(10, 70, 161, 41))
        self.label.setStyleSheet("color: rgb(38, 76, 56);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 211, 41))
        self.label_2.setStyleSheet("color: rgb(38, 76, 56);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 310, 211, 41))
        self.label_3.setStyleSheet("color: rgb(38, 76, 56);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(20, 230, 121, 41))
        self.label_4.setStyleSheet("color: rgb(38, 76, 56);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(360, 50, 191, 61))
        self.pushButton.setStyleSheet("QPushButton{ \n"
"border-radius: 25px;\n"
" border:3px solid #55007f;\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"background-color:#aaaaff ;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.snakeOpen)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 130, 191, 61))
        self.pushButton_2.setStyleSheet("QPushButton{ \n"
"border-radius: 25px;\n"
" border:3px solid #55007f;\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"background-color:#aaaaff ;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.snakeInfo)


        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 210, 191, 61))
        self.pushButton_3.setStyleSheet("QPushButton{ \n"
"border-radius: 25px;\n"
" border:3px solid #005500;\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"background-color : lightgreen;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.tankOpen)

        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 290, 191, 61))
        self.pushButton_4.setStyleSheet("QPushButton{ \n"
"border-radius: 25px;\n"
" border:3px solid #005500;\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"background-color : lightgreen;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.tankInfo)

        self.toolButton = QtWidgets.QToolButton(self.frame_2)
        self.toolButton.setGeometry(QtCore.QRect(310, 70, 31, 31))
        self.toolButton.setStyleSheet("background-image: url(:/newPrefix/slitherButton.jpg);\n"
"background-repeat:none;")
        self.toolButton.setText("")
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.frame_2)
        self.toolButton_2.setGeometry(QtCore.QRect(310, 150, 31, 31))
        self.toolButton_2.setStyleSheet("background-image: url(:/newPrefix/slitherButton.jpg);\n"
"background-repeat:none;")
        self.toolButton_2.setText("")
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.frame_2)
        self.toolButton_3.setGeometry(QtCore.QRect(310, 220, 31, 31))
        self.toolButton_3.setStyleSheet("background-image: url(:/newPrefix/tankButton.jpg);\n"
"background-repeat:none;")
        self.toolButton_3.setText("")
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(self.frame_2)
        self.toolButton_4.setGeometry(QtCore.QRect(310, 300, 31, 31))
        self.toolButton_4.setStyleSheet("background-image: url(:/newPrefix/tankButton.jpg);\n"
"background-repeat:none;")
        self.toolButton_4.setText("")
        self.toolButton_4.setObjectName("toolButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Game Control Menu</span></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Snake Game</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Snake Game Database</span></p><p><br/></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Tank Game Database</span></p><p><br/></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Tank Game </span></p><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Start Snake Game"))
        self.pushButton_2.setText(_translate("Form", "Show Snake Game Infos"))
        self.pushButton_3.setText(_translate("Form", "Start Tank Game"))
        self.pushButton_4.setText(_translate("Form", "Show Tank Game Infos"))

    def snakeOpen(self):
        import snakeGame

    def tankOpen(self):
        import tankGame

    def snakeInfo(self):
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Form_snake()
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()


    def tankInfo(self):
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Form_tank()
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()


import resimler


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())