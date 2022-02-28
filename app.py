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
    session = boto3.Session(aws_access_key_id="ASIARVAB6G2YTG3K264O",
                            aws_secret_access_key="okKWez82HyGEkSYwENFqyUZLwP6jFlOxwmEAaGVR",
                            aws_session_token="FwoGZXIvYXdzEK3//////////wEaDKi3SWRjH8j1aYrP7iLAAYe54sU9mLoGDEG0Tklrcp3JhmFTS0HXJlNgtxjuZKGR+oVjR0g8GdPjxaQMAGXuUp4+Slk8kWN67HezldF9Ks99S7/OZ8F1oTUE76YK+ia1wapm5FJ9rXfmVPiPRsBqVYgr1CNd2DozidLW3Ef7yGijyVTPCRfhsEqFg0C3/lOb+XC1bTcZsuoIN42aLkg3U8A4OvPgvS3tBwV9plCfJ8EkYaIH7E6esUMP38d8V7equW6RjcjQE+kSClEOSKGWwijnyvSQBjItYn/043QB0TyIbN7CNH2TD2wn6NgSV7E4wix4JB0XW4NUuQqmrNbg8Pr4eTiK"
                            )
    s3 = session.resource('s3')
    BUCKET_NAME = 'cloudassignmentb00882103'
    obj: any = s3.Object(BUCKET_NAME, "B00882103File.txt")
    res = obj.put(Body=s3data)


if __name__ == '__main__':
    app.run()
