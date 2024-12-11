import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLineEdit, 
                            QFileDialog, QVBoxLayout, QHBoxLayout, QWidget, QLabel)
from PyQt5 import uic

class UiConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UI to PY Converter")
        self.setGeometry(100, 100, 600, 200)
        
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        
        # UI File selection
        ui_layout = QHBoxLayout()
        self.ui_path = QLineEdit()
        self.ui_path.setPlaceholderText("Select .ui file...")
        ui_button = QPushButton("Browse UI File")
        ui_button.clicked.connect(self.select_ui_file)
        ui_layout.addWidget(QLabel("UI File:"))
        ui_layout.addWidget(self.ui_path)
        ui_layout.addWidget(ui_button)
        
        # Output directory selection
        output_layout = QHBoxLayout()
        self.output_path = QLineEdit()
        self.output_path.setPlaceholderText("Select output directory...")
        output_button = QPushButton("Browse Directory")
        output_button.clicked.connect(self.select_output_dir)
        output_layout.addWidget(QLabel("Output Dir:"))
        output_layout.addWidget(self.output_path)
        output_layout.addWidget(output_button)
        
        # Convert button
        convert_button = QPushButton("Convert")
        convert_button.clicked.connect(self.convert_ui_to_py)
        
        # Status label
        self.status_label = QLabel("")
        
        # Add all layouts and widgets to main layout
        layout.addLayout(ui_layout)
        layout.addLayout(output_layout)
        layout.addWidget(convert_button)
        layout.addWidget(self.status_label)
        
    def select_ui_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Select UI File",
            "",
            "UI Files (*.ui)"
        )
        if file_name:
            self.ui_path.setText(file_name)
            
    def select_output_dir(self):
        dir_name = QFileDialog.getExistingDirectory(
            self,
            "Select Output Directory"
        )
        if dir_name:
            self.output_path.setText(dir_name)
            
    def convert_ui_to_py(self):
        ui_file = self.ui_path.text()
        output_dir = self.output_path.text()
        
        if not ui_file or not output_dir:
            self.status_label.setText("Please select both UI file and output directory!")
            return
        
        try:
            # Generate output Python file name
            ui_file_name = os.path.basename(ui_file)
            py_file_name = os.path.splitext(ui_file_name)[0] + '.py'
            output_file = os.path.join(output_dir, py_file_name)
            
            # Convert UI to Python
            with open(output_file, 'w', encoding='utf-8') as fout:
                uic.compileUi(ui_file, fout)
            
            self.status_label.setText(f"Successfully converted to: {output_file}")
            
        except Exception as e:
            self.status_label.setText(f"Error: {str(e)}")

def main():
    app = QApplication(sys.argv)
    window = UiConverterApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()