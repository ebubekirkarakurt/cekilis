from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QApplication

from Ui_form import Ui_MainWindow

import sys 
import os
import sqlite3 as sql 

os.system('python Connection.py')
os.system('python CreateTable.py')


global isim, soyisim, numara, sehityakini, emekli, engeldurumu, ozeldurumyok

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        self.ui.iptalButton.clicked.connect(quit)
        self.ui.basvurButton.clicked.connect(self.btnKaydetClicked)


    def btnKaydetClicked(self):
        isim = self.ui.isimEdit.text()
        soyisim = self.ui.soyisimEdit.text()
        numara = self.ui.numaraEdit.text()
        
        sehityakini = self.ui.sehitYakini.isChecked()
        engeldurumu = self.ui.engelDurumu.isChecked()
        emekli = self.ui.emekli.isChecked()
        ozeldurumyok = self.ui.ozeldurumyok.isChecked()

        try:
            self.baglanti = sql.connect("Cekilis.db")
            self.c = self.baglanti.cursor()
            self.c.execute("INSERT INTO Basvuranlar (isim, soyisim, numara, sehityakini, emekli, engeldurumu, ozeldurumyok) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (isim, soyisim, numara, sehityakini, emekli, engeldurumu, ozeldurumyok))

            self.baglanti.commit()
            self.c.close()
            self.baglanti.close()

            print("Başarılı", "Başvuranların bilgisi veritabanına kaydedildi.")

        except Exception:
            print("Hata!", "Başvuranların bilgileri kaydedilemedi.")

        self.quit()

    def quit(self):
         QApplication.quit()
         print("Program sonlandirildi..")
         

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())  

app()
