# encoding: utf-8
# @Time   : 2021/8/2 13:52
# @author : zza
# @Email  : 740713651@qq.com
# @File   : 图像轮廓.py

import cv2

img = cv2.imread("img.png", cv2.IMREAD_UNCHANGED)
img2 = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
middle = img2.copy()
result = cv2.drawContours(middle, contours, -1, (0, 0, 255), 3)

cv2.imshow("original", img)
cv2.imshow("resuly", result)

cv2.waitKey()
cv2.destroyAllWindows()
