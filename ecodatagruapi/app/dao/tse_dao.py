from sqlalchemy import text, create_engine
from app.connect.Connection import Connection


class EleitoresDAO:
    cod_municipio: int

    # def get_eleitores(self):
    #     self.__init__()
    #
    #     class