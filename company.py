import csv
import plotly.figure_factory as ff
import pandas as pd

file_data = pd.read_csv('/Users/prathamarora/Downloads/Python_Projects/normal_distribution__bell_curve/company.csv')

figure = ff.create_distplot([file_data['Avg Rating'].tolist()], ['Average Rating'], show_hist = True)
figure.show()