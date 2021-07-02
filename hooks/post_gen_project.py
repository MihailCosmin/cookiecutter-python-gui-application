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
# create_file_one = '{{cookiecutter.create_file_one}}' == 'y'


if not use_poetry:
    # remove top-level file inside the generated folder
    remove('pyproject.toml')

'''
if not create_file_one:
    # remove absolute path to file nested inside the generated folder
    remove(os.path.join(os.getcwd(), '{{cookiecutter.package_name}}', 'file_one.py'))'''

