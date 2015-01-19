"""
Flask-Responses
---------------
Simple response utility for flask
"""

from os import path
from setuptools import setup

long_description = open(
    path.join(
        path.dirname(__file__),
        'README.rst'
    )
).read()

setup(
    name='Flask-Responses',
    version='0.2',
    url='https://github.com/Parkayun/flask-responses',
    license='BSD',
    author='Ayun Park',
    author_email='iamparkayun@gmail.com',
    description='Simple response utility for Flask',
    long_description=long_description,
    packages=['flask_responses'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=0.8',
        'dicttoxml',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='tests',
    tests_require=[
        'nose',
    ]
)
