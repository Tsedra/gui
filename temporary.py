import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создаем главное окно и устанавливаем его размер
        self.setWindowTitle("Latex Formula Viewer")
        self.setGeometry(100, 100, 400, 400)

        # Создаем виджет для отображения изображения
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # LaTeX-формула
        latex_formula = r'$\frac{a}{b} = \frac{c}{d}$'

        # Создаем изображение с формулой
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)
        ax = self.figure.add_subplot(111)
        ax.text(0.5, 0.5, latex_formula, fontsize=20, va='center', ha='center')
        ax.axis('off')

        # Отобразите изображение
        self.canvas.draw()

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
