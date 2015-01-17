Flask-Responses
================

.. module:: flask.ext.responses

Simple response utility for `Flask`.

.. _Flask: http://flask.pocoo.org/

Installation
-------------

.. sourcecode:: bash

   ~ $ python setup.py install

Quick start
-----------

.. sourcecode:: python

   from flask import Flask
   from flask.ext.responses import json_response

   app = Flask(__name__)

   @app.route("/")
   def hello():
       return json_response({"message": "Hello World!"})
