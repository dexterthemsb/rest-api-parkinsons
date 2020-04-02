# dependencies
from flask import Flask, jsonify, request

# init app
app = Flask(__name__)

# get @ /
@app.route("/", methods=["GET"])
def get():
    resp = jsonify({ "msg": "Server is running." })
    resp.status_code = 200
    return resp

# run the server
if __name__ == "__main__":
    app.run(debug=True)
