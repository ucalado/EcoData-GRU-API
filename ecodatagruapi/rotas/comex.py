from fastapi import APIRouter, Query
from typing import List
from app.dao.comex_dao import ComexDAO
from app.schemas.comex_schema import ComexAnual, ComexMensal, ComexProduto
router = APIRouter(prefix="/v1/comex", tags=["Comércio Exterior"])


@router.get("/mensal", response_model=List[ComexMensal],summary="Consulta valores mensais por ano.",
            description=""" 
            """)
def consulta_mensal(ano: int = Query(2024, description="Ano de consulta")):
    return ComexDAO.get_valor_por_mes(ano)


@router.get("/anual", response_model=List[ComexAnual],summary="Consulta valores anuais.",
            description=""" 
            """)
def consulta_anual():
    return ComexDAO.get_valor_por_ano()


@router.get("/produtos/{cod_sh6}", response_model=List[ComexProduto],summary="Consulta classificação de produtos.",
            description=""" 
            """)
def consulta_produtos(cod_sh6: int):
    return ComexDAO.get_produto(cod_sh6)
