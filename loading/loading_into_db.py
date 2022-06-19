import mysql.connector
import pandas as pd

query1 = """
        CREATE TABLE IF NOT EXISTS etl_project2 (
                name VARCHAR(200),
                description VARCHAR(1000),
                date VARCHAR(200),
                location VARCHAR(200),
                state VARCHAR(200)
            );
        """

query2 = """
        INSERT INTO etl_project2 VALUES(
                '{name}',
                '{description}',
                '{date}',
                '{location}',
                '{state}'
            );
        """

class Loader:
    
    con = mysql.connector.connect(host="< host name >", username="< user name >", password="< db password >", database="< db name >")
    cur = con.cursor()
    
    def __init__(self) -> None:
        pass

    def load_data(self,data: pd.DataFrame):
        
        self.cur.execute(query1)
        self.data=data
        size=self.data.__len__()

        for i in range(0,size):
            self.cur.execute(
                query2.format(
                name = str(self.data["name"][i]).replace("'","''"),
                description = str(self.data["description"][i]).replace("'","''"),
                date = str(self.data["date"][i]).replace("'","''"),
                location = str(self.data["location"][i]).replace("'","''"),
                state = str(self.data["state"][i]).replace("'","''") )
            )

        self.con.commit()
        #print("Successfully loaded!")
        self.cur.close()
        self.con.close()
