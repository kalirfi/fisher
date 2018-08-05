import time


def timestamp():
    return int(time.time())


def timeformat(millis):
    formats = '%Y %m %d %H:%M:%S'
    times = time.localtime(int(millis))
    formattime = time.strftime(formats, times)
    return formattime


def log(*args, **kwargs):
    dt = timeformat(time.time())
    with open('log.txt', 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)
