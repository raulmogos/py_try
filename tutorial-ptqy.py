# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(191, 258)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.slider0 = QtWidgets.QSlider(self.centralWidget)
        self.slider0.setGeometry(QtCore.QRect(20, 30, 22, 160))
        self.slider0.setMaximum(127)
        self.slider0.setOrientation(QtCore.Qt.Vertical)
        self.slider0.setObjectName("slider0")
        self.slider1 = QtWidgets.QSlider(self.centralWidget)
        self.slider1.setGeometry(QtCore.QRect(60, 30, 22, 160))
        self.slider1.setMaximum(127)
        self.slider1.setOrientation(QtCore.Qt.Vertical)
        self.slider1.setObjectName("slider1")
        self.slider2 = QtWidgets.QSlider(self.centralWidget)
        self.slider2.setGeometry(QtCore.QRect(100, 30, 22, 160))
        self.slider2.setMaximum(127)
        self.slider2.setOrientation(QtCore.Qt.Vertical)
        self.slider2.setObjectName("slider2")
        self.slider3 = QtWidgets.QSlider(self.centralWidget)
        self.slider3.setGeometry(QtCore.QRect(140, 30, 22, 160))
        self.slider3.setMaximum(127)
        self.slider3.setOrientation(QtCore.Qt.Vertical)
        self.slider3.setObjectName("slider3")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 191, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
