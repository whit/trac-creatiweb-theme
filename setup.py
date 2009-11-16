#!/usr/bin/env python

from setuptools import setup

setup(
    name = 'CreatiWebTheme',
    version = '1.0.9',
    packages = [ 'creatiwebtheme' ],
    package_data = { 'creatiwebtheme': [ 'htdocs/*.css', 'htdocs/*.png', 'htdocs/*.gif', 'templates/*.html' ] },
    author = 'Vitek Pliska',
    author_email = 'whit@jizak.cz',
    description = 'A theme for Trac based on http://creatiweb.cz',
    license = 'BSD',
    keywords = 'trac plugin theme',
    url = 'http://github.com/whit/trac-creatiweb-theme',
    classifiers = [
        'Framework :: Trac',
    ],
    install_requires = [ 'Trac', 'TracThemeEngine>=2.0' ],

    entry_points = {
        'trac.plugins': [
            'creatiwebtheme.theme = creatiwebtheme.theme',
        ]
    },
)

