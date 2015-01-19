# -*- coding:utf-8 -*-
from __future__ import absolute_import

from flask import Response
from flask import request
from flask import jsonify

from .utility import set_headers


def json_response(data, status_code=200, headers=None):
    res = jsonify(**data)
    res.status_code = status_code

    if isinstance(headers, dict):
        res = set_headers(res, headers)

    return res


def xml_response(data, status_code=200, headers=None):
    if isinstance(data, dict):
        from dicttoxml import dicttoxml
        data = dicttoxml(data)

    res = Response(data, mimetype='text/xml')
    res.status_code = status_code

    if isinstance(headers, dict):
        res = set_headers(res, headers)

    return res


def auto_response(*args, **kwargs):
    mime_types = ['application/json', 'application/xml', 'text/html']
    accept_mime_types = request.accept_mimetypes
    accept_type = accept_mime_types.best_match(mime_types)

    if accept_type == mime_types[0]:
        return json_response(*args, **kwargs)
    elif accept_type == mime_types[1]:
        return xml_response(*args, **kwargs)

    data = str(args[0]) if isinstance(args[0], dict) else args
    return data
