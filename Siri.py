import pyttsx3
from PyDictionary import PyDictionary


class Speaking:

	def speak(self, audio):
		engine = pyttsx3.init('sapi5')
		voices = engine.getProperty('voices')
		engine.setProperty('voice', voices[0].id)
		engine.say(audio)
		engine.runAndWait()



if __name__ == '__main__':
	GFG()
	GFG.Dictionary(self=None)
