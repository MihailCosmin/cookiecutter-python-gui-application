Cookiecutter Python GUI Application
===================================

Cookiecutter template for Python GUI Applications based on cookiecutter-pypackage: https://github.com/audreyfeldroy/cookiecutter-pypackage.

This template is mostly intended for beginners in GUI development using Python, but it can be used by experienced developers also.

Besides providing the template and the needed tools for GUI development, this repository also comes with demos for most used python GUI frameworks, in order to get you started, if you are a beginner.

Features
-----
* Free software: BSD license
* Dependency tracking using [poetry](https://python-poetry.org/ "poetry")
* [Pytest](http://pytest.org/ "Pytest") runner: Supports `unittest`, `pytest`, `nose` style tests and more
* [Travis-CI](http://travis-ci.org/"Travis-CI"): Ready for Travis Continuous integration testing
* [Tox](http://testrun.org/tox/ "Tox") testing: Setup to easily test for python 2.6, 2.7, 3.3 and PyPy_
* [Sphinx](http://sphinx-doc.org/ "Sphinx") docs: Documentation ready for generation with, for example, [ReadTheDocs](https://readthedocs.org/ "ReadTheDocs")
* [Wheel](http://pythonwheels.com "Wheel") support: Use the newest python package distribution standard from the get go


Supported GUI Frameworks
-----
* [PyQt5 and PyQt6](https://www.riverbankcomputing.com/static/Docs/PyQt6 "PyQt5 and PyQt6")
* [PySide2 and PySide6](https://doc.qt.io/qtforpython "PySide2 and PySide6")
* [tkinter](https://docs.python.org/3/library/tk.html "tkinter")
* [Kivy](https://kivy.org/doc/stable "Kivy")
* [wxPython](https://www.wxpython.org/ "wxPython")

Demos:
-----
* Qt family (PyQt5, PyQt6, PySide2, PySide6):

![Qt Demo](https://github.com/UN-GCPDS/qt-material/raw/master/docs/source/notebooks/_images/dark.gif)


* Tkinter:

![Text Editor](https://github.com/MihailCosmin/cookiecutter-python-gui-application/blob/main/%7B%7Bcookiecutter.project_slug%7D%7D/demo/tkinter_/text-editor.png)

* Kivy:

![Kivy](https://github.com/MihailCosmin/cookiecutter-python-gui-application/blob/main/%7B%7Bcookiecutter.project_slug%7D%7D/demo/kivy_/sample.gif)

* wxPython:

![Web Browser](https://github.com/MihailCosmin/cookiecutter-python-gui-application/blob/main/%7B%7Bcookiecutter.project_slug%7D%7D/demo/wxPython_/demo.gif)

Usage
-----

Generate a Python GUI Application project::

    cookiecutter https://github.com/MihailCosmin/cookiecutter-python-gui-application.git

Not Exactly What You Want?
--------------------------

Don't worry, you have options:

Similar Cookiecutter Templates
------------------------------

* [audreyr/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage "audreyr/cookiecutter-pypackage"): The original pypackage.

Fork This
---------

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Once you have your fork working, add it to the
Similar Cookiecutter Templates list with a brief explanation. It's up to you
whether or not to rename your fork.

Or Submit a Pull Request
------------------------

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.
