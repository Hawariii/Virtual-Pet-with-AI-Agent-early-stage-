import sys
from PySide6.QtWidgets import QApplication
from pet_window import PetWindow
from bubble import BubbleChat
from speech import SpeechToText
from ai_engine import AIEngine

app = QApplication(sys.argv)

pet = PetWindow()
bubble = BubbleChat()
stt = SpeechToText()
ai = AIEngine()

pet.show()

def on_double_click(event):
    text = stt.listen()
    if text:
        reply = ai.ask(text)
        bubble.show_text(reply, pet.pos())

pet.mouseDoubleClickEvent = on_double_click

sys.exit(app.exec())
