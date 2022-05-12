#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2021/12/16 11:30
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : 处理到处记录.py
import tqdm
from lxml import html
import os


def get_article_info(
    dir_path: str = r"C:\Users\links\Desktop\。\文档\冰orAngus-微博整理-(2011-12-06~2021-12-01)\html",
    filename: str = "2021-09-08.html"
):
    f = open(os.path.join(dir_path, filename), encoding='utf-8').read()
    xml = html.fromstring(f)
    article = "".join(xml.xpath("//article//text()"))
    text = article.strip().replace(" ", " ").replace("　", " ")

    images = xml.xpath("//article//img//@src")
    if images:
        images_text = "\n".join([f"![图]({i})" for i in images])
        text += "\n\n" + images_text
    comment_xpath = "//div[@class='m-diy-btn m-box-col m-box-center m-box-center-a m-box-center-comment']//h4//text()"
    comment = xml.xpath(comment_xpath)[0]
    create_time = xml.xpath("//h4[@class='m-text-cut']//text()")[0]

    return f"""---

{text}

- create_time: {create_time}
- comment: {comment}

"""


def main():
    dir_path = r"C:\Users\links\Desktop\。\文档\冰orAngus-微博整理-(2011-12-06~2021-12-01)\html"
    all_text = "# 微博导出\n\n"
    for filename in tqdm.tqdm(os.listdir(dir_path), bar_format='{l_bar}{bar}{r_bar}{n}'):
        print(filename)
        article_info = get_article_info(dir_path, filename)
        all_text += article_info
    with open("微博导出.md", "w", encoding='utf8') as f:
        f.write(all_text)
    print("finish")


if __name__ == '__main__':
    main()
