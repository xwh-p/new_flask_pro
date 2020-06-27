from flask import Blueprint, render_template, g, session, redirect, url_for

from www.helper.session_help import Session
# from www.model_data.index_5 import get_data1
from www.model_data.index_5 import get_new_driver, hight_inc, region_data, struct_optmize

home_page = Blueprint('home_page', __name__)


@home_page.before_request
def before_request():
    if not Session.is_user_exist():

        print('第一次请求。。。。。。。')
        return render_template('login.html')
    g.user = Session.get_user()
    print(Session.get_user(),'登陆状态')


@home_page.route('/')
def index():
    return render_template('index.html')

# 创新驱动
@home_page.route("/data1/")
def get_bar_chart1():
    c = get_new_driver()
    return c.dump_options_with_quotes()


# 高效增长
@home_page.route('/hight_increase/')
def hight_increase():
    print('---------------来了来了')
    c = hight_inc()
    return c.dump_options_with_quotes()



# 区域协调
@home_page.route('/region_data/')
def get_region_data():
    c = region_data()
    return c.dump_options_with_quotes()


# 结构优化
@home_page.route('/struct_optmize/')
def get_struct_optmize():

    c = struct_optmize()
    return c.dump_options_with_quotes()


