from zeep import Client
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep.transports import Transport
from zeep.settings import Settings

import json
import xmltodict


def get_maintenancemanager():

    wsdl = "https://pasb-dev-uwa-iws.oracleindustry.com/ouaf/webservices/CM-MAINTENANCEMANAGER?WSDL"
    session = Session()
    session.auth = HTTPBasicAuth("RFID_INTEGRATION", "Rfid_1nt")

    client = Client(wsdl, transport=Transport(session=session),
                    settings=Settings(strict=False, raw_response=True))

    request_data = {
        'FROM_DATE': '2019-01-01T14:00:00.000+08:00',
        'TO_DATE': '2020-10-19T14:00:00.000+08:00'
    }

    response = client.service.ExtractMaintenanceManager(**request_data)
    response_xml = response.content
    # print(response_xml)
    middleware_response_json = json.loads(
        json.dumps(xmltodict.parse(response_xml)))
    return middleware_response_json['env:Envelope']['env:Body']['ouaf:ExtractMaintenanceManager']['ouaf:results']
