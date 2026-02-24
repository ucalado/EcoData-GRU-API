from pydantic import BaseModel
from typing import Optional


class EleitoresSchema(BaseModel):
    fonte: Optional[str] = "TSE"  # valor padrão