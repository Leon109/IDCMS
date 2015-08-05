#coding=utf-8

import os
import sys

from flask.ext.wtf import Form
from wtforms import StringField, SelectField
from wtforms import ValidationError
from wtforms.validators import Required, Length

workdir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, workdir + "/../../../")

from app.models import  Site

class SiteForm(Form):
    site = StringField(u'机房名称', validators=[Required(message=u'机房名不能为空'), 
        Length(1, 64, message=u'机房名为1-64个字符')])
    isp = StringField(u'ISP', validators=[Length(1, 64, message=u'ISP为1-64个字符')])
    location = StringField(u'所在城市', validators=[Length(1, 64, message=u'所在城市为1-64个字符')])
    address = StringField(u'详细地址', validators=[Length(1, 64, message=u'详细地址为1-64个字符')])
    contact = StringField(u'联系方式', validators=[Length(1, 64, message=u'联系方式为1-64个字符')])
    remark = StringField(u'备注')
    
    def validate_site(self, field):
        '''如果这么写，wtf会自动监测这个问题'''
        if Site.query.filter_by(site=field.data).first():
            raise ValidationError(u'机房已经添加,不能再次添加')
