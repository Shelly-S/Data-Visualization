import matplotlib.pyplot as plt
from pyecharts.charts import Line, Bar, Tab
import pyecharts.options as opts
import numpy as np
import csv
import sys
from os.path import dirname, abspath

currentDir = dirname(abspath(__file__))

# 3.2 连续型时间数据可视化

# - 3.2.1 阶梯图

line = Line()

dataX1 = [str(x) for x in range(1995, 2010)]
dataY1 = [0.32, 0.32, 0.32, 0.32, 0.33, 0.33, 0.34, 0.37, 0.37, 0.37, 0.37, 0.39, 0.41, 0.42, 0.44]

line.add_xaxis(dataX1)
line.add_yaxis('Price', dataY1, is_step=True)

line.set_colors('green')

line.set_global_opts(
    title_opts=opts.TitleOpts(title='Step Graph of U.S. Postage from 1995 to 2009'),
    yaxis_opts=opts.AxisOpts(min_=0.3, max_=0.45),
    xaxis_opts=opts.AxisOpts(name='Year')
)

line.render('Step Graph.html')


plt.figure(figsize=(12, 6))

plt.xlabel('Year')
plt.ylabel('Price')
plt.xticks(rotation=30)

plt.step(dataX1, dataY1, 'green', where='pre')
plt.show()

# - 3.2.2 折线图

dataX2 = []
dataY2 = []

try:
    with open(r'../Data/practice1/world-population.csv') as f:
        reader = csv.reader(f)

        for dataRow in reader:
            if reader.line_num != 1:
                dataX2.append(dataRow[0])
                dataY2.append(eval(dataRow[1]))
except ValueError or IndexError:
    print('Error reading csv file!')
    sys.exit(-1)

plt.figure(figsize=(14, 6))

plt.title('World Historical Population from 1960 to 2010')
plt.xlabel('Year')
plt.xticks(rotation=30)
plt.ylabel('Population')

plt.plot(dataX2, dataY2)
plt.show()

# - 3.2.3 拟合曲线

dataX3 = []
dataY3 = []

try:
    with open(r'../Data/practice1/unemployment-rate-1948-2010.csv') as f:
        reader = csv.reader(f)

        for dataRow in reader:
            if reader.line_num != 1:
                dataX3.append(eval(dataRow[1]))
                dataY3.append(eval(dataRow[3]))
except ValueError or IndexError:
    print('Error reading csv file!')
    sys.exit(-1)

plt.figure()

plt.title('Unemployment Rate from 1948 to 2010')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate')

plt.scatter(dataX3[:], dataY3[:], s=10, c='green', marker='o', alpha=0.5)

poly = np.polyfit(dataX3, dataY3, deg=3)
plt.plot(dataX3, np.polyval(poly, dataX3))
plt.show()

# 3.3 离散型时间数据可视化

# - 3.3.1 散点图

dataX4 = []
dataY4 = []

try:
    with open(r'../Data/practice1/subscribers.csv') as f:
        reader = csv.reader(f)

        for dataRow in reader:
            if reader.line_num != 1:
                dataX4.append(dataRow[0])
                dataY4.append(eval(dataRow[1]))
except ValueError or IndexError:
    print('Error reading csv file!')
    sys.exit(-1)

plt.figure(figsize=(12, 6))

plt.title('Scatter Plot of Subscriber Numbers')
plt.xlabel('Date')
plt.xticks(rotation=30)
plt.ylabel('Number of Subscribers')

plt.scatter(dataX4, dataY4, s=50, c='green', marker='o', alpha=0.5)
plt.show()

# - 3.3.2 柱形图

bar0 = Bar()

dataX5 = []
dataY5 = []

try:
    with open(r'../Data/practice1/hot-dog-contest-winners.csv') as f:
        reader = csv.reader(f)

        for dataRow in reader:
            if reader.line_num != 1:
                dataX5.append(dataRow[0])
                dataY5.append(eval(dataRow[2]))
except ValueError or IndexError:
    print('Error reading csv file!')
    sys.exit(-1)

bar0.add_xaxis(dataX5)
bar0.add_yaxis("number of dogs eaten", dataY5, label_opts=opts.LabelOpts(is_show=False), color='green')

bar0.set_global_opts(
    title_opts=opts.TitleOpts(title='Bar Chart of Dogs Eaten by Winners\nfrom 1980 to 2010'),
    xaxis_opts=opts.AxisOpts(name='Year'),
    yaxis_opts=opts.AxisOpts(name='Number')
)

bar0.render('Bar Chart.html')


plt.figure(figsize=(12, 6))

plt.title('Dogs Eaten by Winners of U.S. Hot Dog Contests from 1980 to 2010')
plt.xlabel('Year')
plt.xticks(rotation=30)
plt.ylabel('Dogs eaten')

plt.bar(dataX5, dataY5)
plt.show()

# - 3.3.3 堆叠柱形图

bar1 = Bar()

data = []

try:
    with open(r'../Data/practice1/hot-dog-places.csv') as f:
        reader = csv.reader(f)
        for dataRow in reader:
            data.append(dataRow)
    dataX6 = data[0]
    dataY6_1 = [eval(i) for i in data[1]]
    dataY6_2 = [eval(i) for i in data[2]]
    dataY6_3 = [eval(i) for i in data[3]]

except ValueError or IndexError:
    print('Error reading csv file!')
    sys.exit(-1)

bar1.add_xaxis(dataX6)
bar1.add_yaxis("First Prize", dataY6_1, label_opts=opts.LabelOpts(is_show=False), color='lime', stack="stack")
bar1.add_yaxis('Second Prize', dataY6_2, label_opts=opts.LabelOpts(is_show=False), color='lightGreen', stack="stack")
bar1.add_yaxis('Third Prize', dataY6_3, label_opts=opts.LabelOpts(is_show=False), color='lightBlue', stack="stack")

bar1.set_global_opts(
    title_opts=opts.TitleOpts(title='Bar Chart of Dogs Eaten by\nWinners from 1980 to 2010'),
    xaxis_opts=opts.AxisOpts(name='Year'),
    yaxis_opts=opts.AxisOpts(name='Number')
)

bar1.render('Stack Graph.html')