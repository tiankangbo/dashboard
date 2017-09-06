#!/usr/bin/env python
# coding: utf-8
import web

db = web.database(dbn='mysql', db='task', user='root', pw='pa$$w0rd')

render = web.template.render('templates/', cache=False)
#打开工程调试模式
web.config.debug = True

config = web.storage(
    email='tiankangbo@gmail.com',
    site_name = '任务清单',
    site_desc = 'For learn web.py',
    static = '/static',
)


web.template.Template.globals['config'] = config
web.template.Template.globals['render'] = render
