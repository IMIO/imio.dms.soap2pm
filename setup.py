# -*- coding: utf-8 -*-
"""Installer for the imio.dms.soap2pm package."""

from setuptools import find_packages
from setuptools import setup


long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')


setup(
    name='imio.dms.soap2pm',
    version='0.1',
    description="Dsm soap client method",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='',
    author='sgeulette',
    author_email='support@imio.be',
    url='http://pypi.python.org/pypi/imio.dms.soap2pm',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['imio', 'imio.dms'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'five.grok',
        'plone.api',
        'setuptools',
        'imio.dms.mail',
        'imio.pm.wsclient',
    ],
    extras_require={
        'test': [
            'ecreall.helpers.testing',
            'plone.app.testing',
            'plone.app.robotframework',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)