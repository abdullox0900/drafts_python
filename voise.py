import requests
url = "https://api.muxlisa.uz/v1/api/services/tts/"

text = """
Mening ko‘nglumki, gulning g'unchasidek tah-batah qondur, Agar yuz ming bahor o‘lsa, ochilmog'i ne imkondur. Agar ul qoshi yosiz bog' gashtin orzu qilsam, Ko‘zumga o‘qdurur sarv-u ko‘ngulga g'uncha paykondur. Bahor-u bog' sayrin ne qilaykim, dilistonimning, Yuzi gul, zulfi sunbul, qomati sarvi xiromondur. Visoli lazzatidin zavq topmog'liq erur dushvor, Firoqi shiddatinda yo‘qsa jon bermaklik osondur. Boshidin evrulur armoni birla o‘ldum, ey Bobur, Mening na'shimni bori ul pari ko‘yidin aylondur.
"""

payload = {"text": text, "token": "1DsRA-f4yCgZuX1SrpsFDtDLyVRB4AU88Bbdk_f7", "speaker_id": 1}
files = []
headers = {}
response = requests.request("POST", url, headers=headers, data=payload, files=files)
if response.status_code == 200:
    with open("response_audio.ogg", "wb") as audio_file:
        audio_file.write(response.content)
