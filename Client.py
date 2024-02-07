import os
import requests
import json


class Client:
    protocol = os.environ.get("PROTOCOL")
    endpoint_cb = os.environ.get("ENDPOINT_CB")

    def __init__(self) -> None:
        pass

    def get_all_entities_by_type(
        self,
        type,
        context,
        limit=100,
        offset=0,
        service=None,
        subservice=None,
        token=None,
    ):

        url = "{PROTOCOL}://{ENDPOINT_CB}/ngsi-ld/v1/entities".format(
            PROTOCOL=self.protocol, ENDPOINT_CB=self.endpoint_cb
        )

        payload = {
            "type": type,
            "scopeQ": subservice,
            "limit": limit,
            "offset": offset,
            "options": "count",
        }
        headers = {
            "NGSILD-Tenant": service,  # equals to "Fiware-Service": service,
            "X-Auth-Token": token,
            "Link": '<{CONTEXT}>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'.format(
                CONTEXT=context
            ),
            "Accept": "application/ld+json",
        }

        response = requests.request(
            "GET", url, headers=headers, params=payload, verify=False
        )
        return response

    def upsert_entities(self, data, context):
        url = "{PROTOCOL}://{ENDPOINT_CB}/ngsi-ld/v1/entityOperations/upsert".format(
            PROTOCOL=self.protocol, ENDPOINT_CB=self.endpoint_cb
        )

        payload = json.dumps(data)
        headers = {
            "Content-Type": "application/json",
            "Link": '<{CONTEXT}>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'.format(
                CONTEXT=context
            ),
            "Accept": "application/ld+json",
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response
