from pydantic import BaseModel
from typing import Optional


class CnesSchema(BaseModel):
    Cnes: int
    Razao_social: str
    Endereco: str
    Bairro: str
    Cep: int
    Telefone: Optional[str] = None
    Email:  Optional[str] = None
    fonte: Optional[str] = "DATASUS"  # valor padrão