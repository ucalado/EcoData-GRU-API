from sqlalchemy import text, create_engine
from app.connect.Connection import Connection


class ComexDAO:

    @staticmethod
    def get_valor_por_mes(ano:int):
        """Consulta:Valor total por mês em um ano específico"""
        engine = create_engine(Connection().dados)
        query = text("""
            SELECT Ano, Mes,Fluxo, SUM([Valor US$ FOB]) as Total_Fob FROM dados WHERE Ano = :ano
            GROUP BY Ano, Mes
            ORDER BY Mes ASC
           """)

        with engine.connect() as conn:
            resultado = conn.execute(query, {"ano": ano})
            return [dict(row._mapping) for row in resultado]


    @staticmethod
    def  get_valor_por_ano():
        """Consulta: Valor total anual"""
        engine = create_engine(Connection().dados)
        query = text("""
            Select Ano,Fluxo, SUM([Valor US$ FOB]) as Total_Fob FROM dados GROUP BY Ano ORDER BY Ano DESC
        """)
        with engine.connect() as conn:
            resultado = conn.execute(query)
            return [dict(row._mapping) for row in resultado]


    @staticmethod
    def get_produto():
        """Consulta: Detalhamento do produto SH6"""
        engine = create_engine(Connection().dados)
        query = text("""
            SELECT d.Ano,d.Fluxo,
                p.cod_sh2, p.descricao_sh2,
                p.cod_sh4, p.descricao_sh4,
                p.cod_sh6, p.descricao_sh6,
                SUM(d.[Valor US$ FOB]) as Total_Fob
            FROM dados d
            INNER JOIN produtos p ON (d.Cod_SH2 = p.cod_sh2 and d.Cod_SH4 = p.cod_sh4)             
            """)
        with engine.connect() as conn:
            resultado = conn.execute(query)
            return [dict(row._mapping) for row in resultado]
