import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QCheckBox, QRadioButton, QButtonGroup,
                             QLineEdit)

from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        # self.setGeometry(700,300,500,500)  #x,y,width, height
        self.setWindowIcon(QIcon("C:\\Users\\rahul\\OneDrive\\Pictures\\idol.jpg"))
        # self.button = QPushButton("CLICK ME!", self)
        # self.label = QLabel("Hello", self)
        # self.checkbox = QCheckBox("Do you like food?", self)
        # self.radio1 = QRadioButton("Visa", self)
        # self.radio2 = QRadioButton("Mastercard", self)
        # self.radio3 = QRadioButton("Gift Card", self)
        # self.radio4 = QRadioButton("In-Store", self)
        # self.radio5 = QRadioButton("Online", self)
        # self.button_group1 = QButtonGroup(self)
        # self.button_group2 = QButtonGroup(self)
        # self.line_edit = QLineEdit(self)
        # self.button = QPushButton("Submit", self)
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()

        # label = QLabel("Hello", self)
        # label.setFont(QFont('Arial', 20))
        # label.setGeometry(0,0,500,100)
        # label.setStyleSheet("color: #D20103;"
        #                     "background-color: #EFC3CA;"
        #                     "font-weight: bold;"
        #                     "font-style: italic;"
        #                     "text-decoration: underline;")
        
        # label.setAlignment(Qt.AlignTop)       #vertically top
        # label.setAlignment(Qt.AlignBottom)      #vertically bottom
        # label.setAlignment(Qt.AlignVCenter)     #vertically center
        # label.setAlignment(Qt.AlignRight)         #horizontally right
        # label.setAlignment(Qt.AlignHCenter)          #HORIZONTALLY CENTER
        # label.setAlignment(Qt.AlignLeft)              #horizontally left
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)  # center and top
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # center and bottom
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  #center and center
        # label.setAlignment(Qt.AlignCenter)

        # label1 = QLabel(self)
        # label1.setGeometry(0,100,500,400)
        # pixmap = QPixmap("C:\\Users\\rahul\\OneDrive\\Pictures\\idol.jpg")
        # label1.setPixmap(pixmap)
        # label1.setScaledContents(False)
        # label1.setGeometry(self.width() - label1.width(),
        #                    self.height() - label1.height(), 
        #                    label1.width(), 
        #                    label1.height())
        
    def initUI(self):
        # central_widget = QWidget()
        # self.setCentralWidget(central_widget)

        # label2 = QLabel("#1", self)
        # label3 = QLabel("#2", self)
        # label4 = QLabel("#3", self)
        # label5 = QLabel("#4", self)
        # label6 = QLabel("#5", self)

        # label2.setStyleSheet("background-color: red;")
        # label3.setStyleSheet("background-color: yellow;")
        # label4.setStyleSheet("background-color: green;")
        # label5.setStyleSheet("background-color: blue;")
        # label6.setStyleSheet("background-color: purple;")

        # vbox = QVBoxLayout()

        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)
        # vbox.addWidget(label6)

        # central_widget.setLayout(vbox)

        # hbox = QHBoxLayout()

        # hbox.addWidget(label2)
        # hbox.addWidget(label3)
        # hbox.addWidget(label4)
        # hbox.addWidget(label5)
        # hbox.addWidget(label6)

        # central_widget.setLayout(hbox)

        # grid = QGridLayout()

        # grid.addWidget(label2, 0, 0)
        # grid.addWidget(label3, 0, 1)
        # grid.addWidget(label4, 0, 2)
        # grid.addWidget(label5, 1, 1)
        # grid.addWidget(label6, 2, 2)

        # central_widget.setLayout(grid)
        # self.button = QPushButton("CLICK ME!", self)
        # self.button.setGeometry(150, 200, 200, 100)
        # self.button.setStyleSheet("font-size: 30px;")
        # self.button.clicked.connect(self.on_click)

        # self.label.setGeometry(150, 300, 250, 100)
        # self.label.setStyleSheet("font-size: 50px;")
        # self.checkbox.setGeometry(10, 0, 500, 100)
        # self.checkbox.setStyleSheet("font-size: 30px;"
        #                             "font-family: Arial;")
        # self.checkbox.setChecked(False)
        # self.checkbox.stateChanged.connect(self.checkbox_changed)
        # self.radio1.setGeometry(10, 0, 300, 50)
        # self.radio2.setGeometry(10, 50, 300, 50)
        # self.radio3.setGeometry(10, 100, 300, 50)
        # self.radio4.setGeometry(10, 150, 300, 50)
        # self.radio5.setGeometry(10, 200, 300, 50)

        # self.setStyleSheet("QRadioButton{"
        #                    "font-size: 40px;"
        #                    "font-family: Arial;"
        #                    "padding: 10px;"
        #                    "}")
        
        # self.button_group1.addButton(self.radio1)
        # self.button_group1.addButton(self.radio2)
        # self.button_group1.addButton(self.radio3)
        # self.button_group2.addButton(self.radio4)
        # self.button_group2.addButton(self.radio5)
        
        # self.radio1.toggled.connect(self.radio_button_changed)
        # self.radio2.toggled.connect(self.radio_button_changed)
        # self.radio3.toggled.connect(self.radio_button_changed)
        # self.radio4.toggled.connect(self.radio_button_changed)
        # self.radio5.toggled.connect(self.radio_button_changed)
        # self.line_edit.setGeometry(10, 10, 200, 40)
        # self.button.setGeometry(210, 10, 200, 40)
        # self.line_edit.setStyleSheet("font-size: 25px;"
        #                              "font-family: Arial;")
        # self.button.setStyleSheet("font-size: 25px;"
        #                              "font-family: Arial;")
        # self.line_edit.setPlaceholderText("Name")
        # self.button.clicked.connect(self.submit)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
            QPushButton{
                font-size: 40px;
                font-family: Arial;
                padding: 15px 75px;   
                margin: 25px;
                border: 3px solid;
                border-radius: 15px;
            }
            QPushButton#button1:hover{
                background-color: hsl(287, 100%, 84%);
            }
            QPushButton#button2:hover{
                background-color: hsl(350, 100%, 84%);
            }
            QPushButton#button3:hover{
                background-color: hsl(69, 100%, 84%);
            }
        """)

    # def on_click(self):
        # print("Button Clicked!")
        # self.button.setText("Clicked!")
        # self.button.setDisabled(True)
        # self.label.setText("Goodbye!")
    # def checkbox_changed(self, state):
    #     # print(state)
    #     # print("You like food")
    #     if state == Qt.Checked:
    #         print("You like food.")
    #     else:
    #         print("You do not like food.")
    # def radio_button_changed(self):
    #     # print("You selected something.")
    #     radio_button = self.sender()
    #     if radio_button.isChecked():
    #         print(f"{radio_button.text()} is selected.")
    # def submit(self):
    #     # print("You clicked the button!")
    #     text =self.line_edit.text()
    #     print(f"Hello {text}!")

    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()