from fastapi import FastAPI
import json

app = FastAPI()

with open('./questions.txt', 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()

with open('output.json', 'w', encoding='utf-8') as json_file:
    json.dump(lines, json_file, ensure_ascii=False, indent=4)

print("Ma'lumotlar JSON faylga muvaffaqiyatli yozildi.")


@app.get('/questions')
def json_get():
    with open('./output.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

print("Ma'lumotlar jonatilindi")
