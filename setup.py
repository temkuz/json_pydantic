from setuptools import setup, find_packages

NAME = 'json_pydantic'
VERSION = '1.0.0'
AUTHOR = 'temkuz'
AUTHOR_EMAIL = 'temkuz@yandex.ru'

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(
        where='.',
    ),
    entry_points={
        'console_scripts': [
            'json_pydantic = json_pydantic.__main__:main'
        ]
    }
)
