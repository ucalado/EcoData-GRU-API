class Connection:

    def __init__(self):
        self.comex = 'sqlite:///C:/Users/ulissescalado/Documents/Ulisses/ecodatagruapi/data/comex_api.db'
        # self.comex = 'sqlite://./data/comex_api.db'
        self.eleitores = 'sqlite:///data/tse.db'
        self.ibge = 'sqlite:///data/ibge.db'
# "C:\Users\ulissescalado\Documents\Ulisses\ecodatagruapi\data\comex_api.db"