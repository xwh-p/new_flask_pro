import os

from flask import Flask

from www.view_service import dashboard_view
from www.view_service import login_view


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile(os.getcwd()+'/config.py', silent=True)
    else:
        app.config.from_mapping(test_config)


    app.register_blueprint(dashboard_view.home_page)
    app.register_blueprint(login_view.login_req)
    return app
