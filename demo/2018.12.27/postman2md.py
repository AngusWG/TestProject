#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/12/10 15:31
# @author  : zza
# @Email   : 740713651@qq.com


import sys
import json
from pprint import pprint


def gest_error(code):
    print("ERROR !", code, file=sys.stderr)
    print("USAGE : ./postman_to_md.py <path_to_file> <output_file>\n")
    print("\t- path_to_file ->\tpath to the postman json collection")
    print("\t- output_file ->\tpath to the output file")
    exit(84)
    return


def write_info(info):
    to_write = ""
    to_write += "# " + info["name"] + "\n"
    to_write += "description" + "\n"
    to_write += info.get('description') + "\n"
    to_write += "______________________________________\n"
    to_write += "# Requests\n"
    return to_write


def write_request(elem):
    to_write = ""
    to_write += "#### {name}\n".format(method=elem["request"]["method"], name=elem["name"])
    to_write += "* {method}\n".format(method=elem["request"]["method"])
    to_write += "* {description}\n".format(description=elem["request"].get("description", "No description"))
    to_write += "* URL: `{url}`\n".format(url=elem["request"]["url"]['raw'])

    # get_query
    if elem["request"]["url"].get('query') is not None:
        to_write += "##### Params\n"
        to_write += "| key | description | default |\n"
        to_write += "| ---- | ---- | ---- |\n"
        for query in elem["request"]["url"]['query']:
            to_write += "| {} | {} | `{}` |\n".format(query["key"], query.get('description', ""), query["value"])

    # header
    if len(elem["request"]["header"]) > 1:
        to_write += "##### Headers\n"
        to_write += "| key | value |\n"
        to_write += "| ---- | ---- |\n"
    for header in elem["request"]["header"]:
        to_write += "| {} | `{}` |\n".format(header["key"], header["value"])

    if elem['request']['body'].get('raw') is not "":
        to_write += "##### Body \n"
        to_write += "```yml \n{}\n```\n".format(elem['request']['body']['raw']).replace("\r\n","\n")

    if elem["response"] != "{}" and len(elem["response"]) > 0:
        to_write += "##### Sample Response\n"
        for res in elem["response"]:
            to_write += res["name"] + "\n"
            to_write += "```json\n{}\n```\n".format(json.dumps(json.loads(res["body"]), indent=4) )

    return to_write + "\n"


def write_items(items):
    to_write = ""
    for elem in items:
        if elem.get('item'):
            to_write += "### {name}\n".format(name=elem["name"])
            to_write += "* {description}\n\n".format(description=elem.get("description", "No description"))
            to_write += write_items(elem.get('item'))
            to_write += "---\n\n"
        else:
            to_write += write_request(elem)
    return to_write


# def main(input_file=sys.argv[1], output_file=sys.argv[2]):
def main(input_file, output_file):
    print(input_file)
    try:
        f = open(input_file, "r", encoding="utf8")
    except:
        gest_error("file could not be read")
        return

    file = f.read()
    f.close()

    data = json.loads(file)

    to_write = ""
    to_write += write_info(data["info"])
    to_write += write_items(data["item"])

    try:
        f = open(output_file, "w", encoding="utf8")
        f.write(to_write)
        f.close()
    except:
        gest_error("file could not be open/written")


if __name__ == '__main__':
    # print(sys.argv[1])
    main(r'C:\Users\admin\Desktop\contest.postman_collection.json', 'contest.postman_collection.md')
