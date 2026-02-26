from pydantic import BaseModel
from typing import Optional


class ComexMensal(BaseModel):
    Ano: int
    Mes: str
    Fluxo: str
    Total_Fob: int

    fonte: Optional[str] = "COMEXSTAT" # valor padrão


class ComexAnual(BaseModel):
    Ano: int
    Fluxo: str
    Total_Fob: int

    fonte: Optional[str] = "COMEXSTAT" # valor padrão


class ComexProduto(BaseModel):
    Ano: int
    Fluxo: str
    cod_sh2: int
    descricao_sh2: str
    cod_sh4: int
    descricao_sh4: str
    cod_sh6: int
    descricao_sh6: str
    fonte: Optional[str] = "COMEXSTAT" # valor padrão
