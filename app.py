import csv
import json
import requests
from flask import (Flask, request, redirect, render_template)

app = Flask(__name__)

        text1 = 'HTTP/1.1'
        text2 = 'Connection: Keep-Alive'
        text3 = 'Accept: application/json'
        text4 = 'Host: api.ticketutils.net'
        text5 = 'X-Token: 4644945949495429116'
        text6 = 'X-Signature: oL+R0dsVP9GSJAjfY7KgvlIkEq6qJThivdpWzPoibOc='
        text7 = 'Content-Type: application/json; charset=utf-8'


def middleware_factory():
    def aggregate_dob(data):
        

        
        for row in data:
            if 'TotalPurchasePrice.Amount' in row and 'TotalPurchasePrice.Currency' in row and 'FacePrice.Amount' in row and 'FacePrice.Currency' in row and 'SellPrice.Amount' in row and 'SellPrice.Currency' in row and 'POType.ExpirationType' in row and 'POType.ExpirationDays' in row and 'Payments.Amount' in row and 'Payments.PaymentModeId' in row and 'Payments.PaymentMode' in row and 'Payments.PayPalEmail' in row and 'Payments.PayPalTransactionId' in row:
                
                ta = row['TotalPurchasePrice.Amount']
                tc = row['TotalPurchasePrice.Currency']
                row['TotalPurchasePrice'] = {
                    'Amount': ta,
                    'Currency': tc
                }
                del row['TotalPurchasePrice.Amount']
                del row['TotalPurchasePrice.Currency']
                
                fa = row['FacePrice.Amount']
                fc = row['FacePrice.Currency']
                row['FacePrice'] = {
                    'Amount': fa,
                    'Currency': fc
                }
                del row['FacePrice.Amount']
                del row['FacePrice.Currency']
                
                sa = row['SellPrice.Amount']
                sc = row['SellPrice.Currency']
                row['SellPrice'] = {
                    'Amount': sa,
                    'Currency': sc
                }
                del row['SellPrice.Amount']
                del row['SellPrice.Currency']

                pot = row['POType.ExpirationType']
                pod = row['POType.ExpirationDays']
                row['POType'] = {
                    'Amount': pot,
                    'Currency': pod
                }
                del row['POType.ExpirationType']
                del row['POType.ExpirationDays']                
                
                pa = row['Payments.Amount']
                pmid = row['Payments.PaymentModeId']
                pm = row['Payments.PaymentMode']
                pe = row['Payments.PayPalEmail']
                ptid = row['Payments.PayPalTransactionId']
                row['Payments'] = {
                    'Amount': pa,
                    'PaymentModeId': pmid,
                    'PaymentMode': pm,
                    'PayPalEmail': pe,
                    'PayPalTransactionId': ptid
                }
                del row['Payments.Amount']
                del row['Payments.PaymentModeId']
                del row['Payments.PaymentMode']
                del row['Payments.PayPalEmail']
                del row['Payments.PayPalTransactionId']            
                
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
        data = [text1, text2]
        for row in csv.DictReader(text, quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True):
            data.append(row)

        if 'middlewares' in request.form:
            for x in request.form.getlist('middlewares'):
                data = middlewares[x](data)

        target_url = request.form['target']
        res = None
        if target_url and target_url != request.base_url:
            res = requests.post(target_url, json=data)
        return render_template('res.html', res=res, str=json.dumps(data, indent=4, sort_keys=True))

if __name__ == '__main__':
    app.run()
