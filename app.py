import string

import boto3 as boto3
import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    data = {}
    data["banner"] = "B00882103"
    data["ip"] = "127.0.0.1"

    response = requests.post("http://localhost:5000/lookup", data=data)
    return data


@app.route('/storedata', methods=['POST'])
def storedata():
    data = request.json
    s3data: string = data.get('data')
    configures3(s3data)
    return s3data


def configures3(s3data: string):
    session = boto3.Session(aws_access_key_id="ASIARVAB6G2YSOY4LXAS",
                            aws_secret_access_key="scrpH8xfCUfSQDLvaUg7l3qlvlLrdIYqn6T08rKY",
                            aws_session_token="FwoGZXIvYXdzEJj//////////wEaDJg+jKPTgycmXY5AJiLAAU2P8FEK1m7YCX6/0LjMzKlUKAysyTantwlhKKkKJaTP41MOGXRiyumMgXpbugLONqekBsbv7x632cjqIGzR86IXSIhN/zGgKG0dQTZ555dsSylH4CKh8Jd/I/368uYTX954shFGe+GWfhsOdAm1+9Ne4YfhD8VW/NAip4Hmz/Avi3x8XEWJVnIssy0LHqXh2LD0R3BbblrFUhqLvIpvL77aIyrxjFZlRe1jB1NMjQ6eJKlYYvuKuypslOtRiA7PUiiL7++QBjItmvuZ298+knB7aQrOLHLlVFTRP7OOO6tqfCRsp97eoUFfi4IpxoC3YPqGxewJ"
                            )
    s3 = session.resource('s3')
    BUCKET_NAME = 'cloudassignmentb00882103'
    obj: any = s3.Object(BUCKET_NAME, "sumitTest.txt")
    res = obj.put(Body=s3data)


if __name__ == '__main__':
    app.run()
