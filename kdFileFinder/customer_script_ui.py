# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/bkd/git/kdFileFinder\kdFileFinder\customer_script.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(369, 234)
        self.formLayout_2 = QtWidgets.QFormLayout(Dialog)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.formLayout)
        self.le_name = QtWidgets.QLineEdit(Dialog)
        self.le_name.setObjectName("le_name")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_name)
        self.pb_path = QtWidgets.QPushButton(Dialog)
        self.pb_path.setFlat(False)
        self.pb_path.setObjectName("pb_path")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pb_path)
        self.le_path = QtWidgets.QLineEdit(Dialog)
        self.le_path.setObjectName("le_path")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.le_path)
        self.rb_other_filetype = QtWidgets.QRadioButton(Dialog)
        self.rb_other_filetype.setObjectName("rb_other_filetype")
        self.bg_apply_type = QtWidgets.QButtonGroup(Dialog)
        self.bg_apply_type.setObjectName("bg_apply_type")
        self.bg_apply_type.addButton(self.rb_other_filetype)
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.rb_other_filetype)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.le_filetype = QtWidgets.QLineEdit(Dialog)
        self.le_filetype.setObjectName("le_filetype")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.le_filetype)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.buttonBox)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.rb_cur_item = QtWidgets.QRadioButton(Dialog)
        self.rb_cur_item.setChecked(True)
        self.rb_cur_item.setObjectName("rb_cur_item")
        self.bg_apply_type.addButton(self.rb_cur_item)
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.rb_cur_item)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "自定义脚本"))
        self.pb_path.setText(_translate("Dialog", "脚本路径"))
        self.rb_other_filetype.setText(_translate("Dialog", "指定文件类型，如(*.txt;*.pdf)"))
        self.label_2.setText(_translate("Dialog", "文件类型"))
        self.label.setText(_translate("Dialog", "右键名称"))
        self.rb_cur_item.setText(_translate("Dialog", "当前选中项目"))
        self.label_3.setText(_translate("Dialog", "应用于"))


