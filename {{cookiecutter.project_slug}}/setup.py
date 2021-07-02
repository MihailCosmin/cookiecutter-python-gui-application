#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
{%- if cookiecutter.gui_framework == 'PyQt5' %}'PyQt5>=5.15.4',
{% elif cookiecutter.gui_framework == 'PyQt6' %}'PyQt6>=6.1.1',
{% elif cookiecutter.gui_framework == 'PySide2' %}'PySide2>=5.15.2',
{% elif cookiecutter.gui_framework == 'PySide6' %}'PySide6>=6.1.2',
{% elif cookiecutter.gui_framework == 'Kivy' %}'Kivy>=2.0.0',
{% elif cookiecutter.gui_framework == 'wxPython' %}'wxPython>=4.1.1',
{% elif cookiecutter.gui_framework == 'Pyforms' %}'Pyforms>=4.0.3',
{% elif cookiecutter.gui_framework == 'PySimpleGUI' %}'PySimpleGUI>=4.45.0',
{% elif cookiecutter.gui_framework == 'PyGTK' %}'PyGTK>=2.24.2',
{%- endif %}
]

test_requirements = [{%- if cookiecutter.use_pytest == 'y' %}'pytest>=3',{%- endif %} ]

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Win32 (MS Windows)',
        'Environment :: MacOS X',
        'Environment :: X11 Applications',
        'Environment :: Web Environment',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development',
        'Topic :: Communications :: Email',
        'Topic :: Office/Business',
    ],
    description="{{ cookiecutter.project_short_description }}",
    install_requires=requirements,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='{{ cookiecutter.project_slug }}',
    name='{{ cookiecutter.project_slug }}',
    packages=find_packages(include=['{{ cookiecutter.project_slug }}', '{{ cookiecutter.project_slug }}.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    zip_safe=False,
)
