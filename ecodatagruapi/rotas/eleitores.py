from fastapi import APIRouter, Request
from app.dao.tse_dao import EleitoresDAO
from app.schemas.eleitores_schema import EleitoresSchema
from typing import List
from limiter_config import limiter
router = APIRouter(prefix="/v1/eleitores", tags=["Eleitores"])


@router.get("/eleitores", response_model=List[EleitoresSchema],
            summary="Consulta dados referente aos eleitores ativos no município.",
            description="""""")
@limiter.limit("5/minute")
async def consulta_eleitores(request: Request, ano: int, perfil: str = "genero"):
    if perfil == "genero":
        return EleitoresDAO.get_por_genero(ano)
    elif perfil == "instrucao":
        return EleitoresDAO.get_por_grau(ano)
    return {"error":"Perfil não encontrado. Use 'gênero' ou 'instrução'."}
