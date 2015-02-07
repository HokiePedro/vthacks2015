import requests
import argparse
import json
import urllib2
import ssl
import sys
from pprint import pprint

groceryList = [
        "APD EGGS",
        "APD EGGS"
        ]


apiEndpoint = "https://http-api.openbloomberg.com/"
thingie = "/request/blp/refdata/HistoricalData"
body = { "securities": groceryList, 
  "fields": ["PX_LAST", "OPEN"],
  "startDate": "20120101",
  "endDate": "20120105",
  "periodicitySelection": "DAILY" } 
parser = argparse.ArgumentParser()
parser.add_argument('host', type=str)
parser.parse_args()

req = urllib2.Request('https://http-api.openbloomberg.com/request/blp/refdata/HistoricalData'.format(parser.parse_args()))
req.add_header('Content-Type', 'application/json')
ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
ctx.load_verify_locations('bloomberg.crt')
ctx.load_cert_chain('vthacks_spring_2015_018.crt', 'vthacks_spring_2015_018.key')

res = urllib2.urlopen(req, data=json.dumps(body), context=ctx)

pprint(res.read())



