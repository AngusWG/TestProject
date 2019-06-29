import PythonMagick
from PIL import Image
from PyPDF2 import PdfFileReader
import os

pdf_file = r"E:\PycharmProjects\TestProject\demo\temp"
file_name = "统计学（第四版）－贾俊平.pdf"
file_dir = os.path.join(pdf_file, file_name[:-4])

dirs = r"E:\PycharmProjects\TestProject\demo\temp"
DPI = '85'
pdfname = r'E:\Download\ccc.pdf'
pdf_input = PdfFileReader(open(os.path.join(pdf_file,file_name), 'rb'))
# 自动获取PDF页数
page_count = pdf_input.getNumPages()
page_range = range(page_count)
npage = pdf_input.getNumPages()
for p in range(page_count):
    im = PythonMagick.Image()
    # pint = PythonMagick.DrawablePoint(300,300)
    # im.density("300")
    im.read(file_name + '[' + str(p) + ']')
    filename = os.path.join(file_dir, file_name + p + ".jpg")
    im.write(filename)
    print(p)
