# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Lab1(Base):
    __tablename__ = 'lab_1'

    id = Column(INTEGER(11), primary_key=True, unique=True,autoincrement=True)
    name = Column(String(100))
    category = Column(String(100))
    type = Column(String(100))
    priority = Column(String(50))


class LabNeed(Base):
    __tablename__ = 'lab_needs'

    id = Column(INTEGER(11), primary_key=True, unique=True)
    submitter = Column(String(50))
    status = Column(String(60), index=True)
    sys = Column(String(60))
    module = Column(String(60))
    priority = Column(String(60))
    key_word = Column(String(60))
    situation = Column(String(500))
    detail = Column(String(500))
    create_date = Column(DateTime)


class LabStatu(Base):
    __tablename__ = 'lab_status'

    id = Column(INTEGER(11), primary_key=True, unique=True)
    name = Column(String(60))


class Tag(Base):
    __tablename__ = 'tag'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(20))


class User(Base):
    __tablename__ = 'user'

    id = Column(INTEGER(11), primary_key=True)
    username = Column(String(10))
    phone = Column(String(11))


class Article(Base):
    __tablename__ = 'article'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(String(20))
    author_id = Column(ForeignKey('user.id'), index=True)

    author = relationship('User')


class ActicleTag(Base):
    __tablename__ = 'acticle_tag'

    id = Column(INTEGER(11), primary_key=True)
    article_id = Column(ForeignKey('article.id'), index=True)
    tag_id = Column(ForeignKey('tag.id'), index=True)

    article = relationship('Article')
    tag = relationship('Tag')
