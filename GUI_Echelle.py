# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Echelle.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class EchelleWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(400, 200)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Photos/icon.png"))
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 353, 243))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.filename_lable = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.filename_lable.setObjectName("filename_lable")
        self.gridLayout_2.addWidget(self.filename_lable, 0, 0, 1, 1)
        self.filename = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.filename.setObjectName("filename")
        self.gridLayout_2.addWidget(self.filename, 0, 1, 1, 3)
        self.longueur = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.longueur.setObjectName("longueur")
        self.gridLayout_2.addWidget(self.longueur, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 2, 1, 1)
        self.largeure = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.largeure.setObjectName("largeure")
        self.gridLayout_2.addWidget(self.largeure, 1, 3, 1, 1)
        self.mesure = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.mesure.setObjectName("mesure")
        self.gridLayout_2.addWidget(self.mesure, 1, 4, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 371, 22))
        self.menubar.setObjectName("menubar")
        self.menumenu = QtWidgets.QMenu(self.menubar)
        self.menumenu.setObjectName("menumenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsauvegarder = QtWidgets.QAction(MainWindow)
        self.actionsauvegarder.setObjectName("actionsauvegarder")
        self.menumenu.addAction(self.actionsauvegarder)
        self.menubar.addAction(self.menumenu.menuAction())

        MainWindow.setWindowFlag(QtCore.Qt.WindowMinMaxButtonsHint, False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Echelle"))
        self.filename_lable.setText(_translate("MainWindow", "Nom fichier:"))
        self.label.setText(_translate("MainWindow", "x"))
        self.mesure.setText(_translate("MainWindow", "mm²"))
        self.menumenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionsauvegarder.setText(_translate("MainWindow", "Sauvegarder"))

