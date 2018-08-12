from flask import url_for, request, render_template, flash
from flask_login import current_user, login_required
from werkzeug.utils import redirect

from app.models.base import db
from app.models.wish import Wish
from app.service.wish import WishService
from app.view_models.wish import MyWishes
from . import web


def limit_key_prefix():
    isbn = request.args['isbn']
    uid = current_user.id
    return 'satisfy_wish/{}/{}'.format(isbn, uid)


@web.route('/my/wish')
@login_required
def my_wish():
    uid = current_user.id
    wishes = Wish.query.filter_by(uid=uid, launched=False, status=1).all()
    gifts_count = WishService.get_gifts_count(wishes)
    view_model = MyWishes(wishes, gifts_count)
    return render_template('my_wish.html', wishes=view_model.my_wishes)


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            wish = Wish()
            wish.uid = current_user.id
            wish.isbn = isbn
            db.session.add(wish)
    else:
        flash('这本书已添加至你的赠送清单或已存在于你的心愿清单，请勿重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
@login_required
def satisfy_wish(wid):
    return redirect(url_for('web.index'))


@web.route('/wish/book/<isbn>/redraw')
@login_required
def redraw_from_wish(isbn):
    wish = Wish.query.filter_by(isbn=isbn).first()
    if not wish:
        flash('该心愿不存在，删除失败')
    else:
        with db.auto_commit():
            wish.status = 0
    return redirect(url_for('web.my_wish'))

