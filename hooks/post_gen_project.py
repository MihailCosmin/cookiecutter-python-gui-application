# cat post_gen_project.py
import os
import shutil

print(os.getcwd())  # prints /absolute/path/to/{{cookiecutter.project_slug}}

def remove(filepath: str):
    """Remove a file or a directory.

    Args:
        filepath (str): Path to the file or directory to remove.
    """
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
else:
    if '{{cookiecutter.gui_framework}}'.startswith('PySide') or '{{cookiecutter.gui_framework}}'.startswith('PyQt'):
        remove('demo/tkinter_')
        remove('demo/kivy_')
        remove('demo/wxPython_')
        remove('demo/pysimplegui_')

    if '{{cookiecutter.gui_framework}}' == 'Tkinter':
        remove('demo/Tkinter')
        os.rename('demo/tkinter_', 'demo/tkinter')
        remove('demo/kivy_')
        remove('demo/wxPython_')
        remove('demo/pysimplegui_')

    if '{{cookiecutter.gui_framework}}' == 'Kivy':
        remove('demo/Kivy')
        os.rename('demo/kivy_', 'demo/kivy')
        remove('demo/tkinter_')
        remove('demo/wxPython_')
        remove('demo/pysimplegui_')

    if '{{cookiecutter.gui_framework}}' == 'wxPython':
        remove('demo/wxPython')
        os.rename('demo/wxPython_', 'demo/wxPython')
        remove('demo/tkinter_')
        remove('demo/kivy_')
        remove('demo/pysimplegui_')

    if '{{cookiecutter.gui_framework}}' == 'PySimpleGUI':
        remove('demo/PySimpleGUI')
        os.rename('demo/pysimplegui_', 'demo/PySimpleGUI')
        remove('demo/tkinter_')
        remove('demo/kivy_')
        remove('demo/wxPython_')
