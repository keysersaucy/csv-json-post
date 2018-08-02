import csv
import json
import requests
from flask import (Flask, request, redirect, send_from_directory, render_template)

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return send_from_directory('static', 'index.html')
    else:
        csvfile = request.files['file']
        text = [line.decode('utf-8') for line in csvfile]
        data = []
        for row in csv.DictReader(text, quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True):
            data.append(row)
        
        targeturl = request.form['target']
        res = requests.post(targeturl, json=data)
        return render_template('res.html', res=res, str=json.dumps(data))

@app.route("/test", methods=['POST'])
def test():
    print("[TEST] Test endpoint posted")
    return ('', 204)

if __name__ == '__main__':
    app.run()