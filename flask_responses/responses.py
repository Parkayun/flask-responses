# -*- coding:utf-8 -*-
from __future__ import absolute_import

from flask import Response
from flask import jsonify

from .utility import set_headers


def json_response(data, status_code=200, headers=None):
    res = jsonify(**data)
    res.status_code = status_code

    if isinstance(headers, dict):
        res = set_headers(res, headers)

    return res


def xml_response(data, status_code=200, headers=None):
    res = Response(data, mimetype='text/xml')
    res.status_code = status_code

    if isinstance(headers, dict):
        res = set_headers(res, headers)

    return res
