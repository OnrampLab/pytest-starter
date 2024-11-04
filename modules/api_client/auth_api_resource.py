from transstellar.api_client import APIClient, APIResource


class AuthAPIResource(APIResource):
    def __init__(self, api_client: APIClient):
        super().__init__("api/auth/login", api_client)

    def login(self, payload=None):
        response = super().create(payload=payload, expected_successful_status_code=200)

        return response

    def get_current_user(self):
        endpoint = "api/auth/me"
        response = self.api_client.post(
            endpoint=endpoint, payload=None, expected_successful_status_code=200
        )

        return response
