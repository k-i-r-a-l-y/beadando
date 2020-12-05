# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledASWtDK.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import foglal as f
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt,QDate,QTime,QDateTime)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *
from tkinter import *


class Ui_MainWindow(object):
    foglalasok = []

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(558, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 255, 127);")
        MainWindow.setIconSize(QSize(24, 30))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 561, 31))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 70, 47, 13))
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(12)
        self.label_5.setFont(font1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 70, 47, 13))
        self.label_2.setFont(font1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(400, 70, 61, 16))
        self.label_4.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(510, 70, 47, 13))
        self.label_3.setFont(font1)
        self.btn_kereses = QPushButton(self.centralwidget)
        self.btn_kereses.setObjectName(u"btn_kereses")
        self.btn_kereses.setGeometry(QRect(160, 120, 241, 41))
        self.btn_kereses.setFont(font1)
        self.btn_kereses.setStyleSheet(u"background-color:rgb(85, 170, 255);")
        self.hat = QPushButton(self.centralwidget)
        self.hat.setObjectName(u"hat")
        self.hat.setGeometry(QRect(240, 330, 61, 131))
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setStrikeOut(False)
        self.hat.setFont(font2)
        self.hat.setFocusPolicy(Qt.StrongFocus)
        self.hat.setAutoFillBackground(False)
        self.hat.setInputMethodHints(Qt.ImhNone)
        icon = QIcon()
        icon.addFile(u"hatos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hat.setIcon(icon)
        self.hat.setIconSize(QSize(130, 130))
        self.hat.setCheckable(False)
        self.harom = QPushButton(self.centralwidget)
        self.harom.setObjectName(u"harom")
        self.harom.setGeometry(QRect(250, 210, 61, 51))
        font3 = QFont()
        font3.setFamily(u"Times New Roman")
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setWeight(50)
        self.harom.setFont(font3)
        icon1 = QIcon()
        icon1.addFile(u"harmas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.harom.setIcon(icon1)
        self.harom.setIconSize(QSize(60, 60))
        self.harom.setCheckable(False)
        self.bejarat = QToolButton(self.centralwidget)
        self.bejarat.setObjectName(u"bejarat")
        self.bejarat.setEnabled(False)
        self.bejarat.setGeometry(QRect(70, 270, 71, 21))
        self.bejarat.setFont(font1)
        self.bejarat.setStyleSheet(u"background-color: rgb(194, 200, 193);")
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(90, 210, 381, 251))
        self.listView.setFont(font1)
        self.listView.setAutoFillBackground(False)
        self.listView.setStyleSheet(u"background-color: rgb(170, 170, 127)")
        self.ketto = QPushButton(self.centralwidget)
        self.ketto.setObjectName(u"ketto")
        self.ketto.setEnabled(True)
        self.ketto.setGeometry(QRect(380, 210, 61, 41))
        font4 = QFont()
        font4.setFamily(u"Times New Roman")
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setUnderline(False)
        font4.setWeight(50)
        font4.setStrikeOut(False)
        self.ketto.setFont(font4)
        self.ketto.setFocusPolicy(Qt.StrongFocus)
        self.ketto.setInputMethodHints(Qt.ImhNone)
        icon2 = QIcon()
        icon2.addFile(u"kettes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ketto.setIcon(icon2)
        self.ketto.setIconSize(QSize(60, 60))
        self.ketto.setCheckable(False)
        self.egy = QPushButton(self.centralwidget)
        self.egy.setObjectName(u"egy")
        self.egy.setGeometry(QRect(120, 210, 61, 41))
        self.egy.setFont(font2)
        self.egy.setFocusPolicy(Qt.StrongFocus)
        self.egy.setStyleSheet(u"")
        self.egy.setInputMethodHints(Qt.ImhNone)
        self.egy.setIcon(icon2)
        self.egy.setIconSize(QSize(60, 60))
        self.egy.setCheckable(False)
        self.konyha = QToolButton(self.centralwidget)
        self.konyha.setObjectName(u"konyha")
        self.konyha.setEnabled(False)
        self.konyha.setGeometry(QRect(340, 310, 131, 151))
        self.konyha.setFont(font1)
        self.konyha.setFocusPolicy(Qt.StrongFocus)
        self.konyha.setStyleSheet(u"background-color: rgb(194, 200, 193);")
        self.konyha.setInputMethodHints(Qt.ImhNone)
        self.konyha.setCheckable(True)
        self.ot = QPushButton(self.centralwidget)
        self.ot.setObjectName(u"ot")
        self.ot.setGeometry(QRect(130, 390, 61, 71))
        font5 = QFont()
        font5.setFamily(u"Times New Roman")
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.ot.setFont(font5)
        self.ot.setFocusPolicy(Qt.StrongFocus)
        self.ot.setInputMethodHints(Qt.ImhNone)
        icon3 = QIcon()
        icon3.addFile(u"otos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ot.setIcon(icon3)
        self.ot.setIconSize(QSize(70, 70))
        self.ot.setCheckable(False)
        self.negy = QPushButton(self.centralwidget)
        self.negy.setObjectName(u"negy")
        self.negy.setGeometry(QRect(130, 310, 61, 51))
        self.negy.setFont(font3)
        self.negy.setFocusPolicy(Qt.StrongFocus)
        self.negy.setInputMethodHints(Qt.ImhNone)
        icon4 = QIcon()
        icon4.addFile(u"negyes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.negy.setIcon(icon4)
        self.negy.setIconSize(QSize(60, 60))
        self.negy.setCheckable(False)
        self.btn_foglalas = QPushButton(self.centralwidget)
        self.btn_foglalas.setObjectName(u"btn_foglalas")
        self.btn_foglalas.setGeometry(QRect(180, 490, 201, 51))
        self.btn_foglalas.setFont(font1)
        self.btn_foglalas.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.in_fo = QSpinBox(self.centralwidget)
        self.in_fo.setObjectName(u"in_fo")
        self.in_fo.setGeometry(QRect(60, 60, 61, 31))
        self.in_fo.setFont(font1)
        self.in_fo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.in_fo.setMinimum(1)
        self.in_fo.setMaximum(12)
        self.in_datum = QDateEdit(self.centralwidget)
        self.in_datum.setObjectName(u"in_datum")
        self.in_datum.setGeometry(QRect(180, 60, 121, 31))
        self.in_datum.setFont(font1)
        self.in_datum.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.in_datum.setDate(QDate.currentDate())
        self.in_tol = QTimeEdit(self.centralwidget)
        self.in_tol.setObjectName(u"in_tol")
        self.in_tol.setGeometry(QRect(320, 60, 71, 31))
        self.in_tol.setFont(font1)
        self.in_tol.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.in_tol.setDateTime(QDateTime(QDate(2020, 12, 8), QTime(8, 0, 0)))
        self.in_ig = QTimeEdit(self.centralwidget)
        self.in_ig.setObjectName(u"in_ig")
        self.in_ig.setGeometry(QRect(430, 60, 71, 31))
        self.in_ig.setFont(font1)
        self.in_ig.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.in_ig.setDateTime(QDateTime(QDate(2020, 12, 8), QTime(9, 0, 0)))
        self.egyfoglalt = QPushButton(self.centralwidget)
        self.egyfoglalt.setObjectName(u"egyfoglalt")
        self.egyfoglalt.setGeometry(QRect(120, 210, 61, 41))
        self.egyfoglalt.setStyleSheet(u"color: rgb(255, 0, 0);\n"
                                      "background-color: rgb(255, 255, 255);")
        self.kettofoglalt = QPushButton(self.centralwidget)
        self.kettofoglalt.setObjectName(u"kettofoglalt")
        self.kettofoglalt.setGeometry(QRect(380, 210, 61, 41))
        self.kettofoglalt.setStyleSheet(u"color: rgb(255, 0, 0);\n"
                                        "background-color: rgb(255, 255, 255);")
        self.haromfoglalt = QPushButton(self.centralwidget)
        self.haromfoglalt.setObjectName(u"haromfoglalt")
        self.haromfoglalt.setGeometry(QRect(250, 210, 61, 51))
        self.haromfoglalt.setStyleSheet(u"color: rgb(255, 0, 0);\n"
                                        "background-color: rgb(255, 255, 255);")
        self.negyfoglalt = QPushButton(self.centralwidget)
        self.negyfoglalt.setObjectName(u"negyfoglalt")
        self.negyfoglalt.setGeometry(QRect(130, 310, 61, 51))
        self.negyfoglalt.setStyleSheet(u"color: rgb(255, 0, 0);\n"
                                       "background-color: rgb(255, 255, 255);")
        self.otfoglalt = QPushButton(self.centralwidget)
        self.otfoglalt.setObjectName(u"otfoglalt")
        self.otfoglalt.setGeometry(QRect(130, 390, 61, 71))
        self.otfoglalt.setStyleSheet(u"color: rgb(255, 0, 0);\n"
                                     "background-color: rgb(255, 255, 255);")
        self.hatfoglalt = QPushButton(self.centralwidget)
        self.hatfoglalt.setObjectName(u"hatfoglalt")
        self.hatfoglalt.setGeometry(QRect(240, 330, 61, 131))
        self.hatfoglalt.setStyleSheet(u"color: rgb(255, 0, 0);\n"
                                      "background-color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.listView.raise_()
        self.label.raise_()
        self.label_5.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.btn_kereses.raise_()
        self.hat.raise_()
        self.harom.raise_()
        self.bejarat.raise_()
        self.ketto.raise_()
        self.egy.raise_()
        self.konyha.raise_()
        self.ot.raise_()
        self.negy.raise_()
        self.btn_foglalas.raise_()
        self.in_fo.raise_()
        self.in_datum.raise_()
        self.in_tol.raise_()
        self.in_ig.raise_()
        self.egyfoglalt.raise_()
        self.kettofoglalt.raise_()
        self.haromfoglalt.raise_()
        self.negyfoglalt.raise_()
        self.otfoglalt.raise_()
        self.hatfoglalt.raise_()
        self.egy.setHidden(True)
        self.ketto.setHidden(True)
        self.harom.setHidden(True)
        self.negy.setHidden(True)
        self.ot.setHidden(True)
        self.hat.setHidden(True)
        self.listView.setHidden(True)
        self.bejarat.setHidden(True)
        self.konyha.setHidden(True)
        self.btn_foglalas.setHidden(True)
        self.egyfoglalt.setHidden(True)
        self.kettofoglalt.setHidden(True)
        self.haromfoglalt.setHidden(True)
        self.negyfoglalt.setHidden(True)
        self.otfoglalt.setHidden(True)
        self.hatfoglalt.setHidden(True)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 578, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        self.btn_kereses.clicked.connect(self.kereses)
        self.btn_foglalas.clicked.connect(self.lefoglal)
        self.egy.clicked.connect(self.egyes)
        self.ketto.clicked.connect(self.kettes)
        self.harom.clicked.connect(self.harmas)
        self.negy.clicked.connect(self.negyes)
        self.ot.clicked.connect(self.otos)
        self.hat.clicked.connect(self.hatos)

    # setupUi

    def kereses(self):
        tol = self.in_tol.text()
        ig = self.in_ig.text()
        oratol = tol.split(':')
        oraig = ig.split(':')
        if (int(oratol[0])>int(oraig[0])) or (int(oratol[0])==int(oraig[0]) and (int(oratol[1])>=int(oraig[1]))):
            msg = QMessageBox()
            msg.setWindowTitle("Hiba!")
            msg.setText("Rossz időkorlátot adott meg!")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Cancel)
            msg.exec_()
        else:
            self.egy.setHidden(False)
            self.ketto.setHidden(False)
            self.harom.setHidden(False)
            self.negy.setHidden(False)
            self.ot.setHidden(False)
            self.hat.setHidden(False)
            self.listView.setHidden(False)
            self.bejarat.setHidden(False)
            self.konyha.setHidden(False)

        if (self.in_fo.text() == '1') or (self.in_fo.text() == '2'):
            self.id = '1,2'
            self.egy.setEnabled(True)
            self.ketto.setEnabled(True)
            self.harom.setEnabled(False)
            self.negy.setEnabled(False)
            self.ot.setEnabled(False)
            self.hat.setEnabled(False)

        if self.in_fo.text() == '3':
            self.id='3,4'
            self.egy.setEnabled(False)
            self.ketto.setEnabled(False)
            self.harom.setEnabled(True)
            self.negy.setEnabled(True)
            self.ot.setEnabled(False)
            self.hat.setEnabled(False)

        if self.in_fo.text() == '4':
            self.id = '4,5'
            self.egy.setEnabled(False)
            self.ketto.setEnabled(False)
            self.harom.setEnabled(False)
            self.negy.setEnabled(True)
            self.ot.setEnabled(True)
            self.hat.setEnabled(False)

        if self.in_fo.text() == '5':
            self.id = '5,6'
            self.egy.setEnabled(False)
            self.ketto.setEnabled(False)
            self.harom.setEnabled(False)
            self.negy.setEnabled(False)
            self.ot.setEnabled(True)
            self.hat.setEnabled(True)

        in_fo=int(self.in_fo.text())
        if in_fo >= 6:
            self.id = '6,6'
            self.egy.setEnabled(False)
            self.ketto.setEnabled(False)
            self.harom.setEnabled(False)
            self.negy.setEnabled(False)
            self.ot.setEnabled(False)
            self.hat.setEnabled(True)

        datum=self.in_datum.text()
        tol=self.in_tol.text()
        ig=self.in_ig.text()
        id=self.id.split(',')
        oratol=tol.split(':')
        oraig=ig.split(':')
        self.egyfoglalt.setHidden(True)
        self.kettofoglalt.setHidden(True)
        self.haromfoglalt.setHidden(True)
        self.negyfoglalt.setHidden(True)
        self.otfoglalt.setHidden(True)
        self.hatfoglalt.setHidden(True)
        k = open("adatbazis.txt", "r")
        for sor in k:
            adat = sor.rstrip().split(",")
            mettol=adat[2].split(":")
            meddig=adat[3].split(':')
            if (datum==adat[1]) and (id[0]==adat[4] or id[1]==adat[4]) and (int(oratol[0]) < int(meddig[0])) or ((int(oratol[0]) == int(meddig[0]))and (int(meddig[1])>int(oratol[1]))):
                if (((int(oraig[0])>int(mettol[0])) or ((int(oraig[1])>int(mettol[1])))) or ((int(meddig[0])<int(oratol[0])))):
                    if adat[4] == '1':
                        self.egyfoglalt.setHidden(False)
                        self.egy.setEnabled(False)
                        self.egyfoglalt.setEnabled(False)
                    if adat[4] == '2':
                        self.kettofoglalt.setHidden(False)
                        self.ketto.setEnabled(False)
                        self.kettofoglalt.setEnabled(False)
                    if adat[4] == '3':
                        self.haromfoglalt.setHidden(False)
                        self.harom.setEnabled(False)
                        self.haromfoglalt.setEnabled(False)
                    if adat[4] == '4':
                        self.negyfoglalt.setHidden(False)
                        self.negy.setEnabled(False)
                        self.negyfoglalt.setEnabled(False)
                    if adat[4] == '5':
                        self.otfoglalt.setHidden(False)
                        self.ot.setEnabled(False)
                        self.otfoglalt.setEnabled(False)
                    if adat[4] == '6':
                        self.hatfoglalt.setHidden(False)
                        self.hat.setEnabled(False)
                        self.hatfoglalt.setEnabled(False)

    def egyes(self):
        self.id = '1'
        self.btn_foglalas.setHidden(False)
    def kettes(self):
        self.id='2'
        self.btn_foglalas.setHidden(False)
    def harmas(self):
        self.id='3'
        self.btn_foglalas.setHidden(False)
    def negyes(self):
        self.id='4'
        self.btn_foglalas.setHidden(False)
    def otos(self):
        self.id='5'
        self.btn_foglalas.setHidden(False)
    def hatos(self):
        self.id='6'
        self.btn_foglalas.setHidden(False)

    def lefoglal(self):
        if len(self.id)==3:
            msg = QMessageBox()
            msg.setWindowTitle("Hiba!")
            msg.setText("Válasszon ki egy asztalt!")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
        else:
            try:
                foglal = f.Foglalas(self.in_fo.text(), self.in_datum.text(), self.in_tol.text(), self.in_ig.text(),self.id)
                self.foglalasok.append(foglal)
                msg = QMessageBox()
                msg.setWindowTitle("Gratulálunk!")
                msg.setText(f"Ön sikeresen lefoglalta a(z) {self.id}-as asztalt!\nDátum: {self.in_datum.text()}\nVárjuk "
                            f"{self.in_tol.text()} órától az éttermünkben.")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
            except:
                pass
        self.ment_fajlba()

    def ment_fajlba(self):
        k = open("adatbazis.txt", "w")
        for foglal in self.foglalasok:
            print(foglal.__str__(), file=k)
        k.close()

    def olvas_fajlbol(self):
        try:
            k = open("adatbazis.txt", "r")
            for sor in k:
                adat = sor.rstrip().split(",")
                foglal = f.Foglalas(adat[0], adat[1], adat[2], adat[3], adat[4])
                self.foglalasok.append(foglal)
            k.close()
        except:
            pass

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"\u00dcdv\u00f6zli a .... \u00e9tterem asztalfoglal\u00e1si rendszere!",
                                                      None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"F\u0151:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"D\u00e1tum:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"-t\u00f3l", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"-ig", None))
        self.btn_kereses.setText(QCoreApplication.translate("MainWindow", u"Asztal keres\u00e9se", None))
        self.bejarat.setText(QCoreApplication.translate("MainWindow", u"Bej\u00e1rat >", None))
        self.konyha.setText(QCoreApplication.translate("MainWindow", u"Konyha", None))
        self.btn_foglalas.setText(QCoreApplication.translate("MainWindow", u"Lefoglalom!", None))
        self.egyfoglalt.setText(QCoreApplication.translate("MainWindow", u"Foglalt", None))
        self.kettofoglalt.setText(QCoreApplication.translate("MainWindow", u"Foglalt", None))
        self.haromfoglalt.setText(QCoreApplication.translate("MainWindow", u"Foglalt", None))
        self.negyfoglalt.setText(QCoreApplication.translate("MainWindow", u"Foglalt", None))
        self.otfoglalt.setText(QCoreApplication.translate("MainWindow", u"Foglalt", None))
        self.hatfoglalt.setText(QCoreApplication.translate("MainWindow", u"Foglalt", None))
    # retranslateUi


import sys

app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.olvas_fajlbol()
MainWindow.show()
sys.exit(app.exec_())
