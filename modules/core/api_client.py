from interstellar.api_client import APIClient as BaseAPIClient
from interstellar.framework import Loggable


class APIClient(BaseAPIClient):
    def login(self, email, password):
        url = f"{self.base_url}/api/auth/login"
        payload = {"email": email, "password": password}
        responseJson = self.__post(url, payload)

        return responseJson
