#widget creations
from PySide6.QtCore import Qt
from Pyside6.QtWidgets import QApplication, QSlider, QVBoxLayout, QPushButton

#I have no idea
import functools

#Also have no idea
from typing import List, Literal, Tuple

#tab type
from .base import BaseTabWidget

#Avr imports
from bell.avr.mqtt.payloads import (
    AvrPcmSetServoOpenClosePayload,
    AvrPcmSetServoPctPayload
)

class vacuumControlWidget(BaseTabWidget):
    def __init__(self, parent: QtWidgets.QWidget) -> None:
        super().__init__(parent)

        self.setWindowTitle("Vacuum Control")

    def build(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(layout)

        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(1)
        slider.setMaximum(100)
        slider.setValue(1)
        layout.addWidget(slider)

        side_open = QtWidgets.QPushButton("Open")
        side_open.clicked.connect(pneumatic_buttons_open)
        layout.addWidget(side_open)

        side_close = QtWidgets.QPushButton("Close")
        side_close.clicked.connect(pneumatic_buttons_close)
        layout.addWidget(side_close)

    def pneumatic_buttons_open(self) -> None:
        self.send_message(
            "avr/pcm/set_servo_open_close",
            AvrPcmSetServoOpenClosePayload(servo=5, action="open")
        )
    def pneumatic_buttons_close(self) -> None:
       self.send_message(
            "avr/pcm/set_servo_open_close",
            AvrPcmSetServoOpenClosePayload(servo=5, action="close")
        )

    def slider_response(self, data) -> None:
        self.send_message(
            "avr/pcm/set_servo_pct",
            AvrPcmSetServoPctPayload(servo = 4, percent = data)
        )
