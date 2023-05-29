import pandas as pd
from MatPlot.PlotWidget import MyMplCanvas


class ScatterMatrix(MyMplCanvas):
    def __init__(self, *args):
        super().__init__(*args)
        self.transparency = 0.7

    def clear_plot(self):
        super().clear_plot()

    def plot(self, data):
        self.clear_plot()
        pd.plotting.scatter_matrix(data, figsize=(10, 10), marker='o', s=40, alpha=self.transparency, ax=self.axes,
                                       hist_kwds={'bins': 10, 'edgecolor': 'black'})
        self.axes.figure.tight_layout()
        self.draw()
