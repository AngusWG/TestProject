#!/usr/bin/env python
# encoding: utf-8
# @Time   : 2022/10/23 02:55:51
# @author : zza
# @Email  : z740713651@outlook.com
# @File   : 书签导出.py

import json

bookmarks_path = (
    r"C:\Users\z7407\AppData\Local\Microsoft\Edge\User Data\Default\Bookmarks"
)
data = json.load( open(bookmarks_path, encoding="utf8"))


def handle_one(data):

    if data["type"] == "folder":
        # is dir
        dir_name = data["name"]
        # print(data)
        children = [handle_one(item) for item in data["children"]]
        return {dir_name: children}
    else:  # is item
        # print(data)
        return {data["name"]: data["url"]}



all_bookmarks = {
    "bookmark_bar": [handle_one(data["roots"]["bookmark_bar"])],
    "other": [handle_one(data["roots"]["other"])],
    "synced": [handle_one(data["roots"]["synced"])],
}

# pprint(all_bookmarks)


def print_data(data, deep):
    res = ""
    # print(data)
    for name, item in data.items():
        if isinstance(item, str):
            res += "  " * deep + f"- [{name}]{item}"
        else:
            items_str = "\n".join(print_data(i, deep + 1) for i in item)
            res += "  " * deep + f"- {name}\n" + items_str
    return res


print(print_data(all_bookmarks, 0))
