from PyQt5.QtWidgets import QLineEdit


class LineEdit(QLineEdit):
    def __init__(self, st):
        super().__init__(st)

        self.setStyleSheet("QLineEdit {\n"
"    color:rgb(255,255,255);\n"
"    border:4px solid rgb(51,51,51);\n"
"    border-radius:4px;\n"
"    background:rgb(51,51,51);\n"
"    font-size : 14px;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    color:rgb(255,255,255);\n"
"    border:2px solid rgb(112,112,112);\n"
"    border-radius:4px;\n"
"    background:rgb(112,112,112);\n"
"}")
        self.setFocus()

