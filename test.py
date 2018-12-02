# -*- coding: utf-8 -*-
from typing import Union, Iterable

from numpy.core.multiarray import ndarray
import time  # 引入time模块


__author__ = 'Zhao'

import numpy as np

def file_read():
    file = open('ks_4_0.txt', 'r', encoding='utf8')
    item = []
    for lines in file:
        # print(lines.split())
        new_line = []
        for element in lines.split():
            new_line.append(int(element))
        item.append(new_line)

    return np.array(item)

if __name__ == '__main__':
    time1 = time.time()

    print('program starts at: ', time1)
    lines = file_read()
    total_good_num = int(lines[0][0])
    total_capacity = int(lines[0][1])
    items = lines[1:]
    print(items)
    items = np.sort(items,0,'quicksort')
    print(items)

    # aim = [31, 29, 27, 23, 21, 19, 17, 15]
    # sum = 0
    # for ele in aim:
    #     # print(ele)
    #     sum += int(items[ele,0])
    #
    # print(sum)