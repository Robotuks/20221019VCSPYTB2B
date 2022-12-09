import seaborn as sns
import matplotlib.pyplot as plt

# go inside folder use <folder_name>.<file_name>
# to go outside, use '..'
from modules.functions import hello

flights = sns.load_dataset('flights')


flights

list = [1949, 'Jan', 20]
flights.loc[len(flights)] = list


list = [1949, 'Jan', 100]
flights.loc[len(flights)] = list

flights


flights_grouped = flights.groupby(['year', 'month'] ).sum()
flights_grouped = flights_grouped.reset_index()
flights_grouped

flights_pivot = flights_grouped.pivot('month', 'year', 'passengers')
flights_pivot



sns.heatmap(flights_pivot, linewidths=1.)

# plt.show()



hello()