import os
import sys
from PyQt5 import QtCore,QtGui,QtWidgets,uic
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
import pandas as pd
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import FigureCanvas
# matplotlib.pyplot.figure
import matplotlib.pyplot as plt
import numpy as np

from packages.Analysis import Analysis
from packages.Plots import Plots

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

class EDAUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(EDAUI,self).__init__()
        uipath = SCRIPT_DIR + os.sep + 'ui' + os.sep + 'Edaui.ui'
        uic.loadUi(uipath,self)
        # self.showMaximized()
        self.pushButtonOpen.setStyleSheet("background-color: white")
        # self.pushButtonOpen.setStyleSheet("QLabel { background-color : white; color :black; border-radius : 50px ;border-color : white;}")
        # self.pushButtonOpen.setStyleSheet("border-radius: 25px")
        self.comboBox.setStyleSheet("background-color: white")
        self.comboBox_2.setStyleSheet("background-color: white")
        self.pushButtonOpen.clicked.connect(self.read_csv)
        # self.pushButtonPlot.clicked.connect(self.pieplot)
        self.items1 = {}
        self.items2 = {}
        self.loadComboItems1()
        self.loadComboItems2()
        # self.showMaximized()
    
        
    def loadComboItems1(self):
        # Dropdown menu - function call name
        self.items1['Null values'] = 'null_values'
        self.items1['Row count'] = 'number_rows_columns'
        self.items1['Size of the dataset'] = 'size_dataset'
        self.items1['Columns datatype'] = 'column_dtype'
        self.items1['Number of Duplicates'] = 'duplicates'
        self.load_combobox1()

        
    def load_combobox1(self):
        print(self.items1)
        for i in self.items1:
            self.comboBox.addItem(i)

        # self.comboBox.addItem('null_values')
        # self.comboBox.addItem('number_rows_columns')  
        # self.comboBox.addItem('size_datset')  
        # self.comboBox.addItem('column_dtype')  
        # self.comboBox.addItem('duplicates') 
        self.comboBox.activated[str].connect(self.choice1)
        self.comboBox.show() 

    def choice1(self,s):
        print(s)
        fc = self.items1[s]
        function = getattr(self,fc)
        function()

    def null_values(self):
        a = self.analysis.null_values() 
        a = str(a)
        b = "Number of null values in the Dataset = "
        self.label1.setText(b+a)

    def number_rows_columns(self):
        a = self.analysis.number_rows_columns() 
        a = str(a)
        b = "Shape of the Dataset = "
        self.label1.setText(b+a)

    def size_dataset(self):
        a = self.analysis.size_dataset() 
        a = str(a)
        b = "Size of the Dataset = "
        self.label1.setText(b+a)

    def column_dtype(self):
        a = self.analysis.column_dtype() 
        a = str(a)
        b = "Type of each columns in a Dataset ="
        self.label1.setText(b+a)

    def duplicates(self):
        a = self.analysis.duplicates() 
        a = str(a)
        b = "Number of Duplicates in the Dataset = "
        self.label1.setText(b+a)

    def loadComboItems2(self):
        # Dropdown menu - function call name
        self.items2['Pie Plot'] = 'pieplot'
        self.items2['Box Plot'] = 'box_plot'
        self.items2['Box Plot Title'] = 'boxplot_title'
        self.items2['Heat Maps'] = 'heatmaps'
        self.load_combobox2()

    def load_combobox2(self):
        print(self.items2)
        for i in self.items2:
            self.comboBox_2.addItem(i)
        self.comboBox_2.activated[str].connect(self.choice2)
        self.comboBox_2.show() 


    def choice2(self,s):
        print(s)
        fc = self.items2[s]
        function = getattr(self,fc)
        function()

    def pieplot(self):
        self.plot.pie_plot()

    def box_plot(self):
        self.plot.box_plot()

    def boxplot_title(self):
        self.plot.boxplot_title()

    def heatmaps(self):
        self.plot.heatmaps()


    def read_csv(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.filename , _ = QtWidgets.QFileDialog.getOpenFileName(self,'Open CSV file',"",'csv(*.csv)',options = options)
        # print(self.filename,_)
        if self.filename != None:
            self.my_file = pd.read_csv(self.filename)
            self.row = self.my_file.shape[0]
            self.column = self.my_file.shape[1]
            self.tableWidgetCsv.setRowCount(self.row)
            self.tableWidgetCsv.setColumnCount(self.column)
            # print(type(my_file))
            for i in range(self.row):
                for j in range(self.column):
                    x = self.my_file.iloc[i,j]
                    x = str(x)
                    self.tableWidgetCsv.setItem(i,j,QTableWidgetItem(x))
                
            col_headers = self.my_file[self.my_file.columns[0:]]
            self.tableWidgetCsv.setHorizontalHeaderLabels(col_headers)
            self.plot = Plots(dataframe = self.my_file)
            self.analysis = Analysis(dataframe = self.my_file)

    def pieplot(self):
        self.plot.pie_plot()
      
    
   
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    edaui = EDAUI()
    # edaui.showMaximized()
    # edaui.setGeometry(50,500,1080,1080)
    # edaui.resize(2160,2160)
    edaui.show()
    sys.exit(app.exec_())

