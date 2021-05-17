from setuptools import setup
import os
import datetime

setup(
    name='django-test',
    version='1.0',
    description='django-test',
    author='NICT',
    author_email='masao.ideuchi [at] nict.go.jp',
    description="Calling test for NICT translator API via Heroku REST API",
    packages=['django-test'],
    url="https://github.com/ideuchi/django-test",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['django_test = django-test.setup:test']
    },
    install_requires=['django', 'djangorestframework', 'django-filter', 'gunicorn'],
    python_requires='>=3.7',
    scripts=[
             'debug_message_file/setup_test',
            ]
)

def test():
    time = datetime.datetime.now()
    str_time = time.strftime('%Y/%m/%d %H:%M:%S')
    message = str_time+' test() in setup.py called.\n'
    with open('debug.txt', 'a') as f:
        print(message, file=f)
    print(message)

