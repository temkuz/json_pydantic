from setuptools import setup, find_packages

NAME = 'json_pydantic'
VERSION = '1.1.0'
AUTHOR = 'temkuz'
AUTHOR_EMAIL = 'temkuz@yandex.ru'
DESCRIPTION = 'Utility for converting json files to Pydantic models'

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    packages=find_packages(),
    url='https://github.com/temkuz/json_pydantic',
    entry_points={
        'console_scripts': [
            'json_pydantic = json_pydantic.__main__:main'
        ]
    },
    install_requires=[
        'Jinja2==3.1.2'
    ]
)
