from typing import List

from pydantic import BaseModel

from .role import Role


class User(BaseModel):
    id: int = None
    name: str = None
    email: str
    password: str = None
    roles: List[Role] = []

    def is_system_admin(self):
        return any(role.is_system_admin() for role in self.roles)

    def is_account_admin(self):
        return any(role.is_account_admin() for role in self.roles)

    def is_account_analyst(self):
        return any(role.is_account_analyst() for role in self.roles)
