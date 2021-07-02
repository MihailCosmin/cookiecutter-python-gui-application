"""Main module."""

{% if cookiecutter.gui_framework == 'PyQt5' -%}

import sys
from PyQt5.QtWidgets import QApplication, QWidget


def main():

    app = QApplication(sys.argv)

    w = QWidget()
    w.setWindowTitle('{{ cookiecutter.project_name }}')
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


{% endif %}