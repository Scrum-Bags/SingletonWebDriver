from setuptools import setup
from setuptools import find_packages

setup(
    name='singleton_web_driver',
    version='0.0.5',
    author="Doug Walter",
    author_email="doug.walter@smoothstack.com",
    license="Apache 2.0",
    packages=find_packages(
        include=[
            'singleton_web_driver.*'
        ]
    ),
    install_requires=[
        'selenium'
    ]
)