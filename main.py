import time
import csv
import json

import requests


def main():
    with open("config.json", 'r', encoding='utf-8') as file:
        config = json.load(file)


    while True:
        response = requests.post("https://api2.bybit.com/announcements/api/search/v1/index/announcement-posts_en-us")
        print(response.status_code)

        for item in response.json()['result']['hits']:
            if item['date_timestamp'] > config['last_timestamp']:
                config['last_timestamp'] = item['date_timestamp']

                with open("config.json", 'w', encoding='utf-8') as file:
                    json.dump(config, file)

                with open('articles.csv', 'w', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow([item['title'], item['date_timestamp'],
                                     "https://announcements.bybit.com/en-US" + item['url']])

        time.sleep(1)

if __name__ == "__main__":
    main()
