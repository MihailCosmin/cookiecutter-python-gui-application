===================================
Cookiecutter Python GUI Application
===================================

Cookiecutter template for Python GUI Applications based on cookiecutter-pypackage: https://github.com/audreyfeldroy/cookiecutter-pypackage.

This template is mostly intended for beginners in GUI development using Python, but it can be used by experienced developers also.

Besides providing the template and the needed tools for GUI development, this repository also comes with demos for every python GUI framework, in order to get you started, if you are a beginner.

Features
-----
* Free software: BSD license
* Dependency tracking using poetry_
* Pytest_ runner: Supports `unittest`, `pytest`, `nose` style tests and more
* Travis-CI_: Ready for Travis Continuous integration testing
* Tox_ testing: Setup to easily test for python 2.6, 2.7, 3.3 and PyPy_
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_
* Wheel_ support: Use the newest python package distribution standard from the get go


Supported GUI Frameworks
-----
* PyQt5 and PyQt6_
* PySide2 and PySide6_
* tkinter_
* Kivy_
* wxPython_

Demos:
-----
* Qt family (PyQt5, PyQt6, PySide2, PySide6):
Dark theme:
![dark](https://github.com/UN-GCPDS/qt-material/raw/master/docs/source/notebooks/_images/dark.gif)
Light theme:
![light](https://github.com/UN-GCPDS/qt-material/raw/master/docs/source/notebooks/_images/light.gif)

* Tkinter:
![Text Editor]({{cookiecutter.project_slug}}\demo\tkinter_\text-editor.png)

* Kivy:
![Kivy]({{cookiecutter.project_slug}}\demo\kivy_\sample.gif)

* wxPython:
![Web Browser]({{cookiecutter.project_slug}}\demo\wxPython_\demo.gif)

Usage
-----

Generate a Python GUI Application project::

    cookiecutter https://github.com/MihailCosmin/cookiecutter-python-gui-application.git

Not Exactly What You Want?
--------------------------

Don't worry, you have options:

Similar Cookiecutter Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `audreyr/cookiecutter-pypackage`_: The original pypackage.

Fork This
~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Once you have your fork working, add it to the
Similar Cookiecutter Templates list with a brief explanation. It's up to you
whether or not to rename your fork.

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.

.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.org/
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyfeldroy/cookiecutter-pypackage
.. _Pytest: http://pytest.org/
.. _PyPy: http://pypy.org/
.. _Wheel: http://pythonwheels.com
.. _Poetry: https://python-poetry.org/
.. _PyQt6: https://www.riverbankcomputing.com/static/Docs/PyQt6/
.. _PySide6: https://doc.qt.io/qtforpython/
.. _tkinter: https://docs.python.org/3/library/tk.html
.. _Kivy: https://kivy.org/doc/stable/
.. _wxPython: https://www.wxpython.org/