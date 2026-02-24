class Connection:

    def __init__(self):
        self.comex = '/data/comex_raw.duckdb'
        self.eleitores = 'sqlite:///data/tse.db'
        self.ibge = 'sqlite:///data/ibge.db'
        