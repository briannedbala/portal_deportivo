class DevelopmentConfig():
    DEBUG = True
    SECRET_KEY = 'lJqnL4lG4H'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'db_portal_deportivo'


config = {
    'development': DevelopmentConfig
}
