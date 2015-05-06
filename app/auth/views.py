from flask import render_template, redirect, request, url_for, flash, Flask, abort ,g
from flask import jsonify
from flask.ext.login import login_user, logout_user, login_required, current_user
from . import auth
from .. import db, admin
from ..models import User


@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        if current_user.is_authenticated():
            return redirect( url_for('admin.root'))
        return render_template('auth/login.html')
    email = request.form['email']
    password = request.form['password']

    remember_me = True
    if 'remember_me' in request.form:
        remember_me = True

    registered_user = User.query.filter_by(email=email).first()
    if registered_user is not None and registered_user.verify_password(password):
        login_user(registered_user, remember = remember_me)
        flash('Logged in successfully')
        return redirect(request.args.get('next') or url_for('admin.root'))
    flash('Email or Password is invalid' , 'error')
    return redirect(url_for('auth.login'))


@auth.route('/login.json', methods=['POST'])
def login_json():
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    remember_me = True
    if 'remember_me' in request.json:
        remember_me = True

    registered_user = User.query.filter_by(email=email).first()
    if registered_user is not None and registered_user.verify_password(password):
        login_user(registered_user, remember = remember_me)
        print('Logged in successfully')
        return jsonify({'status': 'success'})
    print('Email or Password is invalid' , 'error')
    return jsonify({'status': 'error', 'message': 'email or password incorrect'})

@auth.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('auth/register.html')
    email = request.form['email']
    password = request.form['password']

    searchEmail = User.query.filter_by(email=email).first()
    if searchEmail is not None:
        flash("Email exists, please choose other Email")
        return redirect(url_for('auth.register'))

    user = User(password=password, email=email)
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

