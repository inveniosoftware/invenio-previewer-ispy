# SPDX-FileCopyrightText: 2014, 2015 CERN
# SPDX-License-Identifier: MIT

"""Invenio previewer for ISPY visualisations."""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os
import re

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
    'Flask',
    'six',
    'Invenio',
]

test_requirements = [
    # TODO: put package test requirements here
    'nose',
    'coverage',
]

# Get the version string.  Cannot be done with import!
with open(os.path.join('invenio_previewer_ispy', 'version.py'), 'rt') as f:
    version = re.search(
        '__version__\s*=\s*"(?P<version>.*)"\n',
        f.read()
    ).group('version')

setup(
    name='invenio-previewer-ispy',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    keywords='invenio-previewer-ispy',
    license='MIT',
    author='Invenio collaboration',
    author_email='info@inveniosoftware.org',
    url='https://github.com/inveniosoftware/invenio-previewer-ispy',
    packages=[
        'invenio_previewer_ispy',
    ],
    package_dir={'invenio_previewer_ispy':
                 'invenio_previewer_ispy'},
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=requirements,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    test_suite='nose.collector',
    tests_require=test_requirements
)
