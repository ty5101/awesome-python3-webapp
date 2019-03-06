#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'tanyou'

import time, uuid

from orm import Model,StringField,BooleanField,FloatFeild,TextFeild


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True,defalut=next_id,ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatFeild(defalut=time.time)

class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True,defalut=next_id,ddl='varchar(50)')
    user_id = StringField(ddl='varcahr(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name =StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextFeild()
    created_at = FloatFeild(defalut=time.time)

class Comment(Model):
    __table__ = 'commments'

    id = StringField(primary_key=True,defalut=next_id,ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(50)')
    content = TextFeild()
    created_at = FloatFeild(defalut=time.time)