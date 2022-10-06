import csv
import sys

import matplotlib.pyplot as plt
import numpy as np
import pyecharts.options as opts
from pyecharts.charts import Line, Bar, Scatter

# 3.2 连续型时间数据可视化

# - 3.2.1 阶梯图

line0 = Line()

dataX1 = [str(x) for x in range(1995, 2010)]
dataY1 = [0.32, 0.32, 0.32, 0.32, 0.33, 0.33, 0.34, 0.37, 0.37, 0.37, 0.37, 0.39, 0.41, 0.42, 0.44]

line0.add_xaxis(dataX1)
line0.add_yaxis('Price', dataY1, is_step=True)

line0.set_colors('green')

line0.set_global_opts(
    title_opts=opts.TitleOpts(title='Step Graph of U.S. Postage\nfrom 1995 to 2009'),
    yaxis_opts=opts.AxisOpts(min_=0.3, max_=0.45),
    xaxis_opts=opts.AxisOpts(name='Year')
)

line0.render('Step Graph.html')

plt.figure(figsize=(12, 6))

plt.title('Step Graph of U.S. Postage from 1995 to 2009')
plt.xlabel('Year')
plt.ylabel('Price')
plt.xticks(rotation=30)

plt.step(dataX1, dataY1, 'green', where='pre')
plt.show()

# - 3.2.2 折线图

line1 = Line()

dataX2: list[str] = []
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

line1.add_xaxis(dataX2)
line1.add_yaxis('Population',
                dataY2,
                symbol="emptyCircle",
                is_symbol_show=True,
                label_opts=opts.LabelOpts(is_show=False),
                color='green'
                )

line1.set_global_opts(
    tooltip_opts=opts.TooltipOpts(is_show=True),
    title_opts=opts.TitleOpts(title='World Historical Population\nfrom 1960 to 2010'),
    xaxis_opts=opts.AxisOpts(name='Year', type_='category'),
    yaxis_opts=opts.AxisOpts(type_='value',
                             axistick_opts=opts.AxisTickOpts(is_show=True),
                             splitline_opts=opts.SplitLineOpts(is_show=True),
                             min_=2000000000,
                             max_=7000000000
                             )
)

line1.render('Line Chart.html')

plt.figure(figsize=(14, 6))

plt.title('World Historical Population from 1960 to 2010')
plt.xlabel('Year')
plt.xticks(rotation=30)
plt.ylabel('Population')

plt.plot(dataX2, dataY2)
plt.show()

# - 3.2.3 拟合曲线

s0 = Scatter()
line2 = Line()

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

poly = np.polyfit(dataX3, dataY3, deg=2)
plt.plot(dataX3, np.polyval(poly, dataX3))

plt.show()

dataX3_0 = [str(i) for i in dataX3]

s0.add_xaxis(dataX3_0)
s0.add_yaxis('Rate Scatter',
             dataY3,
             label_opts=opts.LabelOpts(is_show=False),
             symbol_size=5,
             color='lime'
             )

s0.set_global_opts(
    xaxis_opts=opts.AxisOpts(name='Year'),
    title_opts=opts.TitleOpts(
        title='Unemployment Rate from\n1948 to 2010'
    )
)

line2.add_xaxis(dataX3_0)
line2.add_yaxis('Rate Line',
                np.polyval(poly, dataX3),
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(width=5),
                itemstyle_opts=opts.ItemStyleOpts(color='blue')
                )

s0.overlap(line2).render('Curve Fitting.html')

# 3.3 离散型时间数据可视化

# - 3.3.1 散点图

s1 = Scatter()

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

s1.add_xaxis(dataX4)
s1.add_yaxis('Number of Subscribers',
             dataY4,
             label_opts=opts.LabelOpts(is_show=False),
             symbol_size=5,
             color='lime'
             )

s1.set_global_opts(
    xaxis_opts=opts.AxisOpts(name='Date'),
    title_opts=opts.TitleOpts(
        title='Scatter Plot of\nSubscriber Numbers'
    )
)

s1.render('Scatter Plot.html')

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

plt.figure(figsize=(12, 6))

plt.title('Bar Chart of Dogs Eaten by Winners from 1980 to 2010')
plt.xlabel('Year')
plt.ylabel('Number')

plt.bar(dataX6,
        dataY6_1,
        align='center',
        color='lime',
        label='First Prize'
        )

plt.bar(dataX6,
        dataY6_2,
        align='center',
        bottom=dataY6_1,
        color='lightGreen',
        label='Second Prize'
        )

bottom = np.sum([dataY6_1, dataY6_2], axis=0).tolist()

plt.bar(dataX6,
        dataY6_3,
        align='center',
        bottom=bottom,
        color='lightBlue',
        label='Third Prize'
        )

plt.legend()
plt.show()
