# coding: utf-8

"""
    Quickpac API

    Here you will find all public interfaces to the Quickpac system.  # noqa: E501

    OpenAPI spec version: v1.00
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Quickpac API",
    author_email="",
    url="",
    keywords=["Swagger", "Quickpac API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Here you will find all public interfaces to the Quickpac system.  # noqa: E501
    """
)