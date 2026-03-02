from pydantic import BaseModel
from typing import Optional


class CagedSchema(BaseModel):
    ano: int
    cod_municipio: int
    municipio: str
    setor: str
    admissoes: int
    desligamentos: int
    saldo: int
    fonte: Optional[str] = "NOVO_CAGED"  # valor padrão