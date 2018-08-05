from app.models.gift import Gift
from app.models.wish import Wish
from app.view_models.book import BookViewModel
from flask import current_app
from sqlalchemy import func, desc
from app.models.base import db


class GiftService:
    """
    Gift服务层
    """
    @staticmethod
    def get_wish_counts(gifts):
        book_isbn_list = [gift.isbn for gift in gifts]
        count_list = db.session.query(func.count(Wish.id), Wish.isbn). \
            filter(Wish.launched == False, Wish.isbn.in_(book_isbn_list),
                   Wish.status == 1).group_by(Wish.isbn).all()
        return count_list

    @staticmethod
    def recent():
        gift_list = Gift.query.filter_by(launched=False).order_by(
            desc(Gift.create_time)).limit(current_app.config['RECENT_BOOK_PER_PAGE']).all()
        books = [BookViewModel(gift.book.first) for gift in gift_list]
        return books




