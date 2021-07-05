How to Use:
===========

* Create and activate a virtual environment:
    virtualenv venv
    
    venv\Scripts\Activate

* Install dependencies:
	pip install -r requirements.txt
	
* Run the GUI demo:
	python main.py --{%- if cookiecutter.gui_framework == 'PyQt5' %}pyqt5
{% elif cookiecutter.gui_framework == 'PyQt6' %}pyqt6
{% elif cookiecutter.gui_framework == 'PySide2' %}pyside2
{% elif cookiecutter.gui_framework == 'PySide6' %}pyside6
{%- endif %}
    
    
Note:
----
This Demo is taken from this repository: 
https://github.com/UN-GCPDS/qt-material


Sample:
----
Dark theme:
![dark](https://github.com/UN-GCPDS/qt-material/raw/master/docs/source/notebooks/_images/dark.gif)
Light theme:
![light](https://github.com/UN-GCPDS/qt-material/raw/master/docs/source/notebooks/_images/light.gif)
