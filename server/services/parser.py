'''Parse documents'''
import os
import re

#path join file_path = os.path.join("..","doc","OFFRES.txt")
file_path = os.path.join("..","doc","OFFRES.txt")


def parse_file(file_path):
    file = open(file_path, "r", encoding="utf-8")

    offers = file.read().split(">>>")

    offers_data = []

    p = re.compile('\s{2,}')
    for offer in offers : 
        if offer != "" :
            offer_data = dict()
            lines = list(filter(None,map(lambda x: p.sub('', x), offer.split("\n"))))
            offer_data["ESN"] =lines[1]
            offer_data["title"] = lines[2]
            offer_data["contract"] = lines[3]
            offer_data["salary"] = lines[4]
            offer_data["exp"] = lines[5]
            offer_data["remote"] = lines[6]
            offer_data["location"] = lines[7]
            offer_data["body"] = lines[8:]
            offer_data["resume"] = lines[-1].split(",")
            offers_data.append(offer_data)

    print(offers_data)

