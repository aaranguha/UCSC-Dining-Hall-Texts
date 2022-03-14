from re import X
import requests
from bs4 import BeautifulSoup
import os
from twilio.rest import Client
import time

def dict_add(d, key, value):
    if key in d.keys():
        d[key] += [value];
    else:
        d[key] = [value];


def dict_formatter(dict, format_string):
    for x in dict.keys():
        print(format_string.format(x, dict[x]))


def UCSC():
    account_sid = "ACd027baa66c85b1749c04c153245f1532"
    auth_token="47161313f56c8f993b2055656e7ce9b9"
    client = Client(account_sid, auth_token)
    numbersToMessage_UCSC = {'Aaran':'+15109469095',
                             'Aswhin':'+13413561722',
                             'Sibhi': '+15107387296',
                             'Omrishi': '+15107508399',
                            }
    cookies = {"WebInaCartLocation":"", "WebInaCartDates":"", "WebInaCartMeals":"", "WebInaCartRecipes":"", "WebInaCartQtys":""}
    res = requests.get('https://nutrition.sa.ucsc.edu/shortmenu.aspx?sName=UC+Santa+Cruz+Dining&locationNum=40&locationName=Colleges+Nine+%26+Ten+Dining+Hall&naFlag=1%27', cookies=cookies)
    soup = BeautifulSoup(res.text, 'lxml')
    all = soup.find('table')
    titles = all.find_all('div', class_ = 'shortmenucats')
    titleslook = all.find('div', class_ = 'shortmenucats')
    breakfast_fr = all.find_all('div', class_ = 'shortmenurecipes')

    menu = {}

    a = all.find_all('tr')
    for p in a:
        if p.find('tr'):
            continue
        else:
            meals = p.find('div', class_ = 'shortmenumeals')
            cats = p.find('div', class_ = 'shortmenucats')
            recipe = p.find('div', class_ = 'shortmenurecipes')

            if meals:
                #print(meals.text)
                k = meals.text
                if k not in menu.keys():
                    menu[k] = {}
            if cats:
                #print(cats.find('span').text)
                ik = cats.find('span').text.strip("-").strip("  ")
            if recipe:
                #print(recipe.find('span').text)
                dict_add(menu[k], ik, recipe.find('span').text.strip("\xa0"))


        def brekky():
            s = ""
            x = "Breakfast"
            s += x
            for y in menu[x].keys():
                s += "\t" + y + "\n"
                for z in menu[x][y]:
                    s += "\t\t" + z + "\n"
            return s
        def lunch():
            s = ""
            x = "Lunch"
            s += x
            for y in menu[x].keys():
                s += "\t" + y + "\n"
                for z in menu[x][y]:
                    s += "\t\t" + z + "\n"
            return s
        def dinner():
            s = ""
            x = "Dinner"
            s += x
            for y in menu[x].keys():
                s += "\t" + y + "\n"
                for z in menu[x][y]:
                    s += "\t\t" + z + "\n"
            return s
        def Late_Night():
            s = ""
            x = "Late Night"
            s += x
            for y in menu[x].keys():
                s += "\t" + y + "\n"
                for z in menu[x][y]:
                    s += "\t\t" + z + "\n"
            return s


    for name, number in numbersToMessage_UCSC.items():
        message = client.messages.create(  
            messaging_service_sid='MG2d5661c05da3fde5029a7e5484154f83', 
            body=lunch(),
            to=number
        )
 
UCSC()


def Riv():
    account_sid = "ACd027baa66c85b1749c04c153245f1532"
    auth_token="47161313f56c8f993b2055656e7ce9b9"
    client = Client(account_sid, auth_token)
    numbersToMessage_Riv = {
                             'Rashi': '15105792186', 
                            }      
    cookies = {"WebInaCartLocation":"", "WebInaCartDates":"", "WebInaCartMeals":"", "WebInaCartRecipes":"", "WebInaCartQtys":""}
    res2 = requests.get('https://foodpro.ucr.edu/foodpro/shortmenu.asp?sName=University+of+California%2C+Riverside+Dining+Services&locationNum=03&locationName=Glasgow&naFlag=1', cookies=cookies)
    soup = BeautifulSoup(res2.text, 'lxml')
    all = soup.find('table')
    titles = all.find_all('div', class_ = 'shortmenucats')
    titleslook = all.find('div', class_ = 'shortmenucats')
    breakfast_fr = all.find_all('div', class_ = 'shortmenurecipes')

    menu = {}

    a = all.find_all('tr')
    for p in a:
        if p.find('tr'):
            continue
        else:
            meals = p.find('div', class_ = 'shortmenumeals')
            cats = p.find('div', class_ = 'shortmenucats')
            recipe = p.find('div', class_ = 'shortmenurecipes')

            if meals:
                #print(meals.text)
                k = meals.text
                if k not in menu.keys():
                    menu[k] = {}
            if cats:
                #print(cats.find('span').text)
                ik = cats.find('span').text.strip("-").strip("  ")
            if recipe:
                #print(recipe.find('span').text)
                dict_add(menu[k], ik, recipe.find('span').text.strip("\xa0"))


    #for x in menu.keys():
        #print(x)
        #for y in menu[x].keys():
            #print("\t" + y)
            #for z in menu[x][y]:
                #print("\t\t" + z)

        def brekky():
            x = "Breakfast"
            print(x)
            for y in menu[x].keys():
                print("\t" + y)
                for z in menu[x][y]:
                    print("\t\t" + z)
        def lunch():
            s = ""
            x = "Lunch"
            print("\n")
            s += x
            for y in menu[x].keys():
                s += "\t" + y + "\n"
                for z in menu[x][y]:
                    s += "\t\t" + z + "\n"
            return s
            
        def dinner():
            x = "Dinner"
            print(x)
            for y in menu[x].keys():
                print("\t" + y)
                for z in menu[x][y]:
                    print("\t\t" + z)

        def Late_Night():
            s = ""
            x = "Late Night"
            print("\n")
            s += x
            for y in menu[x].keys():
                s += "\t" + y + "\n"
                for z in menu[x][y]:
                    s += "\t\t" + z + "\n"
            return s

    for name, number in numbersToMessage_Riv.items():
        message = client.messages.create(  
            messaging_service_sid='MG2d5661c05da3fde5029a7e5484154f83', 
            body=dinner(),
            to=number
        )

Riv()