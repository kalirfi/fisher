from flask import current_app, flash

from app.models.gift import Gift
from . import web
from flask_login import login_required, current_user
from app.models.base import db


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'My Gifts'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        # 涉及2个模型gift和user模型的操作，用事务操作，保证原子性/事务完整
        # try:
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id

            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            # sqlalchemy天然支持事务操作，见以下的两句
            db.session.add(gift)
        #     db.session.commit()
        # except Exception as e:
        #     db.session.rollback()
        #     raise e
    else:
        flash('这本书已添加至你的赠送清单或已存在于你的心愿清单，请不要重复添加')


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



