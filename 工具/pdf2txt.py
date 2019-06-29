#!/usr/bin/python3
# encoding: utf-8
# @Time    : 2019/6/29 23:44
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : aaa.py
"""将pdf先转化为图片 再将图片中的文字提取出来"""
import os
import concurrent.futures

from PIL import Image
from pdf2image import convert_from_path
import pytesseract
from tqdm import tqdm


def make_jpg(pdf_dir, pdf_name):
    """将pdf转为图片"""
    print("start", pdf_name)
    file_dir = os.path.join(pdf_dir, pdf_name[:-4])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    pages = convert_from_path(os.path.join(pdf_dir, pdf_name), 200)
    for index, page in enumerate(pages):
        page_name = "{}_{}.jpg".format(pdf_name, index)
        print(index, page_name)
        page.save(os.path.join(file_dir, page_name), 'JPEG')
    get_txt(pdf_dir, pdf_name)


def get_txt(pdf_dir, pdf_name):
    """将图片中的文字提取出来"""
    image_dir = os.path.join(pdf_dir, pdf_name[:-4])
    file_list = os.listdir(image_dir)
    txt = ""
    print(pdf_name, "start", image_dir, len(file_list))
    for index, file in tqdm(enumerate(file_list)):
        image = Image.open(os.path.join(image_dir, file))
        code = pytesseract.image_to_string(image, lang='chi_sim')
        txt += """=== {} ===\n\n{}\n\n=== {} ===\n\n""".format(index, code, index)
    with open(os.path.join(pdf_dir, pdf_name[:-4] + ".txt"), "w", encoding="utf8") as f:
        f.write(txt)
    print(pdf_name, "finish")


def service(file_path=r"E:\PycharmProjects\TestProject\demo\temp\中国哲学史新编.pdf"):
    pdf_dir, pdf_name = os.path.dirname(file_path), os.path.basename(file_path)
    print("start {}".format(pdf_name))
    make_jpg(pdf_dir, pdf_name)
    get_txt(pdf_dir, pdf_name)
    print("end   {}".format(pdf_name))


def main():
    """将某个目录的pdf全部转换为txt 多线程"""
    pdf_dir = r"E:\PycharmProjects\TestProject\demo\temp"
    file_list = os.listdir(pdf_dir)
    with concurrent.futures.ProcessPoolExecutor(max_workers=os.cpu_count() - 1) as executor:
        for file in file_list:
            if not file.endswith(".pdf"):
                continue
            print(file)
            # executor.submit(make_jpg, pdf_dir, file)
            executor.submit(get_txt, pdf_dir, file)
    print("main finish")


if __name__ == '__main__':
    main()
