#-*- coding:utf-8 -*-
class Config(object):
    """基础（base）配置类"""
    pass
class ProdConfig(Config):
    """生产（production）环境配置类"""
    pass
class DevConfig(Config):
    """开发（development）环境配置类"""
    DEBUG = True
    # MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:lyu19910409@127.0.0.1:3306/lab_blog'