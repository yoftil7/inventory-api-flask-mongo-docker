DEBUG = False
TESTING = False


TOTP_INTERVAL = 3600
MAIL_USE_TLS = False 
MAIL_USE_SSL = False
MAIL_USERNAME = None
MAIL_PASSWORD = None

SECRET_KEY = ""
JWT_SECRET_KEY = ""
SESSION_COOKIE_SECURE = True
JWT_TOKEN_LOCATION = ['cookies']
JWT_COOKIE_SECURE = False
JWT_ACCESS_COOKIE_PATH = '/'
JWT_REFRESH_COOKIE_PATH = '/'
JWT_COOKIE_CSRF_PROTECT = True
JWT_CSRF_IN_COOKIES = False
