from pydantic import BaseModel
from typing import Optional


class EleitoresGenero(BaseModel):
    Cod_municipio: int
    Municipio: str
    Ano: int
    Genero: str
    Total_aptos: int
    Total_comparecimento: int
    Total_abstencao: int
    fonte: Optional[str] = "TSE"  # valor padrão


class EleitoresGrau(BaseModel):
    Cod_municipio: int
    Municipio: str
    Ano: int
    Grau_de_instrucao: str
    Total_aptos: int
    Total_comparecimento: int
    Total_abstencao: int
    fonte: Optional[str] = "TSE"  # valor padrão


class TseConsolidadoAno(BaseModel):
    Cod_municipio: int
    Nm_municipio: str
    Nr_ano: int
    Qtd_eleitores: int
    font: Optional[str] = "TSE"


class TseConsolidadoMes(BaseModel):
    Cod_municipio: int
    Nm_municipio: str
    Nr_mes: int
    Qtd_eleitores: int
    font: Optional[str] = "TSE"
