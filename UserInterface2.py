from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QApplication

from Ui_form2 import Ui_Form

import sys
import os
import sqlite3 as sql

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.formYukle()
        self.ui.tamamButton.clicked.connect(quit)
        

    def formYukle(self):
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setHorizontalHeaderLabels(["İSİM","SOYİSİM"])
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)


        db = sql.connect("Cekilis.db")
        cur = db.cursor()
        ozeldurumyoksorgu = "SELECT * FROM Basvuranlar WHERE ozeldurumyok = 1 ORDER BY RANDOM() LIMIT 13"
        sehityakiniSorgu = "SELECT * FROM Basvuranlar WHERE sehityakini = 1 ORDER BY RANDOM() LIMIT 3"
        emekliSorgu = "SELECT * FROM Basvuranlar WHERE emekli = 1 ORDER BY RANDOM() LIMIT 2"
        engeldurumuSorgu = "SELECT * FROM Basvuranlar WHERE engeldurumu = 1 ORDER BY RANDOM() LIMIT 2"

        list = [ozeldurumyoksorgu, sehityakiniSorgu, emekliSorgu, engeldurumuSorgu]
        kazananlarList = []

        for i in list:
            cur.execute(i)
            sorguSonucu = cur.fetchall()
            kazananlarList.extend(sorguSonucu)
            print("Sorgu : ", i)
            

        for row in kazananlarList:
            isim = row[0]
            soyisim = row[1]



            self.ui.tableWidget.insertRow(0)
            self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(isim))
            self.ui.tableWidget.setItem(0, 1, QTableWidgetItem(soyisim))


        db.close()

    def quit():
        QApplication.quit()
        print("Program sonlandirildi..")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

