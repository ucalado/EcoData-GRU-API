from fastapi import APIRouter, Request, Query, HTTPException
from app.schemas.caged_schema import CagedSchema
from app.dao.caged_dao import CagedDAO
from typing import List
from limiter_config import limiter
router = APIRouter(prefix="/v1/caged", tags=["Caged"])


@router.get("/caged_setor", response_model=List[CagedSchema],
            summary="Consulta dados referentes ao município.",
            description="""
            Para realizar a consulta, escolha um setor entre: industria, comercio, servico, agricultura.
            """)
@limiter.limit("5/minute")
def get_caged_setor(request: Request, setor: str):
    if setor.lower() == 'industria':
        return CagedDAO.get_por_setor(setor)
    if setor.lower() == "comercio":
        return CagedDAO.get_por_setor(setor)
    if setor.lower() == "servico":
        return CagedDAO.get_por_setor(setor)
    elif setor.lower() == "agricultura":
        return CagedDAO.get_por_setor(setor)
    return HTTPException(status_code=400, detail="Setor não encontrado. escolha um setor entre: industria, comercio, "
                                                 "servico, agricultura.")

@router.get("/caged_ano", response_model=List[CagedSchema],
            summary="Consulta dados referentes ao município.",
            description="""
            
            """)
@limiter.limit("5/minute")
def get_caged_ano(request: Request, ano: int = Query(2024, description="Ano de consulta")):
    return CagedDAO.get_por_ano(ano)

