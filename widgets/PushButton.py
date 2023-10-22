from PyQt5.QtWidgets import QPushButton


class PushButton(QPushButton):
    def __init__(self, parent = None,  ico=None):

        if(ico):
            super().__init__(parent, icon=ico)
        else:
            super().__init__(parent)


        self.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(51,51,51);\n"
"    border-radius: 5px;    \n"
"    color:rgb(255,255,255);\n"
"    background-color: rgb(51,51,51);\n"
"    font-size: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(0,143,150);\n"
"    background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {    \n"
"    border: 2px solid rgb(0,143,150);\n"
"    background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {    \n"
"    border-radius: 5px;    \n"
"    border: 2px solid rgb(112,112,112);\n"
"    background-color: rgb(112,112,112);\n"
"}")