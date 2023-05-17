# =====================================================
# @date 2023.05.17
# @author yuteng 
# @file main.py
# =====================================================

import pandas as pd
import numpy as np


def run():
    # 读取数据
    data = pd.read_csv('data/fyx_chinamoney.csv', header=None)
    # print(data.to_string())
    # 利用np转置，降低维度
    data_array = np.array(data).T.squeeze(0)
    # 转换为列表
    data_list = data_array.tolist()
    # print(data_list)
    cut_len = 80
    # 创建list用于保存切分后的数据
    data_cut_list = [data_list[i:(i + cut_len)]
                     for i in range(0, len(data_list), cut_len)]

    # 打印数据
    for item in data_cut_list:
        print(len(item))
        print(item)
        print('*' * 20)
        pass

    pass


if __name__ == '__main__':
    run()
    pass
