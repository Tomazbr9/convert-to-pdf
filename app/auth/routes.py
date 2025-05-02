from flask import url_for, render_template, redirect

from flask_login import login_user, logout_user, login_required

from werkzeug.security import generate_password_hash, check_password_hash

from app.models.user import UserModel

from app.auth.forms import AuthForm
from app.auth import auth_bp

from app import db

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = AuthForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        new_user = UserModel(
            username=username, # type: ignore
            password=generate_password_hash(password) # type:ignore
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    
    return render_template(
        'auth.html',
        form=form,
        title='Cadastro',
        action_url=url_for('auth.register'),
        submit_label='Registrar'
    )

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    form = AuthForm()
    if form.validate_on_submit():
        username = form.username.data or ''
        password = form.password.data or ''
        
        user = UserModel.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home.home'))
        
    return render_template(
        'auth.html',
        form=form,
        title='Login',
        action_url=url_for('auth.login'),
        submit_label='Entrar'
    )

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
