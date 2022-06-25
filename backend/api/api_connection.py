import pandas as pd
import io
import requests
from time import sleep

class APIConnection:

    def __init__(self):
        self.real_time_url = 'https://temporeal.pbh.gov.br?param=C'
    
    def __enter__(self):
        return self
    
    def get_response(self):
        while(True):
            try:
                response = requests.get(self.real_time_url).content.decode('utf-8')
                return response
            except:
                sleep(1)

    def get_data(self):
        while(True):
            try:
                resp = self.get_response()
                real_time_data = pd.read_csv(io.StringIO(resp), delimiter=';')
                real_time_data = real_time_data.rename(columns=lambda x: x.strip())
                return real_time_data
            except:
                sleep(1)
    
    def __exit__(self, *args, **kwargs):
        return False