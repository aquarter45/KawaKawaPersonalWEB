from flask import Blueprint, render_template, redirect, url_for


views = Blueprint('views', __name__)


@views.route('/')
def home():
    return redirect(url_for('views.get_page', page='home'))


@views.route('/<page>')
def get_page(page):
    return render_template(f'{page}.html')
