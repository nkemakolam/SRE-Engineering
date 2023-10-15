from flask import Blueprint, redirect, url_for
from flask_dance.contrib.azure_b2c import make_azure_b2c_blueprint
from flask_dance.contrib.google import make_google_blueprint
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin
from flask_login import login_user, login_required, current_user

from .models import db, User

auth = Blueprint('auth', __name__)

azure_b2c_bp = make_azure_b2c_blueprint(
    client_id=config.B2C_CLIENT_ID,
    redirect_to='auth.azure_b2c_login',
    redirect_url=config.B2C_REDIRECT_URI,
    scope=config.B2C_SCOPES
)

google_bp = make_google_blueprint(client_id=config.GOOGLE_CLIENT_ID, redirect_to='auth.google_login')

@auth.route('/azure-b2c-login')
def azure_b2c_login():
    if not azure_b2c_bp.session.authorized:
        return redirect(url_for('auth.azure_b2c'))

    resp = azure_b2c_bp.session.get('/v1.0/me')
    if resp.ok:
        user_info = resp.json()
        user = User.query.filter_by(email=user_info['upn']).first()
        if user is None:
            user = User(email=user_info['upn'])
            db.session.add(user)
            db.session.commit()
        login_user(user)
    return redirect(url_for('index'))
