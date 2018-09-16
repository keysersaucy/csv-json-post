import csv
import json
import requests
from flask import (Flask, request, redirect, render_template)

app = Flask(__name__)

def middleware_factory():
    def nest(data):
        for row in data:
            if 'Consignment.Operation' in row and 'Consignment.Commission' in row:
                c1 = row['Consignment.Operation']
                c2 = row['Consignment.Commission']
                row['Consignment'] = {
                    'Operation': c1,
                    'Commission': c2
                }
                del row['Consignment.Operation']
                del row['Consignment.Commission']

        return data
    return {
        'Nest': nest
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

        target_url = request.form['target']
        headers = {'POST https://api.ticketutils.com/POS/v3.1/Tickets','X-Signature: UUkIadAHSyOBVFUYslm9YWxNeAWGkyxgXtPdUNAcJOs=','X-Token: 4644945949495429116','Content-Type: application/json','X-API-Version: 3'}
        res = None
        if target_url and target_url != request.base_url:
            res = requests.post(target_url, json=data, headers=headers)
        return render_template('res.html', res=res, str=json.dumps(data, indent=4, sort_keys=True))

if __name__ == '__main__':
    app.run()
