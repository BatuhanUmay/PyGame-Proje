# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from form import Ui_Form
import sqlite3


class Ui_FormLogin(object):

    def login_check(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        db = sqlite3.connect("login.db")

        result = db.execute(""" SELECT * FROM giris WHERE username = ? AND password = ? """, (username, password))

        if(len(result.fetchall()) > 0):
            print(username," adlı kullanıcı database de bulundu!")

            self.mainwindow = QtWidgets.QMainWindow()
            self.ui = Ui_Form()
            self.ui.setupUi(self.mainwindow)
            self.mainwindow.show()

        else:
            print(username," adlı kullanıcı database de bulunamadı!")



    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(560, 390)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 561, 391))
        self.frame.setStyleSheet("QFrame{\n"
"background-color: rgb(0, 0, 0);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(90, 120, 81, 16))
        self.label.setStyleSheet("color: rgb(172, 255, 239);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(160, 120, 251, 31))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"border:2px solid rgb(0, 60, 180);\n"
"color: gray;\n"
"border-radius:10px;\n"
"background:transparent;\n"
"}")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(230, 30, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 180, 251, 31))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"border:2px solid rgb(0, 60, 180);\n"
"color: gray;\n"
"border-radius:10px;\n"
"background:transparent;\n"
" }\n"
"")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 290, 101, 41))
        self.pushButton_2.setStyleSheet("QPushButton{border: 2px solid rgb(0, 139, 0);\n"
"border-radius:10px;\n"
"color: gray;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: rgb(85, 170, 0);\n"
"\n"
"    color: rgb(0, 67, 0);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.login_check)

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(220, 260, 141, 16))
        self.label_2.setStyleSheet("color:gray;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(160, 220, 21, 21))
        self.toolButton.setStyleSheet("QToolButton{\n"
"    border-radius:5px;\n"
"    border: 1px solid rgb(0, 60, 180);\n"
"}")
        self.toolButton.setText("")
        self.toolButton.setObjectName("toolButton")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(190, 220, 81, 20))
        self.label_4.setStyleSheet("color:gray;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Username:"))
        self.label_3.setText(_translate("Form", "Log In"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Pasword:"))
        self.pushButton_2.setText(_translate("Form", "Login"))
        self.label_2.setText(_translate("Form", "Forget Password?"))
        self.label_4.setText(_translate("Form", "Remember Me?"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_FormLogin()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
