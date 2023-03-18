from flask import Blueprint, render_template, redirect, url_for, abort
from os import path

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return redirect(url_for('views.get_page', page='home'))


@views.route('/<page>')
def get_page(page):
    if path.isfile(f"website/Templates/{page}.html"):
        return render_template(f'{page}.html')

    return abort(404)
