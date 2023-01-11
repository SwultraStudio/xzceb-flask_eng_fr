from flask import Flask,render_template,request
from machinetranslation.translator import french_to_english,english_to_french
import json

app = Flask(__name__,template_folder='templates')

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    fr=english_to_french(textToTranslate)
    return fr

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    en=french_to_english(textToTranslate)
    return en

@app.route("/",methods=['GET'])
def renderIndexPage():
   return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
