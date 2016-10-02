import pandas as pd
import requests
from sqlalchemy import create_engine
from urls import url as nba_url


class Populate:
    def __init__(self):
        self.engine = create_engine('postgresql://root:root@localhost:5432/nba')

    def populate(self):
        frame = get_dataframe_from_response(nba_url)
        # table does not have to exist on insert
        frame.to_sql('hustle_overall', con=self.engine, if_exists='append', index=False)

def get_dataframe_from_response(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    while response.status_code != 200:
        response = requests.get(url)
    headers = response.json()['resultSets'][0]['headers']
    data = response.json()['resultSets'][0]['rowSet']
    frame = pd.DataFrame(data, columns=headers)

    return frame

populate = Populate()
populate.populate()
