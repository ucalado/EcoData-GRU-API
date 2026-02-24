from fastapi import APIRouter
from typing import List
from app.dao.comex_dao import ComexDAO
from app.schemas.comex_schema import ComexSchema
router = APIRouter(prefix="/v1/comex", tags=["Comex"])


@router.get("/comex", response_model=List[ComexSchema],
            summary="Consulta dados do comércio exterior.",
            description="""
            
            """)
def get_comex():
    dados = ComexDAO.get_comercio()
    return dados
