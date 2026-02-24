from fastapi import APIRouter
from app.dao.tse_dao import EleitoresDAO
from app.schemas.eleitores_schema import EleitoresSchema
from typing import List
router = APIRouter(prefix="/v1/eleitores", tags=["Eleitores"])


@router.get("/eleitores", response_model=List[EleitoresSchema],
            summary="Consulta dados referente aos eleitores ativos no município.",
            description="""""")
def get_eleitores():
    dados = EleitoresDAO.get_eleitores()
    return dados
