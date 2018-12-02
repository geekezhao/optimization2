# -*- coding: utf-8 -*-
from typing import Union, Iterable

from numpy.core.multiarray import ndarray
import time  # 引入time模块


__author__ = 'Zhao'

import numpy as np

def file_read():
    file = open('ks_100_0.txt', 'r', encoding='utf8')
    item = []
    for lines in file:
        new_line = []
        for element in lines.split():
            new_line.append(int(element))
        item.append(new_line)

        # item.append(lines.split())

    return np.array(item)

def init(total_good_num, total_capacity):
    matrix = np.zeros((total_good_num, total_capacity), dtype=np.int32)

    return matrix


if __name__ == '__main__':
    time1 = time.time()

    print('program starts at: ', time1)
    lines = file_read()
    total_good_num = int(lines[0][0])
    total_capacity = int(lines[0][1])
    items = lines[1:]
    #
    # items = np.sort(items,0,'quicksort')
    # print(items)
    sum_matrix = init(total_good_num + 1, total_capacity + 1)
    # rows are values under different capacity and columes are different goods set

    capacity = 1
    while capacity <= total_capacity:
        for i in range(1, total_good_num + 1):
            weight = int(items[i - 1][1])
            price = int(items[i - 1][0])

            value = max(int(np.max(sum_matrix[:max((i),1), :max(max(capacity-weight+1,0),1)]) + price*min(max(capacity-weight+1,0),1)),
                        int(np.max(sum_matrix[:max(i+1,1), :max(capacity+1,1)])))  # 这里需要重新审核 value的构成
            # 此时若为节点(goods = 6, capacity = 8)， 则应当取Matrix[6,8]除了(6,8)点以为加的全部的值，但是这个点初始化为0，因此不影响
            sum_matrix[i,capacity] = value

        capacity += 1

    print(sum_matrix)
    print('max value = ', sum_matrix[-1,-1])

    item_list = []
    value_list = []
    space_list = []

    item_location = total_capacity
    while item_location > 1:
        max_temp = np.max(sum_matrix)
        candidate = np.where(sum_matrix == max_temp)
        # 当前矩阵中整体值最大的分块矩阵

        # print(candidate)
        # print(candidate[0])
        # print(candidate[0][0])
        item_list.append(candidate[0][0]) # 本分块矩阵中坐标最小的点的横坐标
        value_list.append(int(items[candidate[0][0]-1, 0]))
        space_list.append(int(items[candidate[0][0]-1, 1]))

        sum_matrix = sum_matrix[:candidate[0][0], :candidate[1][0]+1-int(items[candidate[0][0]-1, 1])]

        item_location = candidate[1][0]+1-int(items[candidate[0][0]-1, 1])

    # print(item_list)

    # ----- 用于验证序列查询结果 START ----- #
    for i in range(0,len(item_list)):
        print('#', item_list[i], ' which has a value of',value_list[i],' and a space of',space_list[i])

    print('sum = ', sum(value_list), ' ; space = ',sum(space_list), ' ; remains = ', total_capacity - sum(space_list))

    # ----- 用于验证序列查询结果 END ----- #

    time2 = time.time()
    print('program ends at: ', time2)
    print('program takes time: ', (time2 - time1)/3600)


