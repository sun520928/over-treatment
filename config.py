from logging.config import dictConfig

DB_USER = 'gpadmin'
DB_PWD = 'gpadmin'
DB_NAME = 'cdrdb'
DB_IP = '10.7.100.17'
DB_PORT = '5432'

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


class BaseConfig(object):
    #SESSION_TYPE = 'redis'  # session类型为redis
    #SESSION_KEY_PREFIX = 'session:'  # 保存到session中的值的前缀
    #SESSION_PERMANENT = False  # 如果设置为True，则关闭浏览器session就失效。
    #SESSION_USE_SIGNER = False  # 是否对发送到浏览器上 session:cookie值进行加密

    #SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://%s:%s@%s/%s'% (DB_USER, DB_PWD, DB_IP, DB_PORT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s'% (DB_USER, DB_PWD, DB_IP, DB_PORT, DB_NAME)
    SQLALCHEMY_POOL_SIZE = 2
    SQLALCHEMY_POOL_TIMEOUT = 30
    SQLALCHEMY_POOL_RECYCLE = -1
    # 追踪对象的修改并且发送信号
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    pass


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass

