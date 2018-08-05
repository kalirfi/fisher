from flask_login import login_required, current_user

from app.service.gift import GiftService
from . import web
from flask import render_template


@web.route('/')
def index():
    gift_list = GiftService.recent()
    return render_template('index.html', recent=gift_list)


@web.route('/personal')
@login_required
def personal_center():
    return render_template('personal.html', user=current_user.summary)
