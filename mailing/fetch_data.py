import mysql.connector
import datetime

class Fetcher:

    def __init__(self) -> None:
        pass

    def fetch(self):
        
        today = datetime.datetime.today()
        date = today.strftime("%Y-%m-%d")
        
        query1 = """
                    SELECT name, description, state FROM etl_project2
                    WHERE date = '{date}'
                    ORDER BY name;
                """.format(date=date)
        
        con = mysql.connector.connect(host="< host name >", username="< user name >", password="< password >", database="< db name >")
        cur = con.cursor()
        cur.execute(query1)
        result = cur.fetchall()
        statement =""
        
        for datum in result:
            statement += datum[0] +" - "+datum[1]+" \n"
            
        if len(statement)==0:
            statement = "No Holidays Today! \n"
        return statement
    
        cur.close()
        con.close()
