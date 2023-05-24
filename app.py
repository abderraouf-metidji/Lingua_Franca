from flask import Flask, render_template, request, jsonify
from langdetect import detect
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/translate', methods=['POST'])
def translate():
    if request.method == 'POST':
        text = request.form['text']
        source_lang = request.form['source_lang']
        target_lang = request.form['target_lang']

        translation = translate_text(text, source_lang, target_lang)

        return jsonify({'translation': translation})

    return render_template('index.html')

def translate_text(text, source_lang, target_lang):
    if source_lang == 'auto':
        source_lang = detect_language(text)

    url = f'https://translate.googleapis.com/translate_a/single?client=gtx&sl={source_lang}&tl={target_lang}&dt=t&q={text}'
    response = requests.get(url)
    translation = response.json()[0][0][0]

    return translation

def detect_language(text):
    language = detect(text)
    return language

if __name__ == '__main__':
    app.run(debug=True)
