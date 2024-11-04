from modules.core import Adapter

from .entities.user import User


class AuthAdapter(Adapter):
    def login(self, email, password) -> str:
        payload = {"email": email, "password": password}
        response_json = self.api_client.auth.login(payload)

        token = self.parse_response(response_json)

        return token

    def get_current_user(self) -> User:
        response_json = self.api_client.auth.get_current_user()

        json = self.parse_response(response_json)

        return User(**json)
