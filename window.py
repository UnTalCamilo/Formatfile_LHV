# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(465, 350)
        MainWindow.setMinimumSize(QtCore.QSize(465, 350))
        MainWindow.setMaximumSize(QtCore.QSize(465, 350))
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ipn_input = QtWidgets.QLineEdit(self.centralwidget)
        self.ipn_input.setEnabled(True)
        self.ipn_input.setGeometry(QtCore.QRect(20, 30, 311, 20))
        self.ipn_input.setReadOnly(True)
        self.ipn_input.setObjectName("ipn_input")
        self.btn_srcipn = QtWidgets.QPushButton(self.centralwidget)
        self.btn_srcipn.setGeometry(QtCore.QRect(360, 30, 75, 23))
        self.btn_srcipn.setObjectName("btn_srcipn")
        self.file_output = QtWidgets.QLineEdit(self.centralwidget)
        self.file_output.setEnabled(False)
        self.file_output.setGeometry(QtCore.QRect(20, 200, 311, 20))
        self.file_output.setObjectName("file_output")
        self.btn_convert = QtWidgets.QPushButton(self.centralwidget)
        self.btn_convert.setEnabled(False)
        self.btn_convert.setGeometry(QtCore.QRect(370, 200, 75, 23))
        self.btn_convert.setObjectName("btn_convert")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 141, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 260, 141, 16))
        self.label_4.setObjectName("label_4")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 280, 421, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_graph_1 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_graph_1.setEnabled(False)
        self.btn_graph_1.setObjectName("btn_graph_1")
        self.horizontalLayout.addWidget(self.btn_graph_1)
        self.btn_graph_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_graph_2.setEnabled(False)
        self.btn_graph_2.setObjectName("btn_graph_2")
        self.horizontalLayout.addWidget(self.btn_graph_2)
        self.btn_graph_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_graph_3.setEnabled(False)
        self.btn_graph_3.setObjectName("btn_graph_3")
        self.horizontalLayout.addWidget(self.btn_graph_3)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 130, 421, 19))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radio_lt = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radio_lt.setCheckable(True)
        self.radio_lt.setChecked(True)
        self.radio_lt.setObjectName("radio_lt")
        self.buttonGrou = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGrou.setObjectName("buttonGrou")
        self.buttonGrou.addButton(self.radio_lt)
        self.horizontalLayout_2.addWidget(self.radio_lt)
        self.radio_hy = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radio_hy.setObjectName("radio_hy")
        self.buttonGrou.addButton(self.radio_hy)
        self.horizontalLayout_2.addWidget(self.radio_hy)
        self.radio_vl = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radio_vl.setObjectName("radio_vl")
        self.buttonGrou.addButton(self.radio_vl)
        self.horizontalLayout_2.addWidget(self.radio_vl)
        self.stn_input = QtWidgets.QLineEdit(self.centralwidget)
        self.stn_input.setEnabled(True)
        self.stn_input.setGeometry(QtCore.QRect(20, 80, 311, 20))
        self.stn_input.setReadOnly(True)
        self.stn_input.setObjectName("stn_input")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 60, 141, 16))
        self.label_5.setObjectName("label_5")
        self.btn_srcstn = QtWidgets.QPushButton(self.centralwidget)
        self.btn_srcstn.setGeometry(QtCore.QRect(360, 80, 75, 23))
        self.btn_srcstn.setObjectName("btn_srcstn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_srcipn.setText(_translate("MainWindow", "Buscar"))
        self.btn_convert.setText(_translate("MainWindow", "Convertir"))
        self.label.setText(_translate("MainWindow", "Ruta archivo ipn"))
        self.label_2.setText(_translate("MainWindow", "Nombre archivo de salida"))
        self.label_4.setText(_translate("MainWindow", "Graficar"))
        self.btn_graph_1.setText(_translate("MainWindow", "longitud - latitud"))
        self.btn_graph_2.setText(_translate("MainWindow", "longitud - profundidad"))
        self.btn_graph_3.setText(_translate("MainWindow", "latitud - profundidad"))
        self.radio_lt.setText(_translate("MainWindow", "Lotos"))
        self.radio_hy.setText(_translate("MainWindow", "HypoDD"))
        self.radio_vl.setText(_translate("MainWindow", "Velest"))
        self.label_5.setText(_translate("MainWindow", "Ruta archivo estaciones"))
        self.btn_srcstn.setText(_translate("MainWindow", "Buscar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
