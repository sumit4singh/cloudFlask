import string

import boto3 as boto3
import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    data = {}
    data["banner"] = "B00882103"
    data["ip"] = "ec2-54-173-219-142.compute-1.amazonaws.com"

    # response = requests.post("http://localhost:3000/lookup", data=data)
    response = requests.post("http://3.88.132.229:80/begin", json=data)
    return response.text


@app.route('/storedata', methods=['POST'])
def storedata():
    data = request.json
    s3data: string = data.get('data')
    configures3(s3data)
    return {"s3uri": "https://cloudassignmentb00882103.s3.amazonaws.com/B00882103File.txt"}


def configures3(s3data: string):
    session = boto3.Session(aws_access_key_id="ASIARVAB6G2YYCQN3SL6",
                            aws_secret_access_key="mdM7o0rfFmrrlPIDH5wXl0/s17oWxIYd9mCyXb9f",
                            aws_session_token="FwoGZXIvYXdzEDwaDGKBNLRqqgjc6WyAjCLAAagKYppHmw1IY/waDT8iKX56UYLvGx7uO1TS3ZOJivD9I3cDBNoFioDuLjSuRc98goeoEEZ3FqWHHxPBf/SIpja3UglUR1wx2Hyz7f/c1TBpYVW30QCjBDdMdy189fGx/hlMCMoIS9+wT4GFPTcP3Wi0sNscBvdWkWAYmKZG/dTyoy6alzTnnpMRbN1t57WrTLACdaIF6e8lMFfXAsAVefPjyZW+GMHYJXZuRPoNOnSQnyZjZztck2YHknCNZK7B4ijc/pORBjItKTwABzYYfqJrvBS0BmYHfI1dPqyAMLjAXY5b6gP8YDDw9X8UJWEN2yOjWOKZ"
                            )
    s3 = session.resource('s3')
    BUCKET_NAME = 'cloudassignmentb00882103'
    obj: any = s3.Object(BUCKET_NAME, "B00882103File.txt")
    obj.put(Body=s3data)
    obj.Acl().put(ACL='public-read')


if __name__ == '__main__':
    app.run()
