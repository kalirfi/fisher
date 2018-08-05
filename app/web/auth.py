from flask import render_template, request, redirect, url_for, flash
from app.forms.auth import RegisterForm, LoginForm
from app.models.base import db
from app.models.user import User
from . import web
from flask_login import login_user, login_required, logout_user
import cymysql


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    # print(form.data)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            # 数据库会话
            db.session.add(user)
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=True)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号不存在或密码错误！')
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    return render_template('404.html')


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    return render_template('404.html')


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    return render_template('404.html')


@web.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('web.index'))
