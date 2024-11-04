class Account:
    def __init__(self, account_data: dict):
        self.id = account_data.get("id")
        self.name = account_data.get("name")
        self.api_token = account_data.get("api_token")

    def get_id(self) -> int:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_api_token(self) -> str:
        return self.api_token
