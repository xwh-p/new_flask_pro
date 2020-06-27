import os
import random

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline, Grid, Line
from pyecharts.globals import ThemeType


def get_zi_index_data(child_path):
    path = os.path.abspath(os.path.join(os.getcwd()))+'/www/data/zi_zhi_shu/'
    data = None
    try:
        data = pd.read_csv(path+child_path)
    except Exception as e:
        try:
            data = pd.read_csv(path + child_path, encoding='gbk')
        except Exception as e:
            print(e)
            print('读取文件错误-------')


    return data.set_index('year')

# 创新驱动指数
def get_new_driver():
    make_new = get_zi_index_data('new_driver.csv')
    return theme_macarons(make_new,'创新驱动')


# 高效增长
def hight_inc():
    make_new = get_zi_index_data('hight_inc_index.csv')

    return theme_macarons(make_new,'高效增长')

# 区域协调
def region_data():
    make_new = get_zi_index_data('region_index.csv')

    return theme_macarons(make_new,'区域协调')


# 结构优化
def struct_optmize():
    make_new = get_zi_index_data('struct_optimize.csv')

    return theme_macarons(make_new, '结构优化')


def theme_macarons(make_new,tag):
    tl = Timeline(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))  # theme=ThemeType.PURPLE_PASSION
    tl.add_schema(pos_bottom='-7px',
                  is_auto_play=True,
                  symbol_size=[20, 20],
                  play_interval=2000,

                  )
    for i in range(2015, 2020):
        bar = Bar()
        bar.add_xaxis(list(make_new.columns))
        bar.add_yaxis("", list(make_new.loc[i, :].values), label_opts=opts.LabelOpts(is_show=False))
        bar.set_colors([random.choice(['blue','rgba(100,255,0,0.8)','#5793f3','#007A99','yellow'])])
        bar.set_global_opts(xaxis_opts=opts.AxisOpts(name="",
                                                     axislabel_opts={"rotate": 40}),
                            title_opts=opts.TitleOpts("{}-{}指数".format(i,tag))

                            )

        tl.add(bar, "{}年".format(str(i)))
    return tl
