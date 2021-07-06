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
install_demo = '{{cookiecutter.install_demo}}' == 'y'

if not use_poetry:
    # remove top-level file inside the generated folder
    remove('pyproject.toml')

if not install_demo:
    # remove top-level file inside the generated folder
    remove('demo')

if '{{cookiecutter.gui_framework}}' == 'Tkinter':
    remove('demo/Tkinter')
