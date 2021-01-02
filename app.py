import json

from flask import Flask, request
import os
from stix_shifter.stix_translation import stix_translation
from stix_shifter.stix_transmission import stix_transmission
translation = stix_translation.StixTranslation()
app = Flask(__name__)

if 'HOST' in os.environ:
    HOST = os.environ['HOST']
if 'PORT' in os.environ:
    PORT = int(os.environ['PORT'])
else:
    PORT = 443

if 'API_KEY' in os.environ:
    API_KEY = os.environ['API_KEY']
if 'API_PASSWORD' in os.environ:
    API_PASSWORD = os.environ['API_PASSWORD']
if 'ORG_ID' in os.environ:
    ORG_ID =  int(os.environ['ORG_ID'])

data_source = {
    "type": "identity",
    "id": "identity--3532c56d-ea72-48be-a2ad-1a53f4c9c6d3",
    "name": "Resilient",
    "identity_class": "artifacts"
}

@app.route('/rest/query_artifacts', methods = ['POST'])
def query_artifacts():
    stix = request.json
    query = translation.translate('resilient', 'query', '{}', stix['query'])
    transmission = stix_transmission.StixTransmission("resilient", {"host":HOST, "port":PORT}, {"orgId":ORG_ID,"auth": {"username": API_KEY, "password": API_PASSWORD}})
    response = transmission.query(query['queries'][0])
    return translation.translate('resilient','results', json.dumps(data_source), json.dumps(response))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port='5000')
