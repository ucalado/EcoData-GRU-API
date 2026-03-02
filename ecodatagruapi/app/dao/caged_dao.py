from sqlalchemy import text, create_engine
from app.connect.Connection import Connection


class CagedDAO:

    @staticmethod
    def get_por_setor(setor: str):
        """Consulta:Valores por setor da economia."""
        engine = create_engine(Connection().dados)
        query = text("""
                   SELECT ano,
                           cod_municipio,
                           municipio,
                           setor,
                           admissoes,
                           desligamentos,
                           saldo
                      FROM caged
                      WHERE setor like :setor
                      ORDER BY ano ASC;
                   """)

        with engine.connect() as conn:
            resultado = conn.execute(query, {"setor": f"%{setor}%"})
            return [dict(row._mapping) for row in resultado]

    @staticmethod
    def get_por_ano(ano: int):
        """Consulta:Valores por ano."""
        engine = create_engine(Connection().dados)
        query = text("""
                   SELECT ano,
                           cod_municipio,
                           municipio,
                           setor,
                           admissoes,
                           desligamentos,
                           saldo
                      FROM caged
                     WHERE ano = :ano;
                   """)

        with engine.connect() as conn:
            resultado = conn.execute(query, {"ano": ano})
            return [dict(row._mapping) for row in resultado]

