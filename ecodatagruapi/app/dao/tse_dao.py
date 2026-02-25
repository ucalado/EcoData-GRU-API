from sqlalchemy import text, create_engine
from app.connect.Connection import Connection


class EleitoresDAO:

    @staticmethod
    def get_por_genero(ano: int):
        """Consulta: Quantidade de eleitores por gênero e ano."""
        engine = create_engine(Connection().dados)
        query = text("""
                    SELECT Ano, Genero, 
                        SUM(Qtd_aptos) as Total_aptos,
                        SUM(Qtd_comparecimento) as Total_Comparecimento,
                        SUM(Qtd_abstencao) as Total_abstencao
                    FROM tse_consolidado
                    WHERE Ano = :ano
                    GROUP BY Genero
                    ORDER BY Total_Aptos
                   """)

        with engine.connect() as conn:
            resultado = conn.execute(query, {"ano": ano})
            return [dict(row._mapping) for row in resultado]

    @staticmethod
    def get_por_grau(ano: int):
        """Consulta:Quantidade de eleitores por grau de instrução e ano."""
        engine = create_engine(Connection().dados)
        query = text("""
                   SELECT Ano, Grau_de_instrucao, SUM(Qtd_aptos) as Total_Aptos
                   FROM tse_consolidado
                   WHERE Ano = :Ano
                   GROUP BY Grau_de_instrucao
                   ORDER BY Total_Aptos DESC
                   """)

        with engine.connect() as conn:
            resultado = conn.execute(query, {"ano": ano})
            return [dict(row._mapping) for row in resultado]


    @staticmethod
    def get_eleitores_ano(ano: int):
        """Consulta:Valor total de eleitores por ano."""
        engine = create_engine(Connection().dados)
        query = text("""
                    
                   """)

        with engine.connect() as conn:
            resultado = conn.execute(query, {"ano": ano})
            return [dict(row._mapping) for row in resultado]


    @staticmethod
    def get_eleitores_mes(mes: int, ano: int):
        """Consulta:Valor total de eleitores por mês e ano."""
        engine = create_engine(Connection().dados)
        query = text("""
                    SELECT CO_CNES as Cnes,
                           NO_RAZAO_SOCIAL as Razao_social,
                           TRIM(NO_LOGRADOURO || ', ' || NU_ENDERECO || ' ' || COALESCE(NO_COMPLEMENTO, '')) as Endereco,
                           NO_BAIRRO as Bairro,
                           CO_CEP as Cep,
                           NU_TELEFONE as Telefone,
                           NO_EMAIL as Email
                      FROM cnes
                      WHERE CO_CEP = :cep
                      ORDER BY CO_CEP ASC;
                   """)

        with engine.connect() as conn:
            resultado = conn.execute(query, {"mes": mes, "ano": ano})
            return [dict(row._mapping) for row in resultado]

