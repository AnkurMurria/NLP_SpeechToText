from flask import Flask, request, jsonify,render_template
import os
from flask_cors import CORS, cross_origin

import speechToText
from utility.utils import decodeSound

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    audio = request.json['sound']
    decodeSound(audio, "audio.wav")
    result = speechToText.speech2Text("audio.wav")
    return jsonify({"Result" : str(result)})


if __name__ == "__main__":
    app.run(host='127.0.0.1')