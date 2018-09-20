import csv
import json
import requests
from flask import (Flask, request, redirect, render_template)

app = Flask(__name__)

def middleware_factory():
    def nest(data):
        for row in data:
            if 'TicketSeats.Seat' in row and 'TicketSeats.Barcode' in row and 'TicketSeats.ReferenceNumber' in row and 'SplitOptions.SplitOption' in row and 'SplitOptions.Splits' in row and 'SplitOptions.OverrideSplitOption' in row and 'InHandDetails.InHandStatus' in row and 'InHandDetails.InHandDays' in row and 'InHandDetails.InHandDate' in row and 'FacePrice.Currency' in row and 'FacePrice.Amount' in row and 'PurchasePrice.Currency' in row and 'PurchasePrice.Amount' in row and 'SellPrice.Currency' in row and 'SellPrice.Amount' in row:
            #if 'Consignment.Operation' in row and 'Consignment.Commission' in row and 'Shipping.Cost' in row and 'Shipping.TrackingNumber' in row and 'Shipping.Service' in row and 'Shipping.Carrier' in row and 'Shipping.Type' in row and 'Shipping.DateExpected' in row and 'Shipping.Note' in row and 'PurchaseOrder.Currency' in row and 'PurchaseOrder.PODate' in row and 'PurchaseOrder.ShipFromContactId' in row and 'PurchaseOrder.BillToAddressId' in row and 'PurchaseOrder.ShipToAddressId' in row and 'PurchaseOrder.VendorCSRId' in row and 'PurchaseOrder.POType' in row and 'PurchaseOrder.ExternalOrderNumber' in row and 'PurchaseOrder.Notes' in row and 'PurchaseOrder.IsShippingCostIncludedinTicketPrice' in row and 'SpecOption.ExpirationType' in row and 'SpecOption.ExpirationDate' in row and 'SpecOption.ExpirationDays' in row and 'TicketSeats.Seat' in row and 'TicketSeats.Barcode' in row and 'TicketSeats.ReferenceNumber' in row and 'SplitOptions.SplitOption' in row and 'SplitOptions.Splits' in row and 'SplitOptions.OverrideSplitOption' in row and 'InHandDetails.InHandStatus' in row and 'InHandDetails.InHandDays' in row and 'InHandDetails.InHandDate' in row and 'FacePrice.Currency' in row and 'FacePrice.Amount' in row and 'PurchasePrice.Currency' in row and 'PurchasePrice.Amount' in row and 'SellPrice.Currency' in row and 'SellPrice.Amount' in row and 'Tickets.SHEventId' in row and 'Tickets.EventId' in row and 'Tickets.VenueId' in row and 'Tickets.Event' in row and 'Tickets.EventDate' in row and 'Tickets.Venue' in row and 'Tickets.Section' in row and 'Tickets.Row' in row and 'Tickets.Quantity' in row and 'Tickets.MaskedQuantity' in row and 'Tickets.DoNotWaste' in row and 'Tickets.Seating' in row and 'Tickets.Stock' in row and 'Tickets.SHDeliveryMethod' in row and 'Tickets.PredeliverToSH' in row and 'Tickets.PublicNotes' in row and 'Tickets.InternalNotes' in row and 'Tickets.BrokerNotes' in row and 'Tickets.ControlNotes' in row and 'Tickets.DeliveryOption' in row and 'Tickets.ReferenceNumber' in row and 'Tickets.Discount' in row and 'Tickets.Overs' in row and 'Tickets.Tax' in row and 'Tickets.Tags' in row and 'Tickets.MinimumPayout' in row and 'Tickets.HideSeats' in row and 'Tickets.ZonePricing' in row and 'Tickets.Location' in row and 'Zones.ZoneCode' in row and 'Zones.Broadcast' in row and 'Broadcast.BroadcastTo' in row:
                
                ts1 = row['TicketSeats.Seat']
                ts2 = row['TicketSeats.Barcode']
                ts3 = row['TicketSeats.ReferenceNumber']
                row['TicketSeats'] = [{
                    'Seat': ts1,
                    'Barcode': ts2,
                    'ReferenceNumber': ts3
                }]
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
       
                sp1 = row['SellPrice.Currency']
                sp2 = row['SellPrice.Amount']
                row['SellPrice'] = {
                    'Currency': sp1,
                    'Amount': sp2
                }
                del row['SellPrice.Currency']
                del row['SellPrice.Amount']
    
                if 'TicketSeats' in row and 'SplitOptions' in row and 'InHandDetails' in row and 'FacePrice' in row and 'PurchasePrice' in row and 'SellPrice' in row and 'Tickets.SHEventId' in row and 'Tickets.EventId' in row and 'Tickets.VenueId' in row and 'Tickets.Event' in row and 'Tickets.EventDate' in row and 'Tickets.Venue' in row and 'Tickets.Section' in row and 'Tickets.Row' in row and 'Tickets.Quantity' in row and 'Tickets.MaskedQuantity' in row and 'Tickets.DoNotWaste' in row and 'Tickets.Seating' in row and 'Tickets.Stock' in row and 'Tickets.SHDeliveryMethod' in row and 'Tickets.PredeliverToSH' in row and 'Tickets.PublicNotes' in row and 'Tickets.InternalNotes' in row and 'Tickets.BrokerNotes' in row and 'Tickets.ControlNotes' in row and 'Tickets.DeliveryOption' in row and 'Tickets.ReferenceNumber' in row and 'Tickets.Discount' in row and 'Tickets.Overs' in row and 'Tickets.Tax' in row and 'Tickets.Tags' in row and 'Tickets.MinimumPayout' in row and 'Tickets.HideSeats' in row and 'Tickets.ZonePricing' in row and 'Tickets.Location' in row:
                    
                    t1 = row['Tickets.SHEventId']
                    t2 = row['Tickets.EventId']
                    t3 = row['Tickets.VenueId']
                    t4 = row['Tickets.Event']
                    t5 = row['Tickets.EventDate']
                    t6 = row['Tickets.Venue']
                    t7 = row['Tickets.Section']
                    t8 = row['Tickets.Row']
                    t9 = row['Tickets.Quantity']
                    t10 = row['Tickets.MaskedQuantity']
                    t11 = row['Tickets.DoNotWaste']
                    t12 = row['Tickets.Seating']
                    t13 = row['Tickets.Stock']
                    t14 = row['Tickets.SHDeliveryMethod']
                    t15 = row['Tickets.PredeliverToSH']
                    t16 = row['TicketSeats']
                    t17 = row['Tickets.PublicNotes']
                    t18 = row['Tickets.InternalNotes']
                    t19 = row['Tickets.BrokerNotes']
                    t20 = row['Tickets.ControlNotes']
                    t21 = row['SplitOptions']
                    t22 = row['InHandDetails']
                    t23 = row['Tickets.DeliveryOption']
                    t24 = row['Tickets.ReferenceNumber']
                    t25 = row['FacePrice']
                    t26 = row['PurchasePrice']
                    t27 = row['SellPrice']
                    t28 = row['Tickets.Discount']
                    t29 = row['Tickets.Overs']
                    t30 = row['Tickets.Tax']
                    t31 = row['Tickets.Tags']
                    t32 = row['Tickets.MinimumPayout']
                    t33 = row['Tickets.HideSeats']
                    t34 = row['Tickets.ZonePricing']
                    t35 = row['Tickets.Location']
                    row['Tickets'] = [{
                        'SHEventId': t1,
                        'EventId': t2,
                        'VenueId': t3,
                        'Event': t4,
                        'EventDate': t5,
                        'Venue': t6,
                        'Section': t7,
                        'Row': t8,
                        'Quantity': t9,
                        'MaskedQuantity': t10,
                        'DoNotWaste': t11,
                        'Seating': t12,
                        'Stock': t13,
                        'SHDeliveryMethod': t14,
                        'PredeliverToSH': t15,
                        'TicketSeats': t16,
                        'PublicNotes': t17,
                        'InternalNotes': t18,
                        'BrokerNotes': t19,
                        'ControlNotes': t20,
                        'SplitOptions': t21,
                        'InHandDetails': t22,
                        'DeliveryOption': t23,
                        'ReferenceNumber': t24,
                        'FacePrice': t25,
                        'PurchasePrice': t26,
                        'SellPrice': t27,
                        'Discount': t28,
                        'Overs': t29,
                        'Tax': t30,
                        'Tags': [t31],
                        'MinimumPayout': t32,
                        'HideSeats': t33,
                        'ZonePricing': t34,
                        'Location': t35
                                                
                    }]
                    del row['Tickets.SHEventId']
                    del row['Tickets.EventId']
                    del row['Tickets.VenueId']
                    del row['Tickets.Event']
                    del row['Tickets.EventDate']
                    del row['Tickets.Venue']
                    del row['Tickets.Section']
                    del row['Tickets.Row']
                    del row['Tickets.Quantity']
                    del row['Tickets.MaskedQuantity']
                    del row['Tickets.DoNotWaste']
                    del row['Tickets.Seating']
                    del row['Tickets.Stock']
                    del row['Tickets.SHDeliveryMethod']
                    del row['Tickets.PredeliverToSH']
                    del row['TicketSeats']
                    del row['Tickets.PublicNotes']
                    del row['Tickets.InternalNotes']
                    del row['Tickets.BrokerNotes']
                    del row['Tickets.ControlNotes']
                    del row['SplitOptions']
                    del row['InHandDetails']
                    del row['Tickets.DeliveryOption']
                    del row['Tickets.ReferenceNumber']
                    del row['FacePrice']
                    del row['PurchasePrice']
                    del row['SellPrice']
                    del row['Tickets.Discount']
                    del row['Tickets.Overs']
                    del row['Tickets.Tax']
                    del row['Tickets.Tags']
                    del row['Tickets.MinimumPayout']
                    del row['Tickets.HideSeats']
                    del row['Tickets.ZonePricing']
                    del row['Tickets.Location']
                    
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
        if target_url: #and target_url != request.base_url:
            res = requests.post(target_url, json=data, headers=headers)
        return render_template('res.html', res=res, str=json.dumps(data, indent=4, sort_keys=True))

if __name__ == '__main__':
    app.run()
