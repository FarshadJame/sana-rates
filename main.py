import datetime
import requests
import mysql.connector
import json
from config import URL, DB, FLAG


def get_rates():
    response = requests.get(URL)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data['sana']['data']
    return None


def save_in_file(filename, rates):
    with open(f'archive/{filename}.txt', 'w', encoding='utf-8') as file:
        for value in rates:
            file.write(f'{value["title"]}: {"{:,}".format(value["p"] // 10)} تومان ' + '\n')
    print('save in file has been done!')


def save_in_database(rates):
    my_cursor = DB.cursor()
    sql = "INSERT INTO rates (title , price, high ,low, updated_at) VALUES (%s, %s ,%s ,%s ,%s)"
    for item in rates:
        val = (item["title"], item["p"], item["h"], item["l"], item["updated_at"])
        my_cursor.execute(sql, val)
        DB.commit()


if __name__ == '__main__':
    res = get_rates()
    if res is not None:
        save_in_file(datetime.datetime.now().strftime("%Y-%m-%d"), res)
    if FLAG:
        save_in_database(res)
