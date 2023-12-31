# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anaekran.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AnaEkran(object):
    def setupUi(self, AnaEkran):
        AnaEkran.setObjectName("AnaEkran")
        AnaEkran.resize(800, 600)
        self.AnaForm = QtWidgets.QWidget(AnaEkran)
        self.AnaForm.setObjectName("AnaForm")
        self.tableWidget = QtWidgets.QTableWidget(self.AnaForm)
        self.tableWidget.setGeometry(QtCore.QRect(30, 20, 741, 521))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        AnaEkran.setCentralWidget(self.AnaForm)
        self.menubar = QtWidgets.QMenuBar(AnaEkran)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuKitap_Listesi = QtWidgets.QMenu(self.menubar)
        self.menuKitap_Listesi.setObjectName("menuKitap_Listesi")
        self.menuKitap_Ekle = QtWidgets.QMenu(self.menubar)
        self.menuKitap_Ekle.setObjectName("menuKitap_Ekle")
        self.menuKitap_Guncelle = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(5)
        self.menuKitap_Guncelle.setFont(font)
        self.menuKitap_Guncelle.setObjectName("menuKitap_Guncelle")
        self.menuSil = QtWidgets.QMenu(self.menubar)
        self.menuSil.setObjectName("menuSil")
        self.menu_Cikis = QtWidgets.QMenu(self.menubar)
        self.menu_Cikis.setObjectName("menu_Cikis")
        AnaEkran.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AnaEkran)
        self.statusbar.setObjectName("statusbar")
        AnaEkran.setStatusBar(self.statusbar)
        self.actionKitapEkle = QtWidgets.QAction(AnaEkran)
        self.actionKitapEkle.setObjectName("actionKitapEkle")
        self.actionKitapEkleme = QtWidgets.QAction(AnaEkran)
        self.actionKitapEkleme.setObjectName("actionKitapEkleme")
        self.action_cikis = QtWidgets.QAction(AnaEkran)
        self.action_cikis.setObjectName("action_cikis")
        self.actionKitap_Guncelleme = QtWidgets.QAction(AnaEkran)
        self.actionKitap_Guncelleme.setObjectName("actionKitap_Guncelleme")
        self.actionKitap_Silme = QtWidgets.QAction(AnaEkran)
        self.actionKitap_Silme.setObjectName("actionKitap_Silme")
        self.actionKitap_Listeleme = QtWidgets.QAction(AnaEkran)
        self.actionKitap_Listeleme.setObjectName("actionKitap_Listeleme")
        self.menuKitap_Listesi.addAction(self.actionKitap_Listeleme)
        self.menuKitap_Ekle.addAction(self.actionKitapEkleme)
        self.menuKitap_Guncelle.addAction(self.actionKitap_Guncelleme)
        self.menuSil.addAction(self.actionKitap_Silme)
        self.menubar.addAction(self.menuKitap_Listesi.menuAction())
        self.menubar.addAction(self.menuKitap_Ekle.menuAction())
        self.menubar.addAction(self.menuKitap_Guncelle.menuAction())
        self.menubar.addAction(self.menuSil.menuAction())
        self.menubar.addAction(self.menu_Cikis.menuAction())

        self.retranslateUi(AnaEkran)
        self.action_cikis.triggered['bool'].connect(AnaEkran.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(AnaEkran)

    def retranslateUi(self, AnaEkran):
        _translate = QtCore.QCoreApplication.translate
        AnaEkran.setWindowTitle(_translate("AnaEkran", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AnaEkran", "Kitap_İd"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AnaEkran", "Kitap Adı"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("AnaEkran", "Okunma Durumu"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("AnaEkran", "Kitap Yazarı"))
        self.menuKitap_Listesi.setTitle(_translate("AnaEkran", "Kitap Listesi"))
        self.menuKitap_Ekle.setTitle(_translate("AnaEkran", "Kitap Ekle"))
        self.menuKitap_Guncelle.setTitle(_translate("AnaEkran", "Kitap Güncelle"))
        self.menuSil.setTitle(_translate("AnaEkran", "Sil"))
        self.menu_Cikis.setTitle(_translate("AnaEkran", "Çıkış"))
        self.actionKitapEkle.setText(_translate("AnaEkran", "KitapEkle"))
        self.actionKitapEkleme.setText(_translate("AnaEkran", "KitapEkleme"))
        self.action_cikis.setText(_translate("AnaEkran", "Çıkış"))
        self.actionKitap_Guncelleme.setText(_translate("AnaEkran", "Kitap Guncelleme"))
        self.actionKitap_Silme.setText(_translate("AnaEkran", "Kitap Silme"))
        self.actionKitap_Listeleme.setText(_translate("AnaEkran", "Kitap Listeleme"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AnaEkran = QtWidgets.QMainWindow()
    ui = Ui_AnaEkran()
    ui.setupUi(AnaEkran)
    AnaEkran.show()
    sys.exit(app.exec_())
