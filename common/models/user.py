# coding: utf-8

from application import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, info='primary key')
    nick_name = db.Column(db.String(30), nullable=False, info='nickname')
    login_name = db.Column(db.String(20), nullable=False, unique=True, info='login name')
    login_pwd = db.Column(db.String(32), nullable=False, info='login password')
    login_salt = db.Column(db.String(32), nullable=False, info='login password random character string')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='status:0:invalid 1:valid')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='last update time')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='insert time')
