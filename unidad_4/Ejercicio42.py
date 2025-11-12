# -*- coding: utf-8 -*-
"""
Requisitos:
- Realizar ping a una dirección IP o dominio desde una interfaz gráfica con PyQt5.
- Mostrar el resultado en pantalla.
"""

# -------------------- LIBRERÍAS IMPORTADAS --------------------
import sys           # Control del sistema (salida de la app con sys.exit()).
import platform      # Detecta el sistema operativo (Windows/Linux/macOS).
import subprocess    # Permite ejecutar comandos externos (como 'ping').

from PyQt5.QtWidgets import (
    QApplication,    # Inicia la aplicación Qt.
    QWidget,         # Ventana base.
    QLabel,          # Etiquetas de texto.
    QLineEdit,       # Campo de texto para ingresar IP o dominio.
    QPushButton,     # Botón para enviar el ping.
    QTextEdit,       # Área de texto para mostrar el resultado.
    QVBoxLayout,     # Layout vertical.
    QHBoxLayout,     # Layout horizontal.
    QMessageBox,     # Ventanas emergentes de advertencia o error.
)
# --------------------------------------------------------------


class PingApp(QWidget):
    """Ventana principal de la aplicación."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ping – PyQt5")
        self.resize(400, 300)

        # ---------- Widgets ----------
        self.host_input = QLineEdit(self)
        self.host_input.setPlaceholderText("Ejemplo: google.com o 8.8.8.8")

        self.ping_btn = QPushButton("Enviar ping", self)
        self.ping_btn.clicked.connect(self.ejecutar_ping)

        self.resultado = QTextEdit(self)
        self.resultado.setReadOnly(True)

        # ---------- Layout ----------
        entrada_layout = QHBoxLayout()
        entrada_layout.addWidget(QLabel("Destino:", self))
        entrada_layout.addWidget(self.host_input)

        main_layout = QVBoxLayout()
        main_layout.addLayout(entrada_layout)
        main_layout.addWidget(self.ping_btn)
        main_layout.addWidget(QLabel("Resultado:", self))
        main_layout.addWidget(self.resultado)

        self.setLayout(main_layout)

    # ------------------------------------------------------------
    def ejecutar_ping(self):
        """Ejecuta el comando 'ping' y muestra su resultado."""
        host = self.host_input.text().strip()
        if not host:
            QMessageBox.warning(self, "Entrada vacía",
                                "Introduce una dirección IP o nombre de host.")
            return

        # Determinar parámetros según el sistema operativo
        sistema = platform.system().lower()
        if "windows" in sistema:
            cmd = ["ping", "-n", "4", host]
        else:
            cmd = ["ping", "-c", "4", host]

        try:
            # Ejecutar el comando y capturar la salida
            proceso = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=10,
            )
            salida = proceso.stdout + proceso.stderr
            self.resultado.setPlainText(salida)
        except subprocess.TimeoutExpired:
            self.resultado.setPlainText("Error: tiempo de espera agotado.")
        except Exception as e:
            self.resultado.setPlainText(f" Error inesperado:\n{e}")


# ------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = PingApp()
    ventana.show()
    sys.exit(app.exec_())