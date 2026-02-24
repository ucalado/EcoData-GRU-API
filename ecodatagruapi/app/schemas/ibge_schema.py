from pydantic import BaseModel
from typing import Optional


class IbgeSchema(BaseModel):
    fonte: Optional[str] = "IBGE"  # valor padrão