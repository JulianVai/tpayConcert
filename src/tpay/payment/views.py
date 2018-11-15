import requests, datetime
from payment.models import *
from requests.auth import HTTPBasicAuth
from tpay.settings import DATABASES as database
import base64
import json
import os, uuid
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname("__file__"), '.env_var') 
load_dotenv(dotenv_path)

USER = os.getenv("USER_TPAY")
PASS= os.getenv("PASS_TPAY")

data = {
"cost":"12000",
"purchase_details_url":"https://example.com/compra/348820",
"voucher_url":"https://example.com/comprobante/348820",
"idempotency_token":"ea0c78c5-e85a-48c4-b7f9-24b9014a2339",
"order_id":"348820",
"terminal_id":"sede_45",
"purchase_description":"Compra en Tienda X",
"purchase_items":[
    {
        "name":"Aceite de girasol",
        "value":"13.390",
        "quantity":"3"
    },
    {
        "name":"Arroz X 80g",
        "value":"4.190"
    }
],
"user_ip_address":"61.1.224.56",
"expires_at":"2018-11-06T20:10:57.549653+00:00"
}



url_pay_req = 'https://stag.wallet.tpaga.co/merchants/api/v1/payment_requests/create'

ath = HTTPBasicAuth(USER,PASS)

def encode_auth(ath):
    cuserpass = ath.username + ":" + ath.password
    str_b = cuserpass.encode("ascii")
    str_b64 = base64.b64encode(str_b)
    authstr = str_b64.decode('ascii')
    return authstr

authstr = encode_auth(ath)

head = {"Content-Type":"application/json",
        "Authorization": 'Basic %s' % authstr}




def make_pay_req(head,data,url_pay_req):
    r = requests.post(url_pay_req,json=data,headers=head)
    return r

def calculate_cost_order(order_id):
    price_unit = EventFeatures.price_unit
    quants = OrderTickets.quantity_sold
    total = price_unit*quants
    return total
    
def create_event():
    cd = EventFeatures()
    cd.id_event = gen_order_or_event_id()
    print("Descripción del evento")
    cd.description = input()
    print("Cantidad de tikets disponibles")
    cd.quantity_total = int(input())
    print("Precio de cada tiket")
    cd.price_unit = int(input())
    cd.save()

def gen_idem_token():
    token = uuid.uuid4()
    token = str(token)
    return token

def gen_order_or_event_id():
    token = uuid.uuid4()
    token = str(token)
    token = token[:8]
    return token

def generate_order(quantity):
    od = OrderTickets()
    od.order_id = gen_order_or_event_id()
    od.idempotency_token = gen_idem_token()
    od.quantity_sold = quantity
    od.state = 'created'
    od.date_create = generate_dates()[0]
    od.exp_date = generate_dates()[1]
    #od.price_total = calculate_cost_order()


def generate_dates():
    now = datetime.datetime.utcnow()
    dt = datetime.timedelta(minutes = 10)
    et = now + dt
    et = et.isoformat()
    et = et +'-05:00'
    now = now.isoformat()
    now = now +'-05:00'
    return et, now

def get_ip():
    ip = requests.get('https://api.ipify.org').text
    return ip

def validate_cant_sale(id_event,quant_to_sale):
    ev = EventFeatures.objects.get(id_event=id_event)
    disp = ev.quantity_total
    if quant_to_sale <= disp:
        new_cant = disp - quant_to_sale
        ev.quantity_total = new_cant
        ev.save()
        return print("Habían %d entradas, ahora quedan %d"%(disp,new_cant))
    else:
        return print("No hay boletas suficientes, solo hay %d" % (disp))

# def gen_json_order(order_id):

#     data = {
#         "cost": 'f2ae6c87'
#     }






    

    


