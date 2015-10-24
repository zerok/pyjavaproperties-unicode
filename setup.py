import os

from setuptools import setup

setup(
    name='pyjavaproperties-unicode',
    version='0.1.1',
    author='Horst Gutmann',
    author_email='horst@zerokspot.com',
    py_modules=['pyjavapropertiesu'],
    install_requires=[
        'pyjavaproperties >= 0.6'
    ],
    license='MIT',
    url='https://github.com/zerok/pyjavaproperties-unicode',
    description='A small wrapper around pyjavaproperties to add unicode '
                'support.',
    long_description=open(os.path.join(os.path.dirname(__file__),
                                       'README.rst')).read(),
)
