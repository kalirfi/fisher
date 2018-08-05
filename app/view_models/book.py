class BookViewModel(object):
    def __init__(self, book):
        self.title = book.get('title', '')
        self.publisher = book.get('publisher', '')
        self.author = '、'.join(book.get('author', ''))
        self.image = book.get('image', '')
        self.price = book.get('price', '')
        self.summary = book.get('summary', '')
        self.pages = book.get('pages', '')
        self.isbn = book.get('isbn', '')

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,
                        [self.author, self.publisher, self.price])
        return '/'.join(intros)


class BookCollection(object):
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]



class _BookViewModel(object):
    @classmethod
    def package_single(cls, data, keyword):
        views = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            views['total'] = 1
            views['books'] = [cls.__cut_book_data(data)]
        return views

    @classmethod
    def package_collection(cls, data, keyword):
        views = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            views['total'] = data['total']
            views['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return views

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            # 因为pages和summary可能为空None,也可以用data['xx'] or ''写法
            'pages': data.get('pages', ''),
            # 'author'返回list更灵活，此处为了后端直接渲染简便
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data.get('summary', ''),
            'image': data['image']
        }
        return book

