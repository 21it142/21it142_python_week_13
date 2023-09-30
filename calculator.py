import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout
from PyQt5.QtCore import Qt

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator")
        self.setGeometry(100, 100, 300, 400)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QGridLayout()
        self.central_widget.setLayout(self.layout)
        
        self.result_display = QLineEdit()
        self.result_display.setStyleSheet("font-size: 24px; padding: 10px;")
        self.layout.addWidget(self.result_display, 0, 0, 1, 4)
        
        button_grid = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]
        
        for i, row in enumerate(button_grid):
            for j, button_text in enumerate(row):
                button = QPushButton(button_text)
                button.setStyleSheet("font-size: 18px; padding: 10px;")
                button.clicked.connect(self.on_button_click)
                if button_text == "=":
                    button.setFixedSize(100, 60)  # Adjust the size as needed
                self.layout.addWidget(button, i + 1, j)
        
        self.current_input = ""
        self.result = None
    
    def on_button_click(self):
        button = self.sender()
        button_text = button.text()
        
        if button_text == "=":
            try:
                self.result = eval(self.current_input)
                self.result_display.setText(str(self.result))
            except Exception as e:
                self.result_display.setText("Error")
            self.current_input = ""
        else:
            self.current_input += button_text
            self.result_display.setText(self.current_input)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc_app = CalculatorApp()
    calc_app.show()
    sys.exit(app.exec_())
