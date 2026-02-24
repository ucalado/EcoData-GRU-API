from pydantic import BaseModel
from typing import Optional

class ComexSchema(BaseModel):


    fonte: Optional[str] = "COMEXSTAT" #valor padrão