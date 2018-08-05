from flask import Flask, current_app, request, Request

app = Flask(__name__)
# 应用上下文 对象 Flask
# 请求上下文 对象 Request
# Flask   AppContext(对Flask的封装，其内包含所需的Flask没有的环境信息)
# Request    RequestContext(对Request的封装，其内包含所需的Request没有的环境信息)
# 不使用以上四个核心类来直接操作，而使用代理模式
# 代理模式生成的request,session,current_app
# 离线应用，单元测试
# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
# ctx.pop()

with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']

# 实现了上下文协议的对象使用with
# 上下文管理器
# __enter__  __exit__
# 上下文表达式必须要返回一个上下文管理器（此例中为app_context()返回了一个实现了__exit__与__enter__的上下文管理器对象）
# with

# 1.连接数据库
# 2.sql
# 3.释放资源
#
# 一般：
# try
# except
# finally:
# 可以：
# __enter__
# __exit__
#
#读取文件
#


# class A:
#     def __enter__(self):
#         a = 1
#         # return a
#
#     def __exit__(self):
#         b = 2
#
# # as后的对象为上下文管理器的__enter__方法所返回的值
# with A() as obj_A: # 1.obj_A:None  2. 1
#     pass

class MyResource:
    def __enter__(self):
        print('connect to resource')
        return self

    def __exit__(self, exc_type, exc_value, tb):
        print('close resource connection')

    def query(self):
        print('query data')


with MyResource() as resource:
    resource.query()

