import requests
import json
enterKey = 'ENT629977eef48af869f07841c71bfc8620'
custKey = 'CUST629977eef48af869f07841c71bfc8620'
id1 = '54b604dfa520e02948a0f508'
req = requests.get('http://api.reimaginebanking.com/customers?key=' + custKey)
print req.json #print req.status_code
##json.loads('[_id{accounts[]address{}}_id{accounts[]address{}}_id{accounts[]address{}}]')
