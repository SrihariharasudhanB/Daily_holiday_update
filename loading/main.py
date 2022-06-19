import requests
import pandas as pd
from loading_into_db import Loader

class Main:
    
    def __init__(self) -> None:
        pass

    def load(self):
        api_key = "< YOUR API KEY >"
        country_code = "< YOUR COUNTRY CODE >"
        year = "< PRESENT YEAR >"

        name = []
        description=[]
        date=[]
        location = []
        state = []

        req = requests.get("https://calendarific.com/api/v2/holidays?&api_key={api_key}&country={country_code}&year={year}".format(api_key=api_key,country_code=country_code,year=year))
        res = req.json()
        loader = Loader()

        for r in res["response"]["holidays"]:
            name.append(r["name"])
            description.append(r["description"])
            date.append(r["date"]["iso"])
            location.append(r["locations"])
            state.append(r["states"])

        date_dict ={
            "name" : name,
            "description" : description,
            "date" : date,
            "location" : location,
            "state" : state
        }

        df = pd.DataFrame(date_dict)

        loader.load_data(df)
        print("success!")

m = Main()
m.load()
