from fastapi import APIRouter
from app.schemas.ibge_schema import IbgeSchema
from app.dao.ibge_dao import IbgeDAO
from typing import List
router = APIRouter(prefix="/v1/ibge", tags=["Ibge"])


@router.get("/ibge", response_model=List[IbgeSchema],
            summary="Consulta dados referentes ao município.",
            description="""
            
            """)
def get_ibge():
    dados = IbgeDAO.get_municipio()
    return dados
