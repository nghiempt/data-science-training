import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url = "http://py4e-data.dr-chuck.net/known_by_Kendyl.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
all_num_list = list()
link_position = 18
Process_repeat = 7

tags = soup('a')

while Process_repeat - 1  >= 0 :
    print("Process round", Process_repeat)
    target = tags[link_position - 1]
    print("target:", target)
    url = target.get('href', 2)
    print("Current url", url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    Process_repeat = Process_repeat - 1