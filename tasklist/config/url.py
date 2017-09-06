#!/usr/bin/env python
# coding: utf-8

pre_fix = 'controllers.'

urls = (
    '/',                    pre_fix + 'task.Index',
    '/task/new',            pre_fix + 'task.New',
    '/task/(\d+)',          pre_fix + 'task.View',
    '/task/(\d+)/edit',     pre_fix + 'task.Edit',
    '/task/(\d+)/delete',   pre_fix + 'task.Delete',
    '/task/(\d+)/finish',   pre_fix + 'task.Finish',

)
