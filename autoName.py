#!/usr/bin/python3

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains 
import requests
import json

names = []

        
def newRandom():
    newRandom.r2 = requests.get('https://www.thecocktaildb.com/api/json/v1/1/random.php')
        
named = ""
while (len(names) < 30):
    newRandom()
    r1 = json.loads(newRandom.r2.text)
    name = r1['drinks'][0]["strDrink"]
    if name not in names:
        newName = name.replace(" ", ".")
        print("name",newName)
        names.append(newName)
    elif name in names:
        newRandom()
        if name not in names:
            newName = name.replace(" ", ".")
            print("name",newName)
            names.append(newName)
    
    print(names)
    
r3 = requests.get("https://www.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck={}".format(names[0]))

