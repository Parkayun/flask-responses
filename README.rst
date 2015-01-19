Flask-Responses 0.2
===================

.. image:: https://pypip.in/version/flask-responses/badge.svg
    :target: https://pypi.python.org/pypi/flask-responses/
    :alt: Latest Version

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
      return xml_response({"message": "Hello World!"}, headers={'x-foo': 'bar'}) # or can do this xml_response('<message>Hello World</message>')
      
   @app.route("/auto")
   def auto():
      return auto_response({"message": "Hello World!"}, status_code=201, headers={'x-foo': 'bar'})
       
Responses
---------
* JSON (json_response)
* XML (xml_response)

ToDo
----
* allow origin cross domain
* server sent evnets
