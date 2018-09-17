import csv
import json
import requests
from flask import (Flask, request, redirect, render_template)

app = Flask(__name__)

def middleware_factory():
    def nest(data):
        for row in data:
            if 'Consignment.Operation' in row and 'Consignment.Commission' in row and 'Shipping.Cost' in row and 'Shipping.TrackingNumber' in row and 'Shipping.Service' in row and 'Shipping.Carrier' in row and 'Shipping.Type' in row and 'Shipping.DateExpected' in row and 'Shipping.Note' in row and 'SpecOption.ExpirationType' in row and 'SpecOption.ExpirationDate' in row and 'SpecOption.ExpirationDays' in row and 'TicketSeats.Seat' in row and 'TicketSeats.Barcode' in row and 'TicketSeats.ReferenceNumber' in row and 'SplitOptions.SplitOption' in row and 'SplitOptions.Splits' in row and 'SplitOptions.OverrideSplitOption' in row and 'InHandDetails.InHandStatus' in row and 'InHandDetails.InHandDays' in row and 'InHandDetails.InHandDate' in row and 'FacePrice.Currency' in row and 'FacePrice.Amount' in row and 'PurchasePrice.Currency' in row and 'PurchasePrice.Amount' in row: # and 'SellPrice.Currency' in row and 'SellPrice.Amount' in row: #and 'Zones.ZoneCode' in row and 'Zones.Broadcast' in row:
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
                
                spo1 = row['SpecOption.ExpirationType']
                spo2 = row['SpecOption.ExpirationDate']
                spo3 = row['SpecOption.ExpirationDays']
                row['SpecOption'] = {
                    'ExpirationType': spo1,
                    'ExpirationDate': spo2,
                    'ExpirationDays': spo3
                }
                del row['SpecOption.ExpirationType']
                del row['SpecOption.ExpirationDate']
                del row['SpecOption.ExpirationDays']
    
                ts1 = row['TicketSeats.Seat']
                ts2 = row['TicketSeats.Barcode']
                ts3 = row['TicketSeats.ReferenceNumber']
                row['TicketSeats'] = {
                    'Seat': ts1,
                    'Barcode': ts2,
                    'ReferenceNumber': ts3
                }
                del row['TicketSeats.Seat']
                del row['TicketSeats.Barcode']
                del row['TicketSeats.ReferenceNumber']
    
                so1 = row['SplitOptions.SplitOption']
                so2 = row['SplitOptions.Splits']
                so3 = row['SplitOptions.OverrideSplitOption']
                row['SplitOptions'] = {
                    'SplitOption': so1,
                    'Splits': so2,
                    'OverrideSplitOption': so3
                }
                del row['SplitOptions.SplitOption']
                del row['SplitOptions.Splits']
                del row['SplitOptions.OverrideSplitOption']
  
                ih1 = row['InHandDetails.InHandStatus']
                ih2 = row['InHandDetails.InHandDays']
                ih3 = row['InHandDetails.InHandDate']
                row['InHandDetails'] = {
                    'InHandStatus': ih1,
                    'InHandDays': ih2,
                    'InHandDate': ih3
                }
                del row['InHandDetails.InHandStatus']
                del row['InHandDetails.InHandDays']
                del row['InHandDetails.InHandDate']
    
                fp1 = row['FacePrice.Currency']
                fp2 = row['FacePrice.Amount']
                row['FacePrice'] = {
                    'Currency': fp1,
                    'Amount': fp2
                }
                del row['FacePrice.Currency']
                del row['FacePrice.Amount']
                
                pp1 = row['PurchasePrice.Currency']
                pp2 = row['PurchasePrice.Amount']
                row['PurchasePrice'] = {
                    'Currency': pp1,
                    'Amount': pp2
                }
                del row['PurchasePrice.Currency']
                del row['PurchasePrice.Amount']
    
    
                if 'Consignment' in row and 'Shipping' in row and 'PurchaseOrder.Currency' in row and 'PurchaseOrder.PODate' in row and 'PurchaseOrder.ShipFromContactId' in row and 'PurchaseOrder.BillToAddressId' in row and 'PurchaseOrder.ShipToAddressId' in row and 'PurchaseOrder.VendorCSRId' in row and 'PurchaseOrder.POType' in row and 'PurchaseOrder.ExternalOrderNumber' in row and 'PurchaseOrder.Notes' in row and 'PurchaseOrder.IsShippingCostIncludedinTicketPrice' in row:
                    
                    p1 = row['PurchaseOrder.Currency']
                    p2 = row['PurchaseOrder.PODate']
                    p3 = row['PurchaseOrder.ShipFromContactId']
                    p4 = row['PurchaseOrder.BillToAddressId']
                    p5 = row['PurchaseOrder.ShipToAddressId']
                    p6 = row['PurchaseOrder.VendorCSRId']
                    p7 = row['PurchaseOrder.POType']
                    p8 = row['Consignment']
                    p9 = row['PurchaseOrder.ExternalOrderNumber']
                    p10 = row['PurchaseOrder.Notes']
                    p11 = row['PurchaseOrder.IsShippingCostIncludedinTicketPrice']
                    p12 = row['Shipping']
                    row['PurchaseOrder'] = {
                        'Currency': p1,
                        'PODate': p2,
                        'ShipFromContactId': p3,
                        'BillToAddressId': p4,
                        'ShipToAddressId': p5,
                        'VendorCSRId': p6,
                        'POType': p7,
                        'Consignment': p8,
                        'ExternalOrderNumber': p9,
                        'Notes': p10,
                        'IsShippingCostIncludedinTicketPrice': p11,
                        'Shipping': p12
                    }
                    del row['PurchaseOrder.Currency']
                    del row['PurchaseOrder.PODate']
                    del row['PurchaseOrder.ShipFromContactId']
                    del row['PurchaseOrder.BillToAddressId']
                    del row['PurchaseOrder.ShipToAddressId']
                    del row['PurchaseOrder.VendorCSRId']
                    del row['PurchaseOrder.POType']
                    del row['Consignment']
                    del row['PurchaseOrder.ExternalOrderNumber']
                    del row['PurchaseOrder.Notes']
                    del row['PurchaseOrder.IsShippingCostIncludedinTicketPrice']
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
