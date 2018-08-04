"""
完成蓝图级别的初始化初始化工作
"""

from flask import Blueprint

# __name__表示蓝图所在的模块
web = Blueprint('web', __name__)

from app.web import book
from app.web import user

