#Melissa Louise Bangloy 1468444
#https://github.com/melissa0987/password-generator

import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QCheckBox,
    QSpinBox, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox
)
from PyQt6.QtCore import Qt
from genpass import Config, get_chars, gen_password, validate_password


class PasswordGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")

        # Widgets
        self.spinbox_label = QLabel("Password Length:")
        self.length_spinbox = QSpinBox()
        self.setGeometry(120, 100, 400, 300)  # x, y, width, height
        self.length_spinbox.setValue(12) #default password length
        self.length_spinbox.setRange(6, 64) #min=6, max=64

        #options labels
        self.validate_checkbox = QCheckBox("Validate password")
        self.symbols_checkbox = QCheckBox("Include symbols (~!@#$%^&*()_+/.,)")
        self.digits_checkbox = QCheckBox("Include digits (0123456789)")
        self.lower_checkbox = QCheckBox("Include lowercase (abc...z)")
        self.upper_checkbox = QCheckBox("Include uppercase (ABC...Z)")

        #buttons labels
        self.generate_button = QPushButton("Generate")
        self.copy_button = QPushButton("Copy")
        self.clear_button = QPushButton("Clear")
        self.show_checkbox = QCheckBox("Show Password")

        self.password_display = QLineEdit()
        self.password_display.setEchoMode(QLineEdit.EchoMode.Password)

        # Layouts
        main_layout = QVBoxLayout()
        length_layout = QHBoxLayout()
        length_layout.addWidget(self.spinbox_label)
        length_layout.addWidget(self.length_spinbox)
        self.spinbox_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #options layout
        options_layout = QVBoxLayout()
        options_layout.addWidget(self.validate_checkbox)
        options_layout.addWidget(self.symbols_checkbox)
        options_layout.addWidget(self.digits_checkbox)
        options_layout.addWidget(self.lower_checkbox)
        options_layout.addWidget(self.upper_checkbox)
        

        #buttons layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.generate_button)
        button_layout.addWidget(self.copy_button)
        button_layout.addWidget(self.clear_button)
        button_layout.addWidget(self.show_checkbox)

        #main layout
        main_layout.addLayout(length_layout)
        main_layout.addLayout(options_layout)
        main_layout.addWidget(self.password_display)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        #lower, upper, digits selected by default
        self.lower_checkbox.setChecked(True)
        self.upper_checkbox.setChecked(True)
        self.digits_checkbox.setChecked(True)

        # Signals
        self.generate_button.clicked.connect(self.generate_password)
        self.copy_button.clicked.connect(self.copy_password)
        self.clear_button.clicked.connect(lambda: self.password_display.clear())
        self.show_checkbox.stateChanged.connect(self.toggle_password_visibility)
        
        

    def generate_password(self):
        config = Config(
            validate=self.validate_checkbox.isChecked(),
            symbols=self.symbols_checkbox.isChecked(),
            digits=self.digits_checkbox.isChecked(),
            length=self.length_spinbox.value(),
            lower=self.lower_checkbox.isChecked(),
            upper=self.upper_checkbox.isChecked()
        )

        chars = get_chars(config)
        if not chars:
            QMessageBox.warning(self, "Error", 
                                "Please select at least one character type.")
            return

        password = gen_password(chars, config.length)

        if config.validate and not validate_password(password, config):
            QMessageBox.warning(self, "Validation Error", 
                                "Password doesn't meet all selected criteria.")
            return

        self.password_display.setText(password)

    def copy_password(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.password_display.text())

#changes password from *** to string
    def toggle_password_visibility(self):
        if self.show_checkbox.isChecked():
            self.password_display.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_display.setEchoMode(QLineEdit.EchoMode.Password)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec())
