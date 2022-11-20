from pprint import pprint
from sqlite3 import connect

from bs4 import BeautifulSoup
from requests import get

url = 'https://en.m.wikipedia.org/wiki/List_of_production_battery_electric_vehicles'

page = get(url).text
soup = BeautifulSoup(page, 'html.parser')
cars = [el.text.lower() for el in soup.select('td:nth-child(1) > a')]

# elements = soup.select('i')
# for el in elements:
#     print(el.text)

with connect('db.sqlite3') as connection:
    cursor = connection.cursor()
    for car in cars:
        print(car)
        car = car.replace("'", "`")
        sqlite_select_query = ("INSERT INTO users_electriccar "
                               f"VALUES (null, '{car}');")
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
    cursor.close()
