from flask import url_for
from werkzeug.utils import redirect

from . import web


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
def send_drift(gid):
    return redirect(url_for('web.index'))


@web.route('/pending')
def pending():
    return redirect(url_for('web.index'))


@web.route('/drift/<int:did>/reject')
def reject_drift(did):
    return redirect(url_for('web.index'))


@web.route('/drift/<int:did>/redraw')
def redraw_drift(did):
    return redirect(url_for('web.index'))


@web.route('/drift/<int:did>/mailed')
def mailed_drift(did):
    return redirect(url_for('web.index'))
