from flask import current_app, flash, render_template, url_for
from sqlalchemy import desc
from werkzeug.utils import redirect

from app.models.gift import Gift
from app.service.gift import GiftService
from app.view_models.gift import MyGifts
from . import web
from flask_login import login_required, current_user
from app.models.base import db


@web.route('/my/gifts')
@login_required
def my_gifts():
    uid = current_user.id
    gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(
        desc(Gift.create_time)).all()
    wishes_count = GiftService.get_wish_counts(gifts)
    view_model = MyGifts(gifts, wishes_count).package()
    return render_template('my_gifts.html', gifts=view_model)


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
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
@login_required
def redraw_from_gifts(gid):
    gift = Gift.query.filter_by(id=gid, launched=False).first()
    if not gift:
        flash('该书籍已交易，删除失败')
    else:
        with db.auto_commit():
            current_user.beans -= current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.delete(gift)
    return redirect(url_for('web.my_gifts'))



