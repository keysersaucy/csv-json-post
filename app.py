import csv
import json
import requests
from flask import (Flask, request, redirect, render_template)

app = Flask(__name__)

def middleware_factory():
    def aggregate_dob(data):
        for row in data:
            if 'birth.year' in row and 'birth.month' in row and 'birth.day' in row:
                by = row['birth.year']
                bm = row['birth.month']
                bd = row['birth.day']
                row['birth'] = {
                    'year': by,
                    'month': bm,
                    'day': bd
                }
                del row['birth.year']
                del row['birth.month']
                del row['birth.day']
        return data
    return {
        'aggregate_dob': aggregate_dob
    }


@app.route("/", methods=['GET', 'POST'])
def index():
    middlewares = middleware_factory()
    if request.method == 'GET':
        return render_template('index.html', middlewares=middlewares)
    else:
        csvfile = request.files['file']
        text = [line.decode('utf-8') for line in csvfile]
        data = []
        for row in csv.DictReader(text, quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True):
            data.append(row)

        if 'middlewares' in request.form:
            for x in request.form.getlist('middlewares'):
                data = middlewares[x](data)

        targeturl = request.form['target']
        res = requests.post(targeturl, json=data)
        return render_template('res.html', res=res, str=json.dumps(data, indent=4, sort_keys=True))

@app.route("/test", methods=['POST'])
def test():
    print("[TEST] Test endpoint posted")
    return ('', 204)

if __name__ == '__main__':
    app.run()