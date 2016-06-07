import requests
import os

from flask import Flask, request, Response
from werkzeug.datastructures import Headers

from two1.wallet import Wallet
from two1.bitserv.flask import Payment

app = Flask(__name__)

wallet = Wallet()
payment = Payment(app, wallet)

@app.route('/<format>/<destination>')
@payment.required(5)
def get(format, destination):
    print(format)
    print(destination)
    url = 'http://localhost:8080/{}/{}'.format(format, destination)
    r = requests.get(url)
    resp = Response()
    resp = Response(
        r.text if r.text else None,
        status = r.status_code)
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
