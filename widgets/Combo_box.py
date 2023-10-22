from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtGui import QDoubleValidator
from widgets.LineEdit import LineEdit
from widgets.PushButton import PushButton
import math
class ComboBox_Equation(QComboBox):

    def __init__(self) -> None:
        super().__init__()
        
        self.actions = [ComboBox_Equation.on_action_0,
                            ComboBox_Equation.on_action_1,
                            ComboBox_Equation.on_action_2,
                            ComboBox_Equation.on_action_3,
                            ComboBox_Equation.on_action_4,
                            ComboBox_Equation.on_action_5] 
        texts = ["Остановочный путь (S) автомобиля без торможения ",
                 "Скорость по следам",
                 "Формула 3",
                 "Формула 4",
                 "Формула 5",
                 "И так далее"]
        for item in texts:
            self.addItem(item)
            self.setItemData(self.count() - 1, item, role=Qt.ToolTipRole)  # Устанавливаем ToolTip для каждого элемента
        self.setStyleSheet("QComboBox {\n"
"    border: 4px solid rgb(51,51,51);\n"
"    border-radius: 4px;    \n"
"    color:rgb(255,255,255);\n"
"    background-color: rgb(51,51,51);\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 2px solid rgb(0,143,170);\n"
"    border-radius: 5px;    \n"
"    color:rgb(255,255,255);\n"
"    background-color: rgb(0,143,170);\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"    background: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/1x/arrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"") 
    
    def on_action_0(ui, s, document, word):
        
        latex_formula = r'$S_{0}=(t_{1} + t_{2} + 0.5\cdot t_{3})\cdot\frac{V_{a}}{3.6} + \frac{V^{2}_{a}}{26\cdot j_{a}}$'
        ui.ready_doc_but.setText("")


        ui.gridLayout.addWidget(formula_picture(ui, latex_formula, s), 1, s)
        if ui.gridLayout.itemAtPosition(2, s) is not None:                  
            for row in range(ui.gridLayout.itemAtPosition(2, s).rowCount()):
                for col in range(ui.gridLayout.itemAtPosition(2, s).columnCount()):
                    if(ui.gridLayout.itemAtPosition(2, s).itemAtPosition(row, col) is not None):
                        w = ui.gridLayout.itemAtPosition(2, s).itemAtPosition(row, col).widget()
                        w.deleteLater()

        if ui.gridLayout.itemAtPosition(2, s) is not None:
            ui.gridLayout.removeItem(ui.gridLayout.itemAtPosition(2, s))

        form = QGridLayout()
        
        labels = [formula_picture(ui, r'$V_{a}$ =', s, font=10), 
                 formula_picture(ui, r'$t_{1}$ =', s, font=10),
                 formula_picture(ui, r'$t_{2}$ =', s, font=10),
                 formula_picture(ui, r'$t_{3}$ =', s, font=10),
                 formula_picture(ui, r'$j_{a}$ =', s, font=10)]
        edits = [LineEdit(""), 
                 LineEdit(""), 
                 LineEdit(""),
                 LineEdit(""),
                 LineEdit("")]
        senses = [formula_picture(ui, r'$км/ч$ ', s, font=10), 
                 formula_picture(ui, r'$с$ ', s, font=10),
                 formula_picture(ui, r'$с$ ', s, font=10),
                 formula_picture(ui, r'$с$ ', s, font=10),
                 formula_picture(ui, r'$м/с^2$ ', s, font=10)]

        def result():

            if(edits[0].text() and edits[1].text() and edits[2].text() and edits[3].text() and edits[4].text()):
                ui.ready_doc_but.setText("")
                try:
                    solution = (float(edits[1].text().replace(',','.')) + float(edits[2].text().replace(',','.')) + 0.5*float(edits[3].text().replace(',','.')))*(float(edits[0].text().replace(',','.'))/3.6) + (float(edits[0].text().replace(',','.'))**2)/(26*float(edits[4].text().replace(',','.')))
                except Exception:
                    return
                result = r""" Остановочный путь \(S_{0}\) автомобиля в условиях места происшествия определяется по формуле:\\
                                \(S_{0}=(t_{1} + t_{2} + 0.5\cdot t_{3})\cdot\frac{V_{a}}{3.6} + \frac{V^{2}_{a}}{26\cdot j_{a}}\)\\"""
                
                result+= r"где: \(V_{a}\) -- скорость движения ТС, км/ч: " + edits[0].text()+ r";\\"
                result+= r"\(t_{1}\) -- время реакции водителя автомобиля для сложившейся дорожной обстановки, с: " + edits[1].text() +  r";\\"
                result+= r"\(t_{2}\) -- время запаздывания срабатывания тормозного привода  водителя автомобиля, с: " + edits[2].text() + r";\\"
                result+= r"\(t_{3}\) -- время нарастания замедления для заданных дорожных условий, с: " + edits[3].text() + r";\\"
                result+= r"\(j_{a}\) -- установившееся замедление технически исправного ТС при экстренном торможении на горизонтальном участке дороги с сухим асфальтированным покрытием и заданной нагрузке, \(м/с^2\): " + edits[3].text()+ r";\\"

                
                formula = "\(S_{0}=(" + edits[1].text() + "+" + edits[2].text() + "+" + r"0.5\cdot " + edits[3].text()+ r")\cdot\frac{" + edits[0].text()+r"}{3.6} + \frac{"+ edits[0].text()+r"^{2}}{26\cdot " + edits[4].text() + r"} м\)\\"
                result+=formula
                temp = r"Величина \(S_{0}\) определяется равной " + str(round(solution, 2)) + r" м. \\ \\ \\"
                result+=temp
                word[0]= result
                form.addWidget(formula_picture(ui, r'$ S_{0} = ' + str(round(solution, 2))+ r' м$ ', s, font=11), 5, 0, 1, 2)
                form.addWidget(PushButton("О формуле"), 6, 0, 1, 1)

        for i in range(5):
            edits[i].setValidator(QDoubleValidator(-100, 300, 2))
            edits[i].textChanged.connect(result)
            
            form.addWidget(labels[i], i, 0)
            form.addWidget(edits[i], i, 1)
            form.addWidget(senses[i], i, 2)
        
        
        
        ui.gridLayout.addLayout(form, 2, s)
        
        

    def on_action_1(ui, s, document, word):#
        latex_formula = r'$V_{a}=1,8\cdot t_{3}\cdot j_{a} + \sqrt{26 \cdot j_{a}\cdot (S_{ю} - B)};$'

        ui.ready_doc_but.setText("")
        ui.gridLayout.addWidget(formula_picture(ui, latex_formula, s), 1, s)
        if ui.gridLayout.itemAtPosition(2, s) is not None:                  
                for row in range(ui.gridLayout.itemAtPosition(2, s).rowCount()):
                    for col in range(ui.gridLayout.itemAtPosition(2, s).columnCount()):
                        if(ui.gridLayout.itemAtPosition(2, s).itemAtPosition(row, col) is not None):
                            w = ui.gridLayout.itemAtPosition(2, s).itemAtPosition(row, col).widget()
                            w.deleteLater()

        if ui.gridLayout.itemAtPosition(2, s) is not None:
            ui.gridLayout.removeItem(ui.gridLayout.itemAtPosition(2, s))

        
        form = QGridLayout()
        
        labels = [formula_picture(ui, r'$t_{3}$ =', s, font=10),
                 formula_picture(ui, r'$j_{a}$ =', s, font=10),
                 formula_picture(ui, r'$S_{ю}$ =', s, font=10),
                 formula_picture(ui, r'$B}$ =', s, font=10)]
        edits = [LineEdit(""), 
                 LineEdit(""),
                 LineEdit(""),
                 LineEdit("")]
        senses = [formula_picture(ui, r'$ c$ ', s, font=10), 
                 formula_picture(ui, r'$м/с^2$ ', s, font=10),
                 formula_picture(ui, r'$м$ ', s, font=10),
                 formula_picture(ui, r'$м$ ', s, font=10)]

        def result():

            if(edits[0].text() and edits[1].text() and edits[2].text() and edits[3].text()):
                ui.ready_doc_but.setText("")
                try:
                    solution = (1.8*float(edits[0].text().replace(',','.'))*float(edits[1].text().replace(',','.'))) + math.sqrt(26*float(edits[1].text().replace(',','.'))*(float(edits[2].text().replace(',','.')) - float(edits[3].text().replace(',','.'))))
                except Exception:
                    return
                result = r""" Скорость перед применением водителем автомобиля ТС экстренного торможения при заданных в постановлении и представленных 
                материалах условиях и исходных данных, соответствующая следам торможения, может быть определена по формуле:\\ 
                                \( V_{a}=1,8\cdot t_{3}\cdot j_{a} + \sqrt{26 \cdot j_{a}\cdot (S_{ю} - B)}\)\\"""
                
                result+= r"где: \(t_{3}\) -- время нарастания замедления ТC-1 для заданных дорожных условий, с: " + edits[0].text()+ r";\\"
                result+= r"\(j_{a}\) -- установившееся замедление технически исправного ТС-1 при торможении на горизонтальном участке дороги с сухим асфальтированным покрытием и заданной нагрузке, \(м/с^2\): " + edits[1].text() +  r";\\"
                result+= r"\(S_{a}\) -- полная длина следов торможения автомобиля ТС-1, м:  " + edits[2].text() + r";\\"
                result+= r"\(B\) -- база автомобиля, м: " + edits[3].text() + r";\\"
                
                formula = r"\(V_{a}=1,8\cdot" + edits[0].text() + r"\cdot" + edits[1].text() + "+" + r"\sqrt{26 \cdot " + edits[1].text()+ r"\cdot (" + edits[2].text() + r"-"+ edits[3].text()+r")} км/ч;\)\\"
                result+=formula
                temp = r"Представленная величина расчетной скорости \(V_{a}\) = " + str(round(solution, 2)) + r" км/ч "
                ber = r"""является минимальной, поскольку непосредственно после контакта автомобиля с 
                пешеходом произошло падение кинетической энергии, затраченной 
                на деформацию кузова при наезде и дальнейшее перемещение автомобиля до конечной остановки без следообразования. \\ \\
                """
                temp+=ber
                result+=temp
                word[1]= result
                
                form.addWidget(formula_picture(ui, r'$ V_{a} = ' + str(round(solution, 2))+ r' км/ч$ ', s, font=11), 4, 0, 1, 2)
                form.addWidget(PushButton("О формуле"), 5, 0, 1, 1)

        for i in range(4):
            edits[i].setValidator(QDoubleValidator(-100, 300, 2))
            edits[i].textChanged.connect(result)
            
            form.addWidget(labels[i], i, 0)
            form.addWidget(edits[i], i, 1)
            form.addWidget(senses[i], i, 2)

        
        
        ui.gridLayout.addLayout(form, 2, s)
        
    def on_action_2(ui, s, document):
        print(s)
        print(999999999)
        
    def on_action_3(ui, s, document):
        print(999999999)
        
    def on_action_4(ui, s, document ):
        print(999999999)
        
    def on_action_5(ui, s, document ):
        print(999999999)

def formula_picture(ui, formula, s, font=14):

    latex_formula = formula
    figure = Figure()
    
    
    if(font <= 12):
        figure.set_size_inches(1, 1)

    figure.patch.set_facecolor( (0.9294, 0.9216, 0.9216))
    canvas = FigureCanvas(figure)
  
    ax = figure.add_subplot(111)

    font_properties = {'family': 'Segoe UI', "color": (0.3569, 0.3529, 0.3529), 'size': font}
    ax.text(0.5, 0.5, latex_formula, fontdict=font_properties, va='center', ha='center')
    ax.axis('off')
    #canvas.draw()
    return canvas

    
    






