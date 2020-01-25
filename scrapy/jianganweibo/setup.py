# Automatically created by: shub deploy

from setuptools import setup, find_packages

setup(
    name         = 'project',
    version      = '1.4',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = jianganweibo.settings']},
)
