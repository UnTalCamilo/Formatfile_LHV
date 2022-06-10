from time import sleep
from window import *
from lib.main import *
from lib.graph import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # Creamos nuestra ventana a partir de un QMainWindow
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.object = None

        self.btn_srcipn.clicked.connect(self.file_ipn)
        self.btn_srcstn.clicked.connect(self.file_stn)

        self.btn_graph_1.clicked.connect(self.graph_one)
        self.btn_graph_2.clicked.connect(self.graph_two)
        self.btn_graph_3.clicked.connect(self.graph_tree)


        self.radio_lt.toggled.connect(self.radio_format)
        self.radio_hy.toggled.connect(self.radio_format)
        self.radio_vl.toggled.connect(self.radio_format)

        self.btn_convert.clicked.connect(self.convert)


        self.radio_format()


    def file_ipn(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Archivo ipn','./',"*.ipn")
        self.ipn_input.setText(fname[0])
    
        if len(self.stn_input.text()) > 0:
            self.file_output.setDisabled(False)
            self.btn_convert.setEnabled(True)


    def file_stn(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open dat file','./',"*.*")
        self.stn_input.setText(fname[0])
        if len(self.ipn_input.text()) > 0:
            self.file_output.setDisabled(False)
            self.btn_convert.setEnabled(True)

    def radio_format(self):
        if self.radio_lt.isChecked():
            self.file_output.setText("rays.dat")
        elif self.radio_hy.isChecked():
            self.file_output.setText("phases.dat")
        else:
            self.file_output.setText("phases.cnv")

    def convert(self):
        self.object = None
        self.btn_enabled(False)
        sleep(1)
        if self.radio_lt.isChecked():
            opt = 0
        elif self.radio_hy.isChecked():
            opt = 1
        else:
            opt = 2
        file_in = self.ipn_input.text()
        tmpfileout = file_in.split('/')[-1]
        tmp_pathout = file_in.replace(tmpfileout, '')
        file_out = tmp_pathout + self.file_output.text()
        file_stns = self.stn_input.text()

        self.object = Convert_ipn(file_in, file_out, file_stns, opt)
        self.object.read_files()
        QtWidgets.QMessageBox.about(self, "Alerta", f"El archivo {self.file_output.text()} se creo exitosamente")
        self.btn_enabled(True)

    def graph_one(self):
        show_graph(0, self.object.points_lon, self.object.points_lat, self.object.points_dep, self.object.volcano)

    def graph_two(self):
        show_graph(1, self.object.points_lon, self.object.points_lat, self.object.points_dep, self.object.volcano)

    def graph_tree(self):
        show_graph(2, self.object.points_lon, self.object.points_lat, self.object.points_dep, self.object.volcano)
    
    def btn_enabled(self, status):
        self.btn_convert.setEnabled(status)
        self.btn_srcipn.setEnabled(status)
        self.btn_srcstn.setEnabled(status)
        self.btn_graph_1.setEnabled(status)
        self.btn_graph_2.setEnabled(status)
        self.btn_graph_3.setEnabled(status)

def main():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()