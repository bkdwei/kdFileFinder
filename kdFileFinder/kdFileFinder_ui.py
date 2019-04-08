# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/bkd/git/kdFileFinder\kdFileFinder\kdFileFinder.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_kdFileFinder(object):
    def setupUi(self, kdFileFinder):
        kdFileFinder.setObjectName("kdFileFinder")
        kdFileFinder.resize(646, 583)
        self.centralwidget = QtWidgets.QWidget(kdFileFinder)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.le_path = QtWidgets.QLineEdit(self.centralwidget)
        self.le_path.setObjectName("le_path")
        self.gridLayout.addWidget(self.le_path, 0, 0, 1, 2)
        self.lb_sidebar = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_sidebar.setFont(font)
        self.lb_sidebar.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lb_sidebar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lb_sidebar.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.lb_sidebar.setObjectName("lb_sidebar")
        self.gridLayout.addWidget(self.lb_sidebar, 1, 0, 1, 1)
        self.lw_main = QtWidgets.QListView(self.centralwidget)
        self.lw_main.setResizeMode(QtWidgets.QListView.Adjust)
        self.lw_main.setObjectName("lw_main")
        self.gridLayout.addWidget(self.lw_main, 1, 1, 2, 1)
        self.lw_sidebar = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lw_sidebar.sizePolicy().hasHeightForWidth())
        self.lw_sidebar.setSizePolicy(sizePolicy)
        self.lw_sidebar.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lw_sidebar.setObjectName("lw_sidebar")
        self.gridLayout.addWidget(self.lw_sidebar, 2, 0, 1, 1)
        kdFileFinder.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(kdFileFinder)
        self.statusbar.setObjectName("statusbar")
        kdFileFinder.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(kdFileFinder)
        self.toolBar.setObjectName("toolBar")
        kdFileFinder.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(kdFileFinder)
        QtCore.QMetaObject.connectSlotsByName(kdFileFinder)

    def retranslateUi(self, kdFileFinder):
        _translate = QtCore.QCoreApplication.translate
        kdFileFinder.setWindowTitle(_translate("kdFileFinder", "kdFileFinder"))
        self.le_path.setText(_translate("kdFileFinder", "/tmp"))
        self.lb_sidebar.setText(_translate("kdFileFinder", "收藏夹"))
        self.toolBar.setWindowTitle(_translate("kdFileFinder", "toolBar"))


