DEBUG = True
TESTING = False

SERVER = "dev"
DB_HOST = "mongodb://localhost:27017"
DB_NAME = "inventorydb"
DB_USERNAME = "inventorydbusername"
DB_PASSWORD = "inventorydbpassword"
MONGODB_CONNSTRING = "mongodb://%s:%s@localhost:27017/?authSource=%s" % (DB_USERNAME, DB_PASSWORD,DB_NAME)
DATA_PATH = "/data/inventory"
MAX_CONTENT_LENGTH = 16 * 1000 * 1000

SECRET_KEY = ""
JWT_SECRET_KEY = ""
SESSION_COOKIE_SECURE = True
JWT_TOKEN_LOCATION = ['cookies']
JWT_COOKIE_SECURE = False
JWT_ACCESS_COOKIE_PATH = '/'
JWT_REFRESH_COOKIE_PATH = '/'
JWT_COOKIE_CSRF_PROTECT = True
JWT_CSRF_IN_COOKIES = False

    



