# dependencies
import os
from flask import Flask, jsonify, request
from fastai import *
from fastai.vision import *

# init app
app = Flask(__name__)

# load the model
model = load_learner(os.getcwd())

# check for file type
extensions = ["jpg", "jpeg", "png"]
def validate_file_type(filename):
	return "." in filename and filename.rsplit(".", 1)[1].lower() in extensions

# predict
def predict_from_model(file):
    # load the image and predict
    image = open_image(file)
    pred = model.predict(image)
    print(str(pred[0]))
    # separate the tensors and the labels
    return jsonify({ "label": str(pred[0]), "tensor": str(pred[2]) })

# get @ /
@app.route("/", methods=["GET"])
def get():
    response = jsonify({ "msg": "Server is running." })
    response.status_code = 200
    return response

# post @ predict
@app.route("/predict", methods=["POST"])
def predict():
    # check if the post request has the file part
    if "file" not in request.files:
        resp = jsonify({ "msg": "Please include a file in the request body." })
        resp.status_code = 400
        return resp
    
    # check if file has a filename
    file = request.files["file"]
    if file.filename == "":
        resp = jsonify({ "msg": "Please include a file in the request body." })
        resp.status_code = 400
        return resp
    
    # validate the file type
    if file and validate_file_type(file.filename):
        # predict
        predictions = predict_from_model(file)
        resp = predictions
        resp.status_code = 200
        return resp
    else:
        resp = jsonify({ "msg": "Allowed file types are JPG, JPEG and PNG." })
        resp.status_code = 400
        return resp

# run the server
if __name__ == "__main__":
    app.run(debug=True)
