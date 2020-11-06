#Login created by Juan Picón
from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFrame, QLabel, QLineEdit,QPushButton)

# //////////// USUARIOS Y CLAVES ////////////
dicc = {'Juan Picon':'pyqt5',
        'Juan Pablo':'interfaz'}

# //////////// VENTANA PRINCIPAL ////////////
class VentanaPrincipal(QMainWindow):
    def __init__(self, parent=None):
        super(VentanaPrincipal, self).__init__(parent)
        
        # //////////// DISEÑO ////////////
        self.setWindowTitle("LOG IN")
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(400, 300)
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor('Gray'))
        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setPalette(paleta)
        frame.setFixedWidth(800)
        frame.setFixedHeight(70)
        frame.move(0, 0)
        fuenteTitulo = QFont()
        fuenteTitulo.setPointSize(25)
        fuenteTitulo.setBold(True)
        labelTitulo = QLabel("<font color='white'>Ventana Principal</font>", frame)
        labelTitulo.setFont(fuenteTitulo)
        labelTitulo.move(52, 15)
        
        # //////////// USUARIO ////////////
        labelUsuario = QLabel("Usuario", self)
        labelUsuario.move(60, 90)
        frameUsuario = QFrame(self)
        frameUsuario.setFrameShape(QFrame.StyledPanel)
        frameUsuario.setFixedWidth(280)
        frameUsuario.setFixedHeight(28)
        frameUsuario.move(60, 116)
        self.lineEditUsuario = QLineEdit(frameUsuario)
        self.lineEditUsuario.setFrame(False)
        self.lineEditUsuario.setTextMargins(8, 0, 4, 1)
        self.lineEditUsuario.setFixedWidth(238)
        self.lineEditUsuario.setFixedHeight(26)
        self.lineEditUsuario.move(40, 1)
        
        # //////////// CONTRASEÑA ////////////
        labelContraseña = QLabel("Contraseña", self)
        labelContraseña.move(60, 160)
        frameContraseña = QFrame(self)
        frameContraseña.setFrameShape(QFrame.StyledPanel)
        frameContraseña.setFixedWidth(280)
        frameContraseña.setFixedHeight(28)
        frameContraseña.move(60, 186)
        self.lineEditContraseña = QLineEdit(frameContraseña)
        self.lineEditContraseña.setFrame(False)
        self.lineEditContraseña.setTextMargins(8, 0, 4, 1)
        self.lineEditContraseña.setFixedWidth(238)
        self.lineEditContraseña.setFixedHeight(26)
        self.lineEditContraseña.move(40, 1)
        self.lineEditContraseña.setEchoMode(QLineEdit.Password)
        
        # //////////// BOTON ////////////
        buttonMostrar = QPushButton("INGRESAR", self)
        buttonMostrar.setFixedWidth(135)
        buttonMostrar.setFixedHeight(28)
        buttonMostrar.move(130, 250)

if __name__ == '__main__':   
    import sys
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(aplicacion.exec_())