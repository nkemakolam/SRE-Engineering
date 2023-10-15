from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user

from .models import db, Article
from .auth import login_manager

main = Blueprint('main', __name__)

@main.route('/')
def index():
    articles = Article.query.all()
    return render_template('view.html', articles=articles)

@main.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        article = Article(title=title, content=content, user_id=current_user.id)
        db.session.add(article)
        db.session.commit()
        flash('Article posted!', 'success')
    return render_template('post.html')

@login_manager.unauthorized_handler
def unauthorized():
    flash('You must be logged in to access this page.', 'danger')
    return redirect(url_for('auth.azure_b2c'))
