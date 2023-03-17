from flask import Blueprint, render_template, redirect, url_for


en_views = Blueprint('en_views', __name__)


@en_views.route('/')
def home():
    return redirect(url_for('en_views.get_page', page='home'))


@en_views.route('/<page>')
def get_page(page):
    return render_template(f'/en/{page}.html')

