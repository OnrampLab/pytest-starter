from enum import Enum

from pydantic import BaseModel


class Roles(Enum):
    SYSTEM_ADMIN = "system-admin"
    ACCOUNT_ADMIN = "account-admin"
    CLIENT_OWNER = "client-owner"
    CLIENT_ANALYST = "client-analyst"


class Role(BaseModel):
    id: int
    name: str

    def is_system_admin(self):
        return self.name == Roles.SYSTEM_ADMIN.value

    def is_account_admin(self):
        return self.name == Roles.ACCOUNT_ADMIN.value

    def is_client_owner(self):
        return self.name == Roles.CLIENT_OWNER.value

    def is_client_analyst(self):
        return self.name == Roles.CLIENT_ANALYST.value
