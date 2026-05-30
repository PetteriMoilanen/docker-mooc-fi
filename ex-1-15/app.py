import random
from flask import Flask, jsonify

app = Flask(__name__)

QUOTES = [
    "Data is the new oil. - Clive Humby",
    "Torture the data, and it will confess to anything. - Ronald Coase",
    "Without data, you're just another person with an opinion. - W. Edwards Deming",
    "The world is one big data problem. - Andrew McAfee",
    "In God we trust. All others must bring data. - W. Edwards Deming"
]

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "Docker dummy app with a random DS quote!",
        "data_science_quote": random.choice(QUOTES)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)