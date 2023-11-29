import wikipedia
from googletrans import Translator

#result = wikipedia.summary("physics", auto_suggest=False, sentences=2)

#print(result)


translator = Translator()
result = translator.translate("Hello World", dest="it")
print(result.text)
