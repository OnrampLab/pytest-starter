from typing import Literal, Optional

from pydantic import BaseModel


class Account(BaseModel):
    id: int
    name: str
    account_type: Optional[Literal["enterprise", "trial", "registered"]] = None
