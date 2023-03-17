from flask import Blueprint, render_template, redirect, url_for


zh_views = Blueprint('zh_views', __name__)


@zh_views.route('/')
def home():
    return redirect(url_for('zh_views.get_page', page='home'))


@zh_views.route('/<page>')
def get_page(page):
    return render_template(f'/zh/{page}.html')
