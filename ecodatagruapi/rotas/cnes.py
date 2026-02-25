from fastapi import APIRouter, Query, Request
from typing import List
from app.dao.cnes_dao import CnesDAO
from app.schemas.cnes_schema import CnesSchema
from limiter_config import limiter
router = APIRouter(prefix="/v1/datasus", tags=["Datasus CNES"])


@router.get("/cep", response_model=List[CnesSchema],summary="Consulta unidades de saúde por cep.",
            description=""" 
            """)
@limiter.limit("5/minute")
async def consulta_cep(request: Request, cep: int = Query(7023051, description="Cep de consulta")):
    return CnesDAO.get_por_cep(cep)


@router.get("/bairro", response_model=List[CnesSchema],summary="Consulta unidades de saúde por bairro.",
            description=""" 
            """)
@limiter.limit("5/minute")
async def consulta_bairro(request: Request, bairro: str):
    return CnesDAO.get_por_bairro(bairro)


@router.get("/cnes", response_model=List[CnesSchema],summary="Consulta unidades de saúde por cnes.",
            description=""" 
            """)
@limiter.limit("5/minute")
async def consulta_cnes(request: Request, cnes: int = Query(3338525, description="Consulta CNES")):
    return CnesDAO.get_por_cnes(cnes)