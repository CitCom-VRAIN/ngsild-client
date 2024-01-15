import os
import requests
import json


class Auth:
    auth_token_subservice = None

    def __init__(self) -> None:
        pass

    def get_auth_token_subservice(self, service, subservice):
        # Get env variables
        protocol = os.environ.get("PROTOCOL")
        endpoint_keystone = os.environ.get("ENDPOINT_KEYSTONE")
        username = os.environ.get("AUTH_USER")
        password = os.environ.get("AUTH_PASSWORD")

        url = "{PROTOCOL}://{ENDPOINT_KEYSTONE}/v3/auth/tokens".format(
            PROTOCOL=protocol, ENDPOINT_KEYSTONE=endpoint_keystone
        )

        payload = json.dumps(
            {
                "auth": {
                    "scope": {
                        "project": {"domain": {"name": service}, "name": subservice}
                    },
                    "identity": {
                        "password": {
                            "user": {
                                "domain": {"name": service},
                                "password": password,
                                "name": username,
                            }
                        },
                        "methods": ["password"],
                    },
                }
            }
        )
        headers = {"Content-Type": "application/json", "Accept": "application/json"}

        # Perform request
        response = requests.request(
            "POST", url, headers=headers, data=payload, verify=False
        )

        auth_token_subservice = response.headers["X-Subject-Token"]
        return auth_token_subservice
