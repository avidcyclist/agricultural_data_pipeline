from flask import Flask, jsonify
from data_ingestion.fetch_weather_data import fetch_weather_data
from data_ingestion.fetch_crop_yield_data import fetch_crop_yield_data
from etl.load_to_postgres import load_data_to_postgres

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather_data():
    data = fetch_weather_data()
    return jsonify(data)

@app.route('/crop_yield', methods=['GET'])
def get_crop_yield_data():
    data = fetch_crop_yield_data()
    return jsonify(data)

@app.route('/load_data', methods=['POST'])
def load_data():
    load_data_to_postgres()
    return jsonify({"message": "Data loaded successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)