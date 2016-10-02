import pandas as pd
from sqlalchemy import create_engine

class DB:
    def __init__(self):
        self.engine = create_engine('postgresql://root:root@localhost:5432/nba')

    def get_data(self):
        frame = pd.read_sql('select * from hustle_overall', con=self.engine)