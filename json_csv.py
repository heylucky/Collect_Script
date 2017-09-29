# coding=utf-8
# __author__ = 'lyl'

import json
import csv

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def read_json(filename):
    """
    读取json格式的文件
    :param filename:  json文件的文件名
    :return: [{}, {}, {}, {}, {}，{} ......]
    """
    return json.loads(open(filename).read())

def write_csv(filename, data_list):
    """
    将python对象 [{}, {}. {}, {} ...] 写入到csv文件中
    :param filename:  生成的csv文件名
    :param data_list:  [{}, {}. {}, {} ...]
    :return: None
    """
    with open(filename,'w') as f:
        dict_writer = csv.DictWriter(f, data_list[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(data_list)


def write_csv2(filename, content_list):
    """
    与 write_csv 类似
    :param filename:
    :param content_list:
    :return:
    """
    with open(filename, 'w') as f:
        csv_writer = csv.writer(f)

        head_list = content_list[0].keys()
        data_list = [content.values() for content in content_list]
        csv_writer.writerow(head_list)
        csv_writer.writerows(data_list)


if __name__ == "__main__":

    # 读出json数据内容
    content_list = read_json('lagou_info_lin3.json')
    # 将数据写入到csv文件
    write_csv( "lagou_info_lin3.csv", content_list)