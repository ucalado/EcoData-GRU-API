from fastapi import APIRouter, Request, HTTPException
from app.dao.tse_dao import EleitoresDAO
from app.schemas.eleitores_schema import EleitoresGenero, EleitoresGrau, TseConsolidadoAno, TseConsolidadoMes
from typing import List, Union
from limiter_config import limiter
router = APIRouter(prefix="/v1/eleitores", tags=["Eleitores"])


@router.get("/eleitores", response_model=Union[List[EleitoresGenero], List[EleitoresGrau]],
            summary="Consulta dados referente aos eleitores ativos no município.",
            description="""Para realizar a consulta, escolha o ano que deseja e
             no campo perfil escolha entre: 'genero' ou 'grau'.\n
             Para que a consulta seja realizada com sucesso, deverá ser utilizado os anos de eleição:
              (ex: 2022,2024) """)
@limiter.limit("5/minute")
async def consulta_eleitores(request: Request, ano: int = 2024, perfil: str = "genero"):
    if perfil.lower() == "genero":
        return EleitoresDAO.get_por_genero(ano)
    elif perfil.lower() == "grau":
        return EleitoresDAO.get_por_grau(ano)
    return HTTPException(status_code=400, detail="Perfil não encontrado. Use Genero ou instrucao")


@router.get("/eleitores_ano", response_model=List[TseConsolidadoAno],
            summary="Consulta dados referente aos eleitores ativos no município por ano.",
            description="""Para realizar a consulta, escolha o ano de referência.""")
@limiter.limit("5/minute")
async def consulta_eleitores_ano(request: Request):
    return EleitoresDAO.get_eleitores_ano()


@router.get("/eleitores_mes_ano", response_model=List[TseConsolidadoMes],
            summary="Consulta dados referente aos eleitores ativos no município por mês/ano.",
            description="""Para realizar a consulta, escolha o ano e mês de referência.\n
            Para que a consulta seja realizada com sucesso, deverá utilizar o mês como valor inteiro: 
            (ex: 1, 2, 3, 4)""")
@limiter.limit("5/minute")
async def consulta_eleitores_mes(request: Request, mes: int = 12, ano: int = 2025):
    return EleitoresDAO.get_eleitores_mes(mes, ano)
