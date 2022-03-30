#!/usr/bin/env python
import pathlib
import pkg_resources
"""
The setup script.
usage: python setup.py install
"""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with pathlib.Path('requirements.txt').open() as requirements_txt:
    requirements = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

test_requirements = ['pytest>=3', ]

setup(
    author="Stan Chen",
    author_email='stanchensz@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Bringing quantitative trading to the masses!",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='deeptendies',
    name='deeptendies',
    packages=find_packages(include=['deeptendies', 'deeptendies.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/stancsz/deeptendies',
    version='0.1.0',
    zip_safe=False,
)
