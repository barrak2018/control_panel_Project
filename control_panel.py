import sys
from PySide6.QtCore import QThread, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QComboBox,
    QPushButton,
    QDial,
    QLabel,
    QGridLayout,
    QGroupBox
)
from serial_engine import Serial_Engine 
from qt_material import (apply_stylesheet)
from pygui.COM_module import Ui_COM_UI

class COM_module(QWidget):
    def __init__(self, serial: Serial_Engine):
        super().__init__()
        self.serial = serial
        self.ui = Ui_COM_UI()
        
        # Llama a setupUi antes de intentar interactuar con los widgets
        self.ui.setupUi(self)
        
        # Ahora que el QComboBox existe, puedes actualizarlo
        self.update_ports()
    
    def update_ports(self):
        # Limpia los elementos existentes en el QComboBox antes de añadir nuevos
        self.ui.port_combobox.clear()
        
        # Obtiene la lista de puertos directamente del motor serial
        ports_list = self.serial.get_list_ports()
        
        # Agrega los puertos al QComboBox
        self.ui.port_combobox.addItems(ports_list)

class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.serial = Serial_Engine()
        self.COM_module = COM_module(self.serial)
        apply_stylesheet(self, theme="dark_cyan.xml")
        self.setCentralWidget(self.COM_module)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main_window()
    window.show()
    sys.exit(app.exec())