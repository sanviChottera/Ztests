import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as s
import random
import pandas as pd

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()
fig = ff.create_distplot([data],["Math Scores"], show_hist= False)
#fig.show()

mean = s.mean(data)
std_deviation = s.stdev(data)
print("mean of population : ",mean)
print("Standard deviation of population : ",std_deviation)

def randomMean(counter):
    dataset = []
    for i in range(0,counter):
        r = random.randint(0,len(data)-1)
        value = data[r]
        dataset.append(value)
    mean = s.mean(dataset)
    return mean

mlist = []
for i in range(0,1000):
    setofmean = randomMean(100)
    mlist.append(setofmean)

print("\n")
mean = s.mean(mlist)
std_deviation = s.stdev(mlist)

print("mean of sample data : ",mean)
print("Standard deviation of sample data : ",std_deviation)
fig = ff.create_distplot([mlist],["Math Scores"], show_hist= False)
#fig.show()

first_std_start, first_std_end = mean - std_deviation, mean + std_deviation
second_std_start, second_std_end = mean - (2* std_deviation), mean + (2* std_deviation)
third_std_start, third_std_end = mean - (3* std_deviation), mean + (3*std_deviation)

# finding the mean of the first data(STUDENTS WHO GOT TABLET WITH LEARNING MATERIAL) and plotting it on the plot.

df = pd.read_csv("data1.csv")
data = df["Math_score"].tolist()
samplemean1 = s.mean(data)
fig = ff.create_distplot([mlist],["Math Scores"], show_hist= False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[samplemean1, samplemean1], y=[0, 0.17], mode="lines", name="MEAN OF SAMPLE ((IPad))"))
fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
#fig.show()

# finding the mean of the SECOND data (STUDENTS WHO HAD EXTRA CLASSES ) and plotting it on the plot.
df = pd.read_csv("data2.csv")
data = df["Math_score"].tolist()
samplemean2 = s.mean(data)
fig = ff.create_distplot([mlist],["Math Scores"], show_hist= False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[samplemean2, samplemean2], y=[0, 0.17], mode="lines", name="MEAN OF SAMPLE ((Extra Classes))"))
fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_end, second_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
#fig.show()

# finding the mean of the THIRD data (STUDENTS WHO GOT FUNSHEET) and plotting it on the plot.
df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()
samplemean3 = s.mean(data)
fig = ff.create_distplot([mlist],["Math Scores"], show_hist= False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[samplemean3, samplemean3], y=[0, 0.17], mode="lines", name="MEAN OF SAMPLE ((Fun Sheet))"))
fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_end, second_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_end, third_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
#fig.show()

#finding the z score using the formula
zscore1 = (samplemean1 - mean)/std_deviation
print("\n Z-Score for students with ipad : " , zscore1)

zscore2 = (samplemean2 - mean)/std_deviation
print("\n Z-Score for students who had extra classes : " , zscore2)

zscore3 = (samplemean3 - mean)/std_deviation
print("\n Z-Score for students with fun sheets : " , zscore3)
#the students with fun sheets had the most impact
#If z < 1 or z < 2; the impact of the intervention might not be statistically significant
