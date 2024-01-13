import os
from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/upload", methods=["POST"])
@cross_origin()
def saveImage():
    uploaded_image = request.files["image"]
    script_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_directory, "image.png")
    
    uploaded_image.save(file_path)
    print("image received")
    
    return "Image received"

@app.route("/hi", methods=["GET"])
@cross_origin()
def hello():
    return "Hello!"
    
if __name__ == '__main__':
    app.run(port=5000)
    
