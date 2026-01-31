from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QPoint, QTimer
from PySide6.QtGui import QPainter, QColor
import random

class PetWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.size = 80
        self.resize(self.size, self.size)

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.drag_pos = QPoint()

        # idle movement
        self.timer = QTimer()
        self.timer.timeout.connect(self.idle_move)
        self.timer.start(2000)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(80, 200, 255))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(0, 0, self.size, self.size)

    def mousePressEvent(self, e):
        self.drag_pos = e.globalPosition().toPoint()

    def mouseMoveEvent(self, e):
        delta = e.globalPosition().toPoint() - self.drag_pos
        self.move(self.pos() + delta)
        self.drag_pos = e.globalPosition().toPoint()

    def idle_move(self):
        dx = random.randint(-10, 10)
        dy = random.randint(-10, 10)
        self.move(self.x() + dx, self.y() + dy)
