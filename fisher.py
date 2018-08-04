from flask import Flask, make_response

__author__ = 'kalirfi'

app = Flask(__name__)
app.config.from_object('config')

# 保证了唯一url，涉及到搜索引擎的索引和优化
# flask可以兼容/hello和hello/，因为其做了一个重定向（在response的location:url2  status code:301/302）
# 视图函数在返回时会有一部分的附加信息
@app.route('/hello/')
def hello():
    # status code 200,404,301
    # content-type http headers
    # content-type = text/html (默认值)
    # flask会将返回的字符串作为body，然后结合其它东西包装成Response对象返回
    headers = {
        'Content-type': 'application/json',
        'Location': 'http://www.bing.com'
    }
    # response = make_response('<html><h1>Hello</h1></html>', 200)
    # response.headers = headers
    # return response
    return '<html></html>', 301, headers
    #return '<h1>Hello<h1>'
# 第二种注册方式：
# app.add_url_rule('/hello/'，view_func=hello) @app.route其实调用的就是该方法add_url_rule()

# 传入debug，调试模式激活，其会将异常很详细的在网页上显示，并且会在修改代码后自动重启服务器
# 调试模式性能差（用的是flask自带的服务器），且返回的错误信息会影响网站安全性
# 导入时不执行判断
if __name__ == '__main__':
    # 生产环境 nginx+ uwsgi(fisher.py是被uwsgi加载的文件)
    app.run(host='0.0.0.0', port=2000, debug=app.config['DEBUG'])
