from PyQt5.QtWidgets import QMainWindow, QButtonGroup, QFileDialog, QLabel, QTableWidgetItem
import pandas as pd
import matplotlib.pyplot as plt

from ui.ui_mainwindow import Ui_MainWindow
from MatPlot.ScatterMatrix import ScatterMatrix

class MainWindow(QMainWindow):
    """
    Current class describe application main window
    """

    def __init__(self):
        super(MainWindow, self).__init__()  # call parent constructor

        # initialize all UI elements.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Bind button events.
        self.ui.read_file_button_1.clicked.connect(self.on_read_file_button_111_clicked)

        # Variables.
        self.Data = pd.DataFrame()

        # Create instance of Plot class and pass plot widget to it.
        self.my_canvas = ScatterMatrix(self.ui.plot_widget_1)
    # ------- UI EVENTS --------------------------------------------------------------------------------------------- #

    def on_read_file_button_111_clicked(self):
        # print("On method {0}".format("on_data_mode_page_select_file_button_clicked"))

        path, check = QFileDialog.getOpenFileName(None, "Select data file", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if not check:
            return

        self.Data = pd.read_csv(path, header=None, sep='\s+')
        self.show_data()
        self.show_statistics()
        self.show_plots()
        return

    def show_data(self):
        # calculate data additional information
        r_count = self.Data.shape[0]
        c_count = self.Data.shape[1]

        # prepare table and widgets
        self.ui.data_table_widget.setColumnCount(c_count)
        self.ui.data_table_widget.setRowCount(r_count)

        # show data
        for i in range(c_count):
            for j in range(r_count):
                self.ui.data_table_widget.setItem(j, i, QTableWidgetItem(str(self.Data[i][j])))

    def show_statistics(self):
        # calculate data additional information
        stats = self.Data.describe()

        r_count = stats.shape[0]
        c_count = stats.shape[1]

        # prepare table and widgets
        self.ui.data_table_widget_2.setColumnCount(c_count)
        self.ui.data_table_widget_2.setRowCount(r_count)

        self.ui.data_table_widget_2.setVerticalHeaderLabels(stats.index.tolist())

        # show data
        for i in range(c_count):
            for j in range(r_count):
                self.ui.data_table_widget_2.setItem(j, i, QTableWidgetItem(str(stats[i][j])))

    def show_plots(self):
        self.my_canvas.plot(self.Data)
