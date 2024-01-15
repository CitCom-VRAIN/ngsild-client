import os
import requests
import json


class Client:
    def __init__(self) -> None:
        pass

    def get_all_entities_by_type(
        self, type, service, subservice, token, limit=20, offset=0
    ):
        protocol = "http"  # os.environ.get("PROTOCOL")
        endpoint_cb = os.environ.get("ENDPOINT_CB")

        url = "{PROTOCOL}://{ENDPOINT_CB}/ngsi-ld/v1/entities?type={TYPE}&scopeQ={SUBSERVICE}&limit={LIMIT}&offset={OFFSET}&options=count".format(
            PROTOCOL=protocol,
            ENDPOINT_CB=endpoint_cb,
            TYPE=type,
            SUBSERVICE=subservice,
            LIMIT=limit,
            OFFSET=offset,
        )

        payload = {}
        headers = {
            "NGSILD-Tenant": service,  # equals to "Fiware-Service": service,
            "X-Auth-Token": token,
            "Link": '<https://raw.githubusercontent.com/smart-data-models/dataModel.WasteManagement/master/context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"',
            "Accept": "application/ld+json",
        }

        response = requests.request(
            "GET", url, headers=headers, data=payload, verify=False
        )
        return response

    def get_all_entities_by_type_and_georel(
        self,
        type,
        service,
        subservice,
        token,
        georel,
        geometry,
        coords,
        limit=20,
        offset=0,
    ):
        protocol = "http"  # os.environ.get("PROTOCOL")
        endpoint_cb = os.environ.get("ENDPOINT_CB")

        url = "{PROTOCOL}://{ENDPOINT_CB}/ngsi-ld/v1/entities?type={TYPE}&scopeQ={SUBSERVICE}&limit={LIMIT}&offset={OFFSET}&options=count&georel={GEOREL}&geometry={GEOMETRY}&coords={COORDS}".format(
            PROTOCOL=protocol,
            ENDPOINT_CB=endpoint_cb,
            TYPE=type,
            SUBSERVICE=subservice,
            LIMIT=limit,
            OFFSET=offset,
            GEOREL=georel,
            GEOMETRY=geometry,
            COORDS=coords
        )
        print(url)

        payload = {}
        headers = {
            "NGSILD-Tenant": service,  # equals to "Fiware-Service": service,
            "X-Auth-Token": token,
            "Link": '<https://raw.githubusercontent.com/smart-data-models/dataModel.WasteManagement/master/context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"',
            "Accept": "application/ld+json",
        }

        response = requests.request(
            "GET", url, headers=headers, data=payload, verify=False
        )
        return response
