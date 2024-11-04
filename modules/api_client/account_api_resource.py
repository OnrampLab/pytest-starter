from transstellar.api_client import APIClient, APIResource


class AccountAPIResource(APIResource):
    def __init__(self, api_client: APIClient):
        super().__init__("api/accounts/{account_id}", api_client)

    def create(
        self,
        path_params: dict = None,
        payload=None,
        headers=None,
        expected_successful_status_code=200,
    ):
        response = super().create(
            path_params, payload, headers, expected_successful_status_code
        )

        return response
