from pyecharts.charts import Pie, Bar, Tree, TreeMap, Line
import pyecharts.options as opts
import pandas as pd
from pyecharts.globals import ThemeType
import json
import sys
import numpy as np

# 4.2 整体与部分

# - 4.2.1 饼图

vote_result = pd.read_csv(r'../Data/practice2/vote_result.csv')

data0 = [list(i) for i in zip(vote_result.values[:, 0], vote_result.values[:, -1])]

p0 = Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))

p0.add('', data0, center=['50%', '50%'])

p0.set_global_opts(
    title_opts=opts.TitleOpts(title='User Interest', pos_left='center'),
    legend_opts=opts.LegendOpts(orient='vertical', pos_left='right')
)

p0.set_series_opts(label_opts=opts.LabelOpts(formatter='{b}: {d}%'))

p0.render(r'../Out/practice2/Pie Chart.html')

# - 4.2.2 环形图

p1 = Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))

p1.add('', data0, center=['50%', '50%'], radius=['45%', '75%'])

p1.set_global_opts(
    title_opts=opts.TitleOpts(title='User Interest', pos_left='center'),
    legend_opts=opts.LegendOpts(orient='vertical', pos_left='right')
)

p1.set_series_opts(label_opts=opts.LabelOpts(formatter='{b}: {d}%'))

p1.render(r'../Out/practice2/Ring Chart.html')

# - 4.2.3 比例中的堆叠

b0 = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width='1200px'))

b0.set_global_opts(
    title_opts=opts.TitleOpts(title='Approval Rate', pos_left='center'),
    xaxis_opts=opts.AxisOpts(
        axislabel_opts={'interval': '0'},
        name='Measures'
    ),
    legend_opts=opts.LegendOpts(orient='vertical', pos_left='right')
)

rate = pd.read_csv(r'../Data/practice2/presidential_approval_rate.csv')

b0.add_xaxis(list(rate.values[:, 0]))

b0.add_yaxis('支持', list(rate.values[:, 1]), stack='1', category_gap='40%',
             label_opts=opts.LabelOpts(position='right'))

b0.add_yaxis('反对', list(rate.values[:, 2]), stack='1', category_gap='40%',
             label_opts=opts.LabelOpts(position='right'))

b0.add_yaxis('不发表意见', list(rate.values[:, -1]), stack='1', category_gap='40%',
             label_opts=opts.LabelOpts(position='right'))

b0.render(r'../Out/practice2/Percent Stacked Area Chart.html')

# - 4.2.4 树图与矩形树图

t0 = Tree(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width='1500px', height='1200px'))

t1 = TreeMap(init_opts=opts.InitOpts(theme=ThemeType.ROMANTIC, width='1500px', height='800px'))

t0.set_global_opts(
    title_opts=opts.TitleOpts(
        title='Some of Continents and Countries',
        pos_left='center')
)

t1.set_global_opts(
    legend_opts=opts.LegendOpts(
        pos_left='center'
    ),
    title_opts=opts.TitleOpts(
        title='GDP',
        pos_left='center'
    )
)

try:
    with open(r'../Data/practice2/GDP_data.json', 'r', encoding='utf-8') as f0:
        data0 = [json.load(f0)]

    with open(r'../Data/practice2/GDP_data_1.json', 'r', encoding='utf-8') as f1:
        data1 = [json.load(f1)]

except IndexError:
    print('Error reading json file!')
    sys.exit(-1)

t0.add('', data0)

t1.add(
    '',
    data1,
    label_opts=opts.LabelOpts(position='inside'),
    color_saturation=[0.35, 0.65],
    itemstyle_opts=opts.ItemStyleOpts(
        border_width=1
    )
)

t0.render(r'../Out/practice2/Tree Chart.html')

t1.render(r'../Out/practice2/Treemap Chart.html')

# 4.3 时空比例（使用堆叠面积图完成）

l0 = Line(init_opts=opts.InitOpts(theme=ThemeType.WONDERLAND, width='900px', height='600px'))

l0.set_global_opts(
    legend_opts=opts.LegendOpts(
        pos_left='right',
        orient='vertical'
    ),
    title_opts=opts.TitleOpts(
        title='U.S. Population By Age',
        pos_left='center'
    ),
    xaxis_opts=opts.AxisOpts(
        name='Year',
        min_=1850, max_=2015,
        interval=10,
        boundary_gap=False
    ),
    tooltip_opts=opts.TooltipOpts(
        trigger='axis',
        axis_pointer_type='cross'
    ),
    yaxis_opts=opts.AxisOpts(
        type_='value',
        axistick_opts=opts.AxisTickOpts(is_show=True),
        splitline_opts=opts.SplitLineOpts(is_show=True),
    )
)

population = pd.read_csv(r'../Data/practice2/us_population_by_age.csv')

year_under5 = list(population.values[:, 1])
year_5_19 = list(population.values[:, 2])
year_20_44 = list(population.values[:, 3])
year_45_64 = list(population.values[:, 4])
year_65above = list(population.values[:, -1])

l0.add_xaxis(population.values[:, 0])

l0.add_yaxis(
    series_name='<5',
    y_axis=year_under5,
    areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
    label_opts=opts.LabelOpts(is_show=False)
)

bottom = np.sum([year_under5, year_5_19], axis=0)

l0.add_yaxis(
    series_name='5-19',
    y_axis=bottom,
    areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
    label_opts=opts.LabelOpts(is_show=False)
)

bottom = np.sum([year_20_44, bottom], axis=0)

l0.add_yaxis(
    series_name='20-44',
    y_axis=bottom,
    areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
    label_opts=opts.LabelOpts(is_show=False)
)

bottom = np.sum([year_45_64, bottom], axis=0)

l0.add_yaxis(
    series_name='45-64',
    y_axis=bottom,
    areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
    label_opts=opts.LabelOpts(is_show=False)
)

bottom = np.sum([year_65above, bottom], axis=0)

l0.add_yaxis(
    series_name='>=65',
    y_axis=bottom,
    areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
    label_opts=opts.LabelOpts(is_show=False)
)

l0.render(r'../Out/practice2/Stacked Area Chart.html')
