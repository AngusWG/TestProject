#!/usr/bin/python3
# encoding: utf-8
# @Time    : 2021/9/15 10:54
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : wallpaper_abyss_downloader.py
import os
import shutil
import tkinter

import requests
from bs4 import BeautifulSoup

screen = tkinter.Tk()
proxies = {
    "http": "http://127.0.0.1:9999",
    "https": "http://127.0.0.1:9999",
}

base_url = 'https://wall.alphacoders.com/'


def download_image(url: str, folder: str):
    source = requests.get(url, proxies=proxies).text
    soup = BeautifulSoup(source, 'lxml')
    # print(soup.prettify())
    a = soup.find('img', class_='main-content')
    print(a)
    span = soup.find('span', class_='btn btn-success btn-custom download-button').attrs
    img = span['data-id'] + '.' + span['data-type']

    image = requests.get(a.attrs['src'], proxies=proxies, stream=True)
    with open(folder + '/' + img, 'wb') as out_file:
        shutil.copyfileobj(image.raw, out_file)
    del image
    del source


sys_definition = f"{screen.winfo_screenwidth()}x{screen.winfo_screenheight()}"


def main(
    # target_url='https://wall.alphacoders.com/search.php?search=Tilt+Shift+Wallpapers',
    target_url='https://wall.alphacoders.com/by_sub_category.php?id=118389&name=Tilt+Shift+Wallpapers',
    folder='images',
    definition: str = sys_definition,
):
    count = 0
    page_count = 1

    if not os.path.exists(folder):
        os.mkdir(folder)

    screen_x, screen_y = definition.split("x")
    screen_x, screen_y = int(screen_x), int(screen_y)

    while True:
        page_url = f"{target_url}&page={page_count}"
        page = requests.get(page_url, proxies=proxies).text
        soup = BeautifulSoup(page, 'lxml')

        for i in soup.find_all('div', class_='thumb-container-big'):
            span = i.find('span')
            x, y = span.text.split('x')
            print(str(count) + ": " + base_url + i.a.attrs['href'])
            if int(x) / screen_x * screen_y == int(y):
                download_image(base_url + i.a.attrs['href'], folder)
                count += 1
        page_count += 1


if __name__ == '__main__':
    main()
