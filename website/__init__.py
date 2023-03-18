from flask import Flask, render_template


def page_not_found(e):
    return render_template("404.html"), 404


def create_app():
    # define app
    app = Flask(__name__)

    # import blueprint
    from .views import views

    # register Blueprint
    app.register_blueprint(views, url_prefix='/')
    app.register_error_handler(404, page_not_found)

    # return WebAPP
    return app
