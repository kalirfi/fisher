from flask import url_for
from werkzeug.utils import redirect

from . import web


@web.route('/my/wish')
def my_wish():
    return redirect(url_for('web.index'))


@web.route('/wish/book/<isbn>')
def save_to_wish(isbn):
    return redirect(url_for('web.index'))


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    return redirect(url_for('web.index'))


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    return redirect(url_for('web.index'))
