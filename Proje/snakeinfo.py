# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/batu_/OneDrive/Masaüstü/oyunYeni/snakeinfo.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import sqlite3

class Ui_Form_snake(object):

    def add(self):
        name = self.textEdit.toPlainText()
        score = self.textEdit_2.toPlainText()
        velocityFps = self.textEdit_3.toPlainText()

        db = sqlite3.connect("snake.db")

        db.execute(""" INSERT INTO puan(name, score, velocityFps) VALUES(?,?,?) """, (name, score, velocityFps))
        db.commit()

        self.load()


    def load(self):
        db = sqlite3.connect("snake.db")
        sql = """ SELECT * FROM puan """
        result = db.execute(sql)
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))


    def delete(self):
        db = sqlite3.connect("snake.db")
        sql = """ SELECT * FROM puan """
        result = db.execute(sql)

        for row in enumerate(result):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                name = data[0]
                score = data[1]
                velocityFps = data[2]
                db.execute(""" DELETE FROM puan WHERE name = ? AND score = ? AND velocityFps = ?""",
                           (name, score, velocityFps))
                db.commit()
                self.load()


    def updated(self):

        db = sqlite3.connect("snake.db")
        sql = """SELECT * FROM puan"""
        cursor = db.cursor()
        result = cursor.execute(sql)

        y_name = self.textEdit.toPlainText()
        y_score = self.textEdit_2.toPlainText()
        y_velocityFps = self.textEdit_3.toPlainText()

        for row in enumerate(result):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                name = data[0]
                score = data[1]
                velocityFps = data[2]

                cursor.execute('''UPDATE puan SET name = ?, score = ?, velocityFps = ? WHERE name = ? AND score = ? AND velocityFps = ?''', (y_name, int(y_score), int(y_velocityFps), name, score, velocityFps))
                db.commit()
                self.load()


    def Clicked(self):
        db = sqlite3.connect("snake.db")
        sql = """SELECT * FROM puan"""
        cursor = db.cursor()
        result = cursor.execute(sql)
        for row in enumerate(result):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                name = data[0]
                score = data[1]
                velocityFps = data[2]
                self.textEdit.setText(name)
                self.textEdit_2.setText(str(score))
                self.textEdit_3.setText(str(velocityFps))


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(756, 487)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 761, 491))
        self.frame.setStyleSheet("background-color: rgb(208, 208, 208);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 110, 101, 21))
        self.label.setObjectName("label")
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_3.setGeometry(QtCore.QRect(130, 220, 201, 31))
        self.textEdit_3.setStyleSheet("border-radius:10px;\n"
"border: 3px solid #00007f;\n"
"")
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(160, 350, 81, 41))
        self.pushButton.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"border: 3px solid #00007f;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(70, 70, 211);\n"
"border-radius:10px;\n"
"border: 3px solid #4646d3;\n"
"color:white\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add)

        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 350, 81, 41))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"border: 3px solid #00007f;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(32, 98, 0);\n"
"border-radius:10px;\n"
"border: 3px solid #4646d3;\n"
"color:white\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.delete)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 350, 81, 41))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"border: 3px solid #00007f;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#339999;\n"
"border-radius:10px;\n"
"border: 3px solid #4646d3;\n"
"color:white\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.load)

        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 350, 81, 41))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"border: 3px solid #00007f;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(121, 60, 90);\n"
"border-radius:10px;\n"
"border: 3px solid #4646d3;\n"
"color:white\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.updated)

        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(130, 100, 201, 31))
        self.textEdit.setStyleSheet("border-radius:10px;\n"
"border: 3px solid #00007f;\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 101, 21))
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_2.setGeometry(QtCore.QRect(130, 160, 201, 31))
        self.textEdit_2.setStyleSheet("border-radius:10px;\n"
"border: 3px solid #00007f;\n"
"")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 230, 101, 21))
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(390, 80, 351, 171))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        self.tableWidget.clicked.connect(self.Clicked)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Name</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Add"))
        self.pushButton_3.setText(_translate("Form", "Delete"))
        self.pushButton_2.setText(_translate("Form", "Display"))
        self.pushButton_4.setText(_translate("Form", "Update"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Score</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Velocity Fps</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "score"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "velocityFps"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_snake()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())