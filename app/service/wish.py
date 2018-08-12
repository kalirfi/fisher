from sqlalchemy import func

from app.models.base import db
from app.models.gift import Gift


class WishService:
    """
    Wish服务层
    """
    @classmethod
    def get_gifts_count(cls, wish_list):
        book_isbn_list = [wish.isbn for wish in wish_list]
        count_list = db.session.query(func.count(Gift.id), Gift.isbn). \
            filter(Gift.launched is False, Gift.isbn.in_(book_isbn_list), Gift.status == 1).all()
        return count_list
