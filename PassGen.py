import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLineEdit, QPushButton, QWidget, 
                            QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QButtonGroup, QSlider)
import random
import string
from PyQt5.QtCore import Qt, QTimer

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()  
        self.int()

    def int(self):

        # main window setup

        self.setWindowTitle("Password Generator")
        self.setMaximumSize(400,400)
        self.setMinimumSize(400,400) 
        
        # this is all the buttons need to set up this project

        self.text_box = QLineEdit(self) # this needs to be harizontal/ textbox where the random passwod will be displayed
        self.button1 = QPushButton("Copy",self) # next to the random password displayed/ allows user to copy
        self.slider = QSlider(Qt.Horizontal,self)
        self.slider_value_box = QLineEdit(self)
        self.button2 = QPushButton("Generate",self) # be at bottom left under everything
        self.cap_letter = QCheckBox("Capitalize letters",self) 
        self.lower_letter = QCheckBox("Lowercase Letters",self)
        self.special_char = QCheckBox("Speacial Character",self) 
        self.numbers = QCheckBox("Numbers",self)

        # set up the text box and copy button horizontally
        
        self.text_box.setPlaceholderText("Generated Password") # placeholder text 
        self.text_box.setFixedWidth(250)
        self.button1.setFixedWidth(100)

        # display the current value of the slider

        self.slider_value_box.setAlignment(Qt.AlignCenter) # center the text
        self.slider_value_box.setReadOnly(True) # make it read only
        self.slider_value_box.setText(str(self.slider.value()))
        self.slider_value_box.setFixedWidth(100)

       # layout for text box button
         
        hbox = QHBoxLayout()
        hbox.addWidget(self.text_box, alignment=Qt.AlignCenter)
        hbox.addWidget(self.button1, alignment=Qt.AlignCenter)

       # layout for radio buttons

        options_layout = QVBoxLayout()
        options_layout.addWidget(self.cap_letter)
        options_layout.addWidget(self.lower_letter)
        options_layout.addWidget(self.special_char)
        options_layout.addWidget(self.numbers)

        bottom_layout = QVBoxLayout()
        bottom_layout.addWidget(self.slider, alignment=Qt.AlignCenter)
        bottom_layout.addWidget(self.slider_value_box, alignment=Qt.AlignCenter)
        bottom_layout.addWidget(self.button2, alignment=Qt.AlignCenter)
                
        # main verticale layout

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(options_layout)
        vbox.addLayout(bottom_layout)

        self.setLayout(vbox)

        # adjust the slider behavior
        self.slider.setRange(6,20) # set a range for slider 
        self.slider.setValue(12) # set intial value of slider to 12
        self.text_box.setAlignment(Qt.AlignCenter) # center text inside text box

        # set the text box value to match the initaial slider value
        
        self.slider_value_box.setText(str(self.slider.value()))
        
        # connect the slider value change to the text box update 
        
        self.slider.valueChanged.connect(self.update_slider_value)

        # connect the generated button to the generatedpassword method
        
        self.button2.clicked.connect(self.generate_password)

        # connect the copy button to the copy password method 
        
        self.button1.clicked.connect(self.copy_password)

    def update_slider_value(self):
        # update the text box to show the current value of the slider 
        
        self.slider_value_box.setText(str(self.slider.value()))

    
    def generate_password(self):
        
        lenght = self.slider.value()
        character_pool = ""

        if self.cap_letter.isChecked():
            character_pool += string.ascii_uppercase
        if self.lower_letter.isChecked():
            character_pool += string.ascii_lowercase
        if self.special_char.isChecked():
            character_pool += "!@#$%^&*()"
        if self.numbers.isChecked():
            character_pool += string.digits 

        if not character_pool:
            self.text_box.setText("Please select a option")
            return 

        # generate random password 
        password = ''.join(random.choice(character_pool)for _ in range(lenght))
        self.text_box.setText(password)  

    def copy_password(self):
            clipboard = QApplication.clipboard()
            clipboard.setText(self.text_box.text()) 

        # change copy button text to copied 
            self.button1.setText("Copied") 

        # revert the button text back to copy 
            QTimer.singleShot(2000, lambda: self.button1.setText("Copy"))                  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    password_generator = PasswordGenerator()
    password_generator.show()
    sys.exit(app.exec_()) 
