import requests
import json
enterKey = 'ENT629977eef48af869f07841c71bfc8620'
custKey = 'CUST629977eef48af869f07841c71bfc8620'
id1 = '54b604dfa520e02948a0f508'
id2 = '54b604dfa520e02948a0f50a'
id3 = '54b604dfa520e02948a0f50b'


body = '{"type": "savings", "nickname": "example", "rewards": 1, "balance": 2}'

ran = json.load(body)
#reqString = ('http://api.reimaginebanking.com:80/customers/'+ id1 +'/accounts?key=' + custKey)
reqString = ('http://api.reimaginebanking.com:80/customers/54b604dfa520e02948a0f508/accounts?key=CUST629977eef48af869f07841c71bfc8620')
req = requests.post(reqString, data=ran)
print req.text





#print req.status_cod