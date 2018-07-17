from  forecastiopy import *
from .models import Current

api_key=None

def get_api_key(app):
    global api_key
    api_key=app.config["API_KEY"]
	
def get_daily_data(town):
    fio = ForecastIO.ForecastIO(api_key, latitude=town[0], longitude=town[1])
    current = FIOCurrently.FIOCurrently(fio)
    return Current(current)