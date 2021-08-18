import random
import pandas as pd
import plotly.figure_factory as ff
import statistics
import csv

df = pd.read_csv("medium_data.csv")

data = df["reading_time"].tolist()

fig = ff.create_distplot([data], ["reading_time"], show_hist=False)

fig.show()


print("population mean:- ",statistics.mean(data))


def random_set_of_mean(counter):

    dataset = []
    
    for i in range(0, counter):
        random_index= random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean



def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(10)
        mean_list.append(set_of_means)
    show_Fig(mean_list)
    print("sampling mean is ", statistics.mean(mean_list))


setup()

def showFig(meanlist):

    df = meanlist
    
    mean = statistics.mean(df)
    fig = ff.create_distplot([poplist],["Population"], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = "lines", name = "Mean"))

    fig.show()