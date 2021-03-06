Flask-Responses 0.2
===================

.. image:: http://badge.kloud51.com/pypi/v/flask-responses.svg
    :alt: Latest Version
    :target: https://pypi.python.org/pypi/flask-responses/

.. image:: https://secure.travis-ci.org/Parkayun/flask-responses.svg?branch=master
   :alt: Build Status
   :target: https://travis-ci.org/Parkayun/flask-responses

.. image:: https://img.shields.io/coveralls/Parkayun/flask-responses.svg
   :alt: Coverage Status
   :target: https://coveralls.io/r/Parkayun/flask-responses

.. module:: flask.ext.responses

Simple response utility for `Flask`.

.. _Flask: http://flask.pocoo.org/

Installation
-------------

.. sourcecode:: bash

   ~ $ python setup.py install
   
or can use pip

.. sourcecode:: bash

   ~ $ pip install flask-responses

Quick start
-----------

.. sourcecode:: python

   from flask import Flask
   from flask.ext.responses import json_response, xml_response, auto_response

   app = Flask(__name__)

   @app.route("/json")
   def hello():
       return json_response({"message": "Hello World!"}, status_code=201)
       
   @app.route("/xml")
   def world():
      # or can do this return xml_response('<message>Hello World</message>')
      return xml_response({"message": "Hello World!"}, headers={'x-foo': 'bar'}) 
      
   @app.route("/auto")
   def auto():
      # auto response json or xml by Accept request header
      return auto_response({"message": "Hello World!"}, status_code=201, headers={'x-foo': 'bar'})
       
Responses
---------
* JSON (json_response)
* XML (xml_response)

ToDo
----
* allow origin cross domain
* server sent events
