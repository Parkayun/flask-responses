Flask-Responses
================

.. image:: https://secure.travis-ci.org/Parkayun/flask-responses.svg?branch=master
   :alt: Build Status
   :target: https://travis-ci.org/Parkayun/-responses

.. image:: https://img.shields.io/coveralls/Parkayun/flask-responses.svg
   :alt: Coverage Status
   :target: https://coveralls.io/r/dahliaParkayun/flask-responses

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
   from flask.ext.responses import json_response, xml_response

   app = Flask(__name__)

   @app.route("/json")
   def hello():
       return json_response({"message": "Hello World!"})
       
   @app.route("/xml")
   def world():
      from dicttoxml import dicttoxml # 3rd party packge (dict to xml)
      return xml_response(dicttoxml({"message": "Hello World!"}))
       
Responses
---------
* JSON (json_response)
* XML (xml_response)

ToDo
----
* Server Sent Evnets
