#!/usr/bin/env python
# coding:utf-8


""""
Name: 图书管理系统.py
Date: 2018/2018/29
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

import time


class Book(object):
    def __init__(self, name, author, state, bookIndex):
        self.name = name
        self.author = author
        # 0: 借出， 1：未借出
        self.state = state
        self.bookIndex = bookIndex

    def __str__(self):
        stat = "已借出"
        if self.state == 1:
            stat = "未借出"
        return "书名:《%s》 作者:%s 状态:%s 位置:%s" % (
            self.name, self.author, self.state, self.bookIndex
        )


class BookManger(object):
    books = []

    def init(self):
        self.books.append(Book("python", '廖雪峰', 1, 'I12009'))

    def Menu(self):
        self.init()
        while True:
            print("""
                            图书管理系统

                1. 查询所有书籍
                2. 增加书籍
                3. 借出书籍
                4. 归还书籍
                5. 退出
            """)
            choice = input("请选择:")
            if choice == 1:
                self.showAllBook()
            elif choice == 2:
                self.addBook()
            elif choice == 3:
                self.borrowBook()
            elif choice == 4:
                self.returnBook()
            elif choice == 5:
                print("谢谢使用")
                exit()

    def showAllBook(self):
        # 遍历列表
        # book是对象
        for book in self.books:
            # Book类中有__str__方法, 所以直接打印;
            print(str(book))

    def addBook(self):
        pass

    def borrowBook(self):
        name = input("借阅书籍名称:")
        ret = self.checkBook(name)
        if ret != None:
            if ret.state == 0:
                print("书籍《%s》已经借出" % (name))
            else:
                ret.state = 0
                print("书籍《%s》已经借阅成功!" % (name))
        else:
            print("书籍《%s》不存在" % (name))

    def returnBook(self):
        pass

    def checkBook(self, name):
        for book in self.books:
            # book是对象
            if book.name == name:
                return book
            else:
                return None


manager = BookManger()
manager.Menu()
