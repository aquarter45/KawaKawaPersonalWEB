from flask import Flask, render_template


def page_not_found(e):
    return render_template("404.html"), 404


def create_app():
    # define app
    app = Flask(__name__)

    # import blueprint
    from .en_views import en_views
    from .jp_views import jp_views
    from .zh_views import zh_views

    # register Blueprint
    app.register_blueprint(en_views, url_prefix='/')
    app.register_blueprint(zh_views, url_prefix='/zh')
    app.register_blueprint(jp_views, url_prefix='/jp')

    # return WebAPP
    return app
