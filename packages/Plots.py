import pandas as pd
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import FigureCanvas
# matplotlib.pyplot.figure
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class Plots:

    def __init__(self,dataframe):
        self.data = dataframe
        print('Dataframe recvied = {}'.format(type(self.data)))

    def pie_plot(self):
        # plt.figure()
        lst = []
        counts = self.data.project_is_approved.value_counts()
        n = counts[1]
        l = counts[0]
        lst.append(n)
        lst.append(l)
        labels = ['approved','not approved']
        plt.pie(lst,labels = labels)
        plt.figure()
        plt.show()

    def box_plot(self):
        f = plt.figure(figsize=(10,3))
        ax = f.add_subplot(121)
        ax2 = f.add_subplot(122)
        sns.boxplot(x="teacher_prefix", y="project_is_approved", data = self.data, ax = ax)
        sns.boxplot(x="project_grade_category", y="project_is_approved", data = self.data, ax = ax2)
        plt.show()



    def boxplot_title(self):
        plt.figure()
        approved_title_word_count = self.data[self.data['project_is_approved']==1]['project_title'].str.split().apply(len)
        approved_title_word_count = approved_title_word_count.values

        rejected_title_word_count = self.data[self.data['project_is_approved']==0]['project_title'].str.split().apply(len)
        rejected_title_word_count = rejected_title_word_count.values

        plt.boxplot([approved_title_word_count, rejected_title_word_count])
        plt.xticks([1,2],('Approved Projects','Rejected Projects'))
        plt.ylabel('Words in project title')
        # plt.grid()
        plt.figure()
        plt.show()

    def heatmaps(self):
        plt.figure()
        corr_matrix=self.data.corr()
        sns.heatmap(corr_matrix,annot = True, cmap='PuOr')
        plt.show()
