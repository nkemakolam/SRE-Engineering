import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/mydatabase'
    B2C_TENANT = 'your-b2c-tenant'
    B2C_CLIENT_ID = 'your-b2c-client-id'
    B2C_REDIRECT_URI = 'http://localhost:5000/callback'
    B2C_SCOPES = ['openid', 'profile', 'offline_access']
    GOOGLE_CLIENT_ID = 'your-google-client-id'
