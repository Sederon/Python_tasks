import PyQt5
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QSizePolicy

import matplotlib.image as mpimg

# Create a matplotlib figure and add a plot to it
class MyMplCanvas(FigureCanvas):
    def __init__(self, parent: PyQt5.QtWidgets.QWidget, x_min = 0, x_max = 10, y_min = 0, y_max = 10):
        # Chart borders
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        # Create plot figure
        fig = Figure(figsize=(611/100, 461/100))
        # plt.rcParams['lines.markersize'] = 15 # Set the size for points and curves

        self.axes = fig.add_subplot(111)
        self.axes.set_xlim(self.x_min, self.x_max)
        self.axes.set_ylim(self.y_min, self.y_max)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        # Adjust plot to the borders of the element
        self.figure.subplots_adjust(top=0.95, right=0.95, left = 0.07, bottom=0.07)

    def plot(self, x_data, y_data):
        self.axes.plot(x_data, y_data)

    def clear_plot(self):
        self.axes.clear()
        self.axes.set_xlim(self.x_min, self.x_max)
        self.axes.set_ylim(self.y_min, self.y_max)
        self.draw()