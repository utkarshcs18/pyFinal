import pyttsx3 as pytt
import pyjokes as joke

engine = pytt.init()
jokes = joke.get_joke()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

print(jokes)
engine.say(jokes)
engine.runAndWait()
