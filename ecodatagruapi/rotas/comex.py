from fastapi import APIRouter, Query, Request
from typing import List
from app.dao.comex_dao import ComexDAO
from app.schemas.comex_schema import ComexAnual, ComexMensal, ComexProduto
from limiter_config import limiter
router = APIRouter(prefix="/v1/comex", tags=["Comércio Exterior"])


@router.get("/mensal", response_model=List[ComexMensal],summary="Consulta valores mensais por ano.",
            description=""" 
            """)
@limiter.limit("5/minute")
async def consulta_mensal(request: Request, ano: int = Query(2024, description="Ano de consulta")):
    return ComexDAO.get_valor_por_mes(ano)


@router.get("/anual", response_model=List[ComexAnual],summary="Consulta valores anuais.",
            description=""" 
            """)
@limiter.limit("5/minute")
async def consulta_anual(request: Request):
    return ComexDAO.get_valor_por_ano()


@router.get("/produtos/", response_model=List[ComexProduto],summary="Consulta classificação de produtos.",
            description=""" 
            """)
@limiter.limit("5/minute")
async def consulta_produtos(request: Request):
    return ComexDAO.get_produto()
