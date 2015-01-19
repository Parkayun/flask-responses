# -*- coding:utf-8 -*-

def set_headers(res, headers):
    for key, value in headers.items():
        res.headers.add(key, value)
    return res
