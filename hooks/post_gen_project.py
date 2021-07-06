# cat post_gen_project.py
import os
import shutil

print(os.getcwd())  # prints /absolute/path/to/{{cookiecutter.project_slug}}

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

use_poetry = '{{cookiecutter.use_poetry}}' == 'y'
keep_demo = '{{cookiecutter.keep_demo}}' == 'y'

if not use_poetry:
    # remove top-level file inside the generated folder
    remove('pyproject.toml')

if not keep_demo:
    # remove top-level file inside the generated folder
    remove('demo')

if 'Py' in '{{cookiecutter.gui_framework}}':
    remove('demo/tk')
    remove('demo/kivy_')

if '{{cookiecutter.gui_framework}}' == 'Tkinter':
    remove('demo/Tkinter')
    remove('demo/kivy_')

if '{{cookiecutter.gui_framework}}' == 'Kivy':
    remove('demo/Kivy')
    os.rename('demo/kivy_', 'demo/kivy')
    remove('demo/tk')
