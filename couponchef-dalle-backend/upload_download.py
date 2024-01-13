import os
from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/", methods=["POST"])
@cross_origin(origins=["http://localhost"], supports_credentials=True)
def saveImage():
    uploaded_image = request.files["image"]
    script_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_directory, "image.png")
    
    uploaded_image.save(file_path)
    
    return "Image received"
    
if __name__ == '__main__':
    app.run(host='localhost', port=5000)