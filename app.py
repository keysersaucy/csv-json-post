import csv
import json
import urllib
from flask import (Flask, request, redirect, send_from_directory)

app = Flask(__name__, static_folder='static', static_url_path='')

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
        
        jsonstr = json.dumps(data).encode('utf8')
        targeturl = request.form['target']
        req = urllib.request.Request(targeturl, data=jsonstr, headers={'content-type': 'application/json'})
        res = urllib.request.urlopen(req)
        return redirect('/')

if __name__ == '__main__':
    app.run()