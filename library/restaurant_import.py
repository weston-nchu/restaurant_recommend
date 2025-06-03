import csv
from dao import *

rest_dao = RestaurantDao()
tags_dao = RestaurantTagsDao()

with open('resources/restaurant_merged.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        main = Restaurant(row["name"], row["code"], row["desc"], row["address"], row["url"],
            row["img_1"], row["img_2"], row["img_3"], row["img_4"], row["img_5"])
        rest_dao.create(main)
        
        tags = RestaurantTags(main.uid, row["restaurant_style"], row["restaurant_type"], row["occasion"],
            row["cuisine_style"], row["atmosphere"], row["special"])
        tags_dao.create(tags)