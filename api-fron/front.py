from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def form():
    return render_template('form.html')

@app.route("/addrec", methods=['POST'])
def addrec():
    if request.method == 'POST':
        data = {
            'Id': request.form['Id'],
            'nm': request.form['nm'],
            'nm1': request.form['nm1']
        }
        response = requests.post('http://backend:5000/test', json=data)
        return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(debug=True, port=5001, host="0.0.0.0")
