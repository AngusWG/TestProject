#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/4/14 0014 16:31
# @author  : zza
# @Email   : 740713651@qq.com


def read_email_list(file_name):
    pass


def read_data(file_name):
    pass


def main():

    # 读取邮箱表
    mail_file = input("邮箱文件（默认 邮箱表.xlsx 按Enter键跳过）\n：")
    if not mail_file:
        mail_file = "邮箱表.xlsx"
    mail_list = read_email_list(mail_file)
    print("读取｛｝成功".format(mail_file))
    # 读取工资条信息
    data_file = input("工资文件（默认 工资表.xlsx 按Enter键跳过）\n：")
    if not data_file:
        data_file = "工资表.xlsx"
    data_list = read_data(data_file)

    # 邮箱发送
    q
    pass


if __name__ == '__main__':
    main()
