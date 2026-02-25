from sqlalchemy import text, create_engine
from app.connect.Connection import Connection

class CnesDAO:

    @staticmethod
    def get_por_cep(cep:int):
        """Consulta:Unidades de saúde por cep."""
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
            resultado = conn.execute(query, {"cep": cep})
            return [dict(row._mapping) for row in resultado]

    @staticmethod
    def get_por_bairro(bairro: str):
        """Consulta:Unidades de saúde por bairro."""
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
                              WHERE NO_BAIRRO like :bairro
                              ORDER BY NO_RAZAO_SOCIAL ASC;
                           """)

        with engine.connect() as conn:
            resultado = conn.execute(query, {"bairro": f"%{bairro}%"})
            return [dict(row._mapping) for row in resultado]

    @staticmethod
    def get_por_cnes(cnes: int):
        """Consulta:Unidades de saúde por cnes."""
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
                              WHERE CO_CNES = :cnes
                              ORDER BY CO_CEP ASC;
                           """)
        with engine.connect() as conn:
            resultado = conn.execute(query, {"cnes": cnes})
            return [dict(row._mapping) for row in resultado]
