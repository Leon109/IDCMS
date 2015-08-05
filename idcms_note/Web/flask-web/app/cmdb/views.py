#coding=utf-8
from flask import render_template, redirect, url_for
from flask.ext.login import login_required
from . import cmdb

@cmdb.route('/', methods=['GET'])
@login_required
def index():
    return redirect(url_for('cmdb.cmdb'))
    
@cmdb.route('/cmdb', methods=['GET', 'POST'])
@login_required
def cmdb():
    return render_template('cmdb/cmdb.html')
