import csv
import json
import requests
from flask import (Flask, request, redirect, render_template)

app = Flask(__name__)

def middleware_factory():
    def nest(data):
        for row in data:
            if 'Consignment.Operation' in row and 'Consignment.Commission' in row and 'Shipping.Cost' in row and 'Shipping.TrackingNumber' in row and 'Shipping.Service' in row and 'Shipping.Carrier' in row and 'Shipping.Type' in row and 'Shipping.DateExpected' in row and 'Shipping.Note' in row: #and 'SpecOption.ExpirationType' in row and 'SpecOption.ExpirationDate' in row and 'SpecOption.ExpirationDays' in row and 'TicketSeats.Seat' in row and 'TicketSeats.Barcode' in row and 'TicketSeats.ReferenceNumber' in row and 'SplitOptions.SplitOption' in row and 'SplitOptions.Splits' in row and 'SplitOptions.OverrideSplitOption' in row and 'InHandDetails.InHandStatus' in row and 'InHandDetails.InHandDays' in row and 'InHandDetails.InHandDate' in row and 'FacePrice.Currency' in row and 'FacePrice.Amount' in row and 'PurchasePrice.Currency' in row and 'PurchasePrice.Amount' in row and 'SellPrice.Currency' in row and 'SellPrice.Amount' in row and 'Zones.ZoneCode' in row and 'Zones.Broadcast' in row:
            #if 'Consignment.Operation' in row and 'Consignment.Commission' in row and 'Shipping.Cost' in row and 'Shipping.TrackingNumber' in row and 'Shipping.Service' in row and 'Shipping.Carrier' in row and 'Shipping.Type' in row and 'Shipping.DateExpected' in row and 'Shipping.Note' in row and 'PurchaseOrder.Currency' in row and 'PurchaseOrder.PODate' in row and 'PurchaseOrder.ShipFromContactId' in row and 'PurchaseOrder.BillToAddressId' in row and 'PurchaseOrder.ShipToAddressId' in row and 'PurchaseOrder.VendorCSRId' in row and 'PurchaseOrder.POType' in row and 'PurchaseOrder.ExternalOrderNumber' in row and 'PurchaseOrder.Notes' in row and 'PurchaseOrder.IsShippingCostIncludedinTicketPrice' in row and 'SpecOption.ExpirationType' in row and 'SpecOption.ExpirationDate' in row and 'SpecOption.ExpirationDays' in row and 'TicketSeats.Seat' in row and 'TicketSeats.Barcode' in row and 'TicketSeats.ReferenceNumber' in row and 'SplitOptions.SplitOption' in row and 'SplitOptions.Splits' in row and 'SplitOptions.OverrideSplitOption' in row and 'InHandDetails.InHandStatus' in row and 'InHandDetails.InHandDays' in row and 'InHandDetails.InHandDate' in row and 'FacePrice.Currency' in row and 'FacePrice.Amount' in row and 'PurchasePrice.Currency' in row and 'PurchasePrice.Amount' in row and 'SellPrice.Currency' in row and 'SellPrice.Amount' in row and 'Tickets.SHEventId' in row and 'Tickets.EventId' in row and 'Tickets.VenueId' in row and 'Tickets.Event' in row and 'Tickets.EventDate' in row and 'Tickets.Venue' in row and 'Tickets.Section' in row and 'Tickets.Row' in row and 'Tickets.Quantity' in row and 'Tickets.MaskedQuantity' in row and 'Tickets.DoNotWaste' in row and 'Tickets.Seating' in row and 'Tickets.Stock' in row and 'Tickets.SHDeliveryMethod' in row and 'Tickets.PredeliverToSH' in row and 'Tickets.PublicNotes' in row and 'Tickets.InternalNotes' in row and 'Tickets.BrokerNotes' in row and 'Tickets.ControlNotes' in row and 'Tickets.DeliveryOption' in row and 'Tickets.ReferenceNumber' in row and 'Tickets.Discount' in row and 'Tickets.Overs' in row and 'Tickets.Tax' in row and 'Tickets.Tags' in row and 'Tickets.MinimumPayout' in row and 'Tickets.HideSeats' in row and 'Tickets.ZonePricing' in row and 'Tickets.Location' in row and 'Zones.ZoneCode' in row and 'Zones.Broadcast' in row and 'Broadcast.BroadcastTo' in row:
                c1 = row['Consignment.Operation']
                c2 = row['Consignment.Commission']
                row['Consignment'] = {
                    'Operation': c1,
                    'Commission': c2
                }
                del row['Consignment.Operation']
                del row['Consignment.Commission'] 
                
                s1 = row['Shipping.Cost']
                s2 = row['Shipping.TrackingNumber']
                s3 = row['Shipping.Service']
                s4 = row['Shipping.Carrier']
                s5 = row['Shipping.Type']
                s6 = row['Shipping.DateExpected']
                s7 = row['Shipping.Note']
                row['Shipping'] = {
                    'Cost': s1,
                    'TrackingNumber': s2,
                    'Service': s3,
                    'Carrier': s4,
                    'Type': s5,
                    'DateExpected': s6,
                    'Note': s7
                }
                del row['Shipping.Cost']
                del row['Shipping.TrackingNumber']
                del row['Shipping.Service']
                del row['Shipping.Carrier']
                del row['Shipping.Type']
                del row['Shipping.DateExpected']
                del row['Shipping.Note']
                
                if 'Consignment' in row and 'Shipping' in row and 'PurchaseOrder.Currency' in row:
                    
                    p1 = row['PurchaseOrder.Currency']
                    p8 = row['Consignment']
                    p12 = row['Shipping']
                    row['PurchaseOrder'] = {
                        'Currency': p1,
                        'Consignment': p8,
                        'Shipping': p12
                    }
                    del row['PurchaseOrder.Currency']
                    del row['Consignment']
                    del row['Shipping']
        
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
