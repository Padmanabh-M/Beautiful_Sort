#Finale'
import os
import shutil
from bs4 import BeautifulSoup
import requests
import re


def send_em(thy_name, released):
    if os.path.exists(path+'\\'+ released):
        shutil.move(path+'\\'+thy_name, path+'\\'+released+'\\'+thy_name )
    else:
        os.makedirs(path+'\\'+date)
        shutil.move(path+'\\'+thy_name, path+'\\'+released+'\\'+thy_name )



path = 'E:\GRIP\Task 1\\'


listo = os.listdir(path)


# Looping through songs
for i in listo:
    if (i[-4:] == '.mp3') or (i[-4:] == '.m4a'):
        flag = 0
        print(i)
        song_name = i 
        hehe = '+'.join(i.split())
        source = requests.get('https://www.google.com/search?q=when+was+the+song+'+hehe[:-4]+'+released&oq=&aqs=chrome.2.69i59i450l8.598641056j0j15&sourceid=chrome&ie=UTF-8').text
        soup = BeautifulSoup(source, 'lxml')


    #     Trying on the search page
        try1 = soup.find_all(class_ = 'FCUp0c rQMQod')
        for ii in try1:
            date = ii.text
            if len(date)==4:
                print(date)
                send_em(song_name, date)
                flag = 1
                break

        if flag == 0:
            try2 = soup.find_all(class_ = 'BNeawe iBp4i AP7Wnd')
            for iii in try2:
                date = iii.text
                if len(date)==4:
                    print(date)
                    send_em(song_name, date)
                    flag = 1
                    break

        if flag == 0:
            try3 = soup.find_all(class_ = 'BNeawe deIvCb AP7Wnd')
            for iiii in try3:
                date = iiii.text
                if len(date)==4:
                    print(date)
                    send_em(song_name, date)
                    flag = 1
                    break




        # Going all wiki....
        if flag == 0:

            maybe = soup.find( class_='BNeawe UPmit AP7Wnd')
            wanna = maybe.text[26:]

            source = requests.get('https://en.wikipedia.org/wiki/'+wanna).text

            soup = BeautifulSoup(source, 'lxml')

            maybe2 = soup.find_all( class_='infobox-data plainlist')

            for iiiii in maybe2:
                pratt = re.compile(r'\s\d\d\d\d')
                chris = pratt.findall(str(iiiii))
                if chris:
                    date = chris[0][-4:]
                    send_em(song_name, date)
                    break





