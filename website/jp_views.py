from flask import Blueprint, render_template, redirect, url_for


jp_views = Blueprint('jp_views', __name__)


@jp_views.route('/')
def home():
    return redirect(url_for('jp_views.get_page', page='home'))


@jp_views.route('/<page>')
def get_page(page):
    return render_template(f'/jp/{page}.html')
