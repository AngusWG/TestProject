# anthor MrJStyle
# Form https://github.com/MrJStyle/Python-Crawler

import logging
import os
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import click
from bs4 import BeautifulSoup

log_format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=log_format)


def downloads(url, folder, name, directory):
    path = os.path.join(directory, folder)
    if not os.path.exists(path):
        os.mkdir(path)
    urllib.request.urlretrieve(url=url, filename=path + '{}.jpg'.format(name))


header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}


@click.command()
@click.option('-u', '--target_url', default='http://wallpaperswide.com/')
@click.option('-b', '--begin_num', default=1)
@click.option('-e', '--end_num', default=2)
@click.option('-d', '--directory', default='./')
@click.option('-f', '--folder', default='WallPapers')
def run(target_url, begin_num, end_num, directory, folder):
    executor = ThreadPoolExecutor(2)
    req = urllib.request.Request(url=target_url, headers=header)
    response = urllib.request.urlopen(req)  # req可以看成一种更为高级的URL
    html = response.read().decode('utf-8', 'ignore')
    soup = BeautifulSoup(html, 'lxml')
    page = int(soup.find('div', class_='pagination').find_all('a')[-2].string)
    for index, i in enumerate(range(int(begin_num), int(end_num) + 1)):
        logging.info('page {} / {}'.format(index, len(range(int(begin_num), int(end_num)))))
        # logging.info('page %s / %s', index, len(range(int(begin_num), int(end_num))))
        new_url = 'http://wallpaperswide.com/page/' + str(i)
        req_1 = urllib.request.Request(url=new_url, headers=header)

        response_1 = urllib.request.urlopen(req_1)
        html_1 = response_1.read().decode('utf-8', 'ignore')
        soup = BeautifulSoup(html_1, 'lxml')
        div = soup.find('ul', class_='wallpapers')
        li_list = div.find_all('li', class_='wall')
        for index2, j in enumerate(li_list):
            # secondary_url(directory, folder, index, index2, j, li_list)
            executor.submit(secondary_url, directory, folder, index, index2, j, li_list)


def secondary_url(directory, folder, index, index2, j, li_list):
    logging.info('page {}  Wallpaper {} / {}'.format(index, index2, len(li_list) - 1))
    tail = j.find('a')['href']
    pattern = r'/(.*)\.'
    name = re.match(pattern, tail).group()
    name = name[1:-1]
    logging.info('scrawling picture %s', name)
    pic_url = 'http://wallpaperswide.com' + str(tail)
    req2 = urllib.request.Request(url=pic_url, headers=header)
    response2 = urllib.request.urlopen(req2)
    soup2 = BeautifulSoup(response2, 'lxml')
    file = \
        soup2.find('div', class_='wallpaper-resolutions').find('a',
                                                               title='HD 16:9 1920 x 1080 wallpaper for FHD 1080p High Definition or Full HD displays')[
            'href']
    host_file_url = 'http://wallpaperswide.com' + str(file)
    downloads(host_file_url, folder, name, directory)


if __name__ == '__main__':
    # run('http://wallpaperswide.com/', 8, 11, '/Volumes/Samsung_T5/Files/Photo/', 'WallPapers')
    run()
