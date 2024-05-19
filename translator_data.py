import json
from googletrans import Translator

translator = Translator()

text = "Hello, world!"

translated = translator.translate(text, src='en', dest='uz')

print(f'Original text: {text}')
print(f'Tarjima qilingan: {translated.text}')