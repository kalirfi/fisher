class MyResource:
    def query(self):
        print('query data')

from contextlib import contextmanager


@contextmanager
def make_myresource():
    print('connect to resource')
    yield  MyResource()
    print('close resource connection')


with make_myresource() as r:
    r.query

