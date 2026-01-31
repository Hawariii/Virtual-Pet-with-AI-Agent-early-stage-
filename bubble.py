from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt, QTimer

class BubbleChat(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QLabel {
                background-color: rgba(30,30,30,200);
                color: white;
                border-radius: 10px;
                padding: 8px;
                font-size: 12px;
            }
        """)
        self.setAlignment(Qt.AlignLeft)
        self.hide()

    def show_text(self, text, pos):
        self.setText(text)
        self.adjustSize()
        self.move(pos.x() + 90, pos.y() - 10)
        self.show()

        QTimer.singleShot(4000, self.hide)
