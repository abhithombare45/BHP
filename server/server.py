from flask import Flask, request, jsonify, send_from_directory
import server.util as util
import os

# Serve files from '../client' directory
app = Flask(__name__, static_folder="../client", static_url_path="")

# Load model and columns
util.load_saved_artifacts()

# Serve home page
@app.route('/')
def serve_home():
    return send_from_directory(app.static_folder, 'app.html')

# Serve any static files (CSS, JS, etc.)
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

# API endpoint for location list
@app.route("/get_location_names")
def get_location_names():
    response = jsonify({"locations": util.get_location_names()})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

# API endpoint for prediction
@app.route("/predict_home_price", methods=["POST"])
def predict_home_price():
    total_sqft = float(request.form["total_sqft"])
    location = request.form["location"]
    bhk = int(request.form["bhk"])
    bath = int(request.form["bath"])

    response = jsonify({
        "estimated_price": util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
