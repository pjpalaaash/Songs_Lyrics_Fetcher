from os import link
import requests
from bs4 import BeautifulSoup
import html5lib
import os

songtemp = input("Enter Song Name: ").split()
movietemp = input("Enter Movie Name: ").split()

s = "-".join(songtemp)
m = "-".join(movietemp)

url = "https://www.lyricsmint.com/"+m+"/"+s
print(url)
print(s)
print(m)

r = requests.get(url)

contents = r.content

soup = BeautifulSoup(contents,"html.parser")

div = soup.find_all(class_="text-base")

lyrics = (div[1].getText())
lyrics2 = (div[0].getText())




print(lyrics)

f = open(s,"w",encoding='utf8')

f.writelines(lyrics)


f.writelines(lyrics2)


f.close()