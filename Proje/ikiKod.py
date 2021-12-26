
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import sqlite3

class Ui_Form(object):
   
    def add(self):
        name = self.textEdit.toPlainText()
        score = self.textEdit_2.toPlainText()
        velocityFps = self.textEdit_3.toPlainText()

        db = sqlite3.connect("snake.db")

        db.execute(""" INSERT INTO puan(name, score, velocityFps) VALUES(?,?,?) """,(name, score, velocityFps))
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
                db.execute(""" DELETE FROM puan WHERE name = ? AND score = ? AND velocityFps = ?""",(name, score, velocityFps))
                db.commit()
                self.load()
                
############################################################################ 


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import sqlite3

class Ui_Form(object):
   
    def add(self):
        enemyTankHealth = self.textEdit.toPlainText()
        ourTankHealth = self.textEdit_2.toPlainText()
        power = self.textEdit_3.toPlainText()
        enemyDamage = self.textEdit_4.toPlainText()
        playerDamage = self.textEdit_5.toPlainText()

        db = sqlite3.connect("tank.db")

        db.execute(""" INSERT INTO tank1(enemyTankHealth, ourTankHealth, power, enemyDamage, playerDamage) VALUES(?,?,?,?,?) """,(enemyTankHealth, ourTankHealth, power, enemyDamage, playerDamage))
        db.commit()

        self.load()
    
    
    def load(self):
        db = sqlite3.connect("tank.db")
        sql = """ SELECT * FROM tank1 """
        result = db.execute(sql)
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
    
    def delete(self):
        db = sqlite3.connect("snake.db")
        sql = """ SELECT * FROM tank1 """
        result = db.execute(sql)

        for row in enumerate(result):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                enemyTankHealth = data[0]
                ourTankHealth = data[1]
                power = data[2]
                enemyDamage = data[3]
                playerDamage = data[4]
             
                db.execute(""" DELETE FROM tank1 WHERE enemyTankHealth = ? AND ourTankHealth = ? AND power = ? AND enemyDamage = ? AND playerDamage = ?""",(enemyTankHealth, ourTankHealth, power, enemyDamage, playerDamage))
                db.commit()
                self.load()
             