from flask import render_template

from app.home import home_bp

@home_bp.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html') 