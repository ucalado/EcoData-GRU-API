from pydantic import BaseModel
from typing import Optional


class EleitoresSchema(BaseModel):
    sg_uf: str
    cod_municipio: int
    nm_municipio: str
    nr_ano: int
    nr_mes: int
    qt_eleitores: int
    dt_carga: str
    fonte: Optional[str] = "TSE"  # valor padrão


class TseConsolidado(BaseModel):
    Cd_municipio: int
    Ano: int
    Estado_civil: str
    Genero: str
    Municipio: str
    UF: str
    Grau_de_instrucao: str
    Qtd_comparecimento: int
    Qtd_abstencao: int
    Qtd_aptos: int
    Data_de_carga: str
    font: Optional[str] = "TSE"
