===================================
cookiecutter-python-gui-application
===================================

Cookiecutter template for a Python GUI Application based on cookiecutter-pypackage: https://github.com/audreyr/cookiecutter .

This template is mostly intended for beginners in GUI development using Python, but it can be used by experienced developers also.

Besides providing the template and the needed tools for GUI development, this repository also comes with demos for every python GUI framework in order to get you started if you are a beginner.


* Free software: BSD license
* Dependency tracking using poetry_
* Pytest_ runner: Supports `unittest`, `pytest`, `nose` style tests and more
* Travis-CI_: Ready for Travis Continuous integration testing
* Tox_ testing: Setup to easily test for python 2.6, 2.7, 3.3 and PyPy_
* Sphinx_ docs: Documentation raedy for generation with, for example, ReadTheDocs_
* Wheel_ support: Use the newest python package distribution standard from the get go


Supported GUI Frameworks
-----
* PyQt5 and PyQt6_
* PySide2 and PySide6_
* tkinter_
* Kivy_
* Pyforms_
* PySimpleGUI_
* PyGTK_


Usage
-----

Generate a Python package project::

    cookiecutter https://github.com/MihailCosmin/cookiecutter-python-gui-application.git

Then:

* Create a repo and put it there.
* Add the repo to your Travis CI account.
* Add the repo to your ReadTheDocs account + turn on the ReadTheDocs service hook.
* Run `tox` to make sure all tests pass.
* Release your package the standard Python way.

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
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter
.. _Pytest: http://pytest.org/
.. _PyPy: http://pypy.org/
.. _Wheel: http://pythonwheels.com
.. _Poetry: https://python-poetry.org/
.. _PyQt6: https://www.riverbankcomputing.com/static/Docs/PyQt6/
.. _PySide6: https://doc.qt.io/qtforpython/
.. _tkinter: https://docs.python.org/3/library/tk.html
.. _Kivy: https://kivy.org/doc/stable/
.. _Pyforms: https://pyforms.readthedocs.io/en/v4/
.. _PySimpleGUI: https://pysimplegui.readthedocs.io/en/latest/
.. _PyGTK: https://python-gtk-3-tutorial.readthedocs.io/en/latest/
