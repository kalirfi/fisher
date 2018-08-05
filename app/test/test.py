from app.libs.httper import HTTP

isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'


def search_by_isbn(isbn):
    url = isbn_url.format(isbn)
    result = HTTP.get(url)
    return result


def search_by_keyword(keyword, count=20, start=0):
    url = keyword_url.format(keyword, count, start)
    result = HTTP.get(url)
    return result

print(search_by_keyword('我'))
