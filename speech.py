import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        self.r = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            audio = self.r.listen(source)
        try:
            return self.r.recognize_google(audio, language="id-ID")
        except:
            return ""
