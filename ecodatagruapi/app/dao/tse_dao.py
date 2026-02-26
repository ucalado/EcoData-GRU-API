from sqlalchemy import text, create_engine
from app.connect.Connection import Connection


class EleitoresDAO:

    @staticmethod
    def get_por_genero(ano: int):
        """Consulta: Quantidade de eleitores por gênero e ano."""
        engine = create_engine(Connection().dados)
        query = text("""
                    SELECT cod_municipio as Cod_municipio,
                        municipio as Municipio,
                        ano as Ano, 
                        genero as Genero, 
                        SUM(Qtd_aptos) as Total_aptos,
                        SUM(Qtd_comparecimento) as Total_comparecimento,
                        SUM(Qtd_abstencao) as Total_abstencao
                    FROM tse_consolidado
                    WHERE ano = :Ano
                    GROUP BY Cod_municipio, Municipio, Ano, Genero
                    ORDER BY Total_aptos
                   """)

        with engine.connect() as conn:
            resultado = conn.execute(query, {"Ano": ano})
            return [dict(row._mapping) for row in resultado]

    @staticmethod
    def get_por_grau(ano: int):
        """Consulta:Quantidade de eleitores por grau de instrução e ano."""
        engine = create_engine(Connection().dados)
        query = text("""
                   SELECT cod_municipio as Cod_municipio,
                        municipio as Municipio,
                        ano as Ano, 
                        grau_de_instrucao as Grau_de_instrucao, 
                        SUM(Qtd_aptos) as Total_aptos,
                        SUM(Qtd_comparecimento) as Total_comparecimento,
                        SUM(Qtd_abstencao) as Total_abstencao
                   FROM tse_consolidado
                   WHERE Ano = :Ano
                   GROUP BY Cod_municipio, Municipio, Ano, Grau_de_instrucao
                   ORDER BY Total_aptos DESC
                   """)

        with engine.connect() as conn:
            resultado = conn.execute(query, {"Ano": ano})
            return [dict(row._mapping) for row in resultado]


    @staticmethod
    def get_eleitores_ano():
        """Consulta:Valor total de eleitores por ano."""
        engine = create_engine(Connection().dados)
        query = text("""
                    SELECT 
                        cod_municipio as Cod_municipio,
                        nm_municipio as Nm_municipio,
                        nr_ano as Nr_ano,
                        SUM(qt_eleitores) as Qtd_eleitores
                    FROM tse_eleitorado
                    GROUP BY Nr_ano
                    ORDER BY Nr_ano DESC 
                   """)

        with engine.connect() as conn:
            resultado = conn.execute(query)
            return [dict(row._mapping) for row in resultado]


    @staticmethod
    def get_eleitores_mes(mes: int, ano: int):
        """Consulta:Valor total de eleitores por mês e ano."""
        engine = create_engine(Connection().dados)
        query = text("""
                    SELECT 
                        cod_municipio as Cod_municipio,
                        nm_municipio as Nm_municipio,
                        nr_mes as Nr_mes,
                        qt_eleitores as Qtd_eleitores
                    FROM tse_eleitorado
                    WHERE nr_mes = :mes AND nr_ano = :ano
                    ORDER BY Nr_mes 
                   """)

        with engine.connect() as conn:
            resultado = conn.execute(query, {"mes": mes, "ano": ano})
            return [dict(row._mapping) for row in resultado]

