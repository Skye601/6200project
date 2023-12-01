import numpy as np
import pandas as pd
import os
from collections import Counter


if __name__ == "__main__":
    path = "../Cosmodataset/train/"
    # path = "../Cosmodataset/test/"
    csv_files = [file for file in os.listdir(path) if file.endswith('.csv')]
    # 创建一个字典来保存每个人每个动作的数据
    data_dict = {}

    # 遍历所有csv文件
    for file in csv_files:
        # 解析文件名获取person_id、动作id和次数
        person_id = file[1:3]
        action_id = file[4:6]
        count = file.split('_')[1].split('.')[0]
        # print(person_id, action_id, count)

        # 读取csv文件数据
        file_path = os.path.join(path, file)
        df = pd.read_csv(file_path, header=None, usecols=[0, 1, 2])

        # 如果person_id和action_id在字典中不存在，则创建一个新的键值对
        if (person_id, action_id) not in data_dict:
            data_dict[(person_id, action_id)] = []

        # 将数据添加到相应的键值对中
        data_dict[(person_id, action_id)].append(df.values)

    print(data_dict.keys())
    action_ids = []
    for key, values in data_dict.items():
        person_id, action_id = key
        action_ids.append(action_id)
    # print(np.unique(np.array(action_ids)))
    print(Counter(action_ids))

    save_path = "../dataset_weight/COSMO_Train/"
    save_path = "../dataset_weight/COSMO_Test/"
    items = 1
    labels = ['06', '07', '12', '13', '14', '15', '17', '18', '19', '20', '21', '22', '29', '30']
    label_maps = {value: index for index, value in enumerate(labels)}
    print(label_maps)

    # # # 将数据保存到npy文件
    # for key, values in data_dict.items():
    #     person_id, action_id = key
    #     data = np.concatenate(values, axis=0).reshape(-1, 200, 3).astype(np.float32)
    #     y = label_maps[action_id]
    #     label = np.full(data.shape[0], y)
    #     # print(label)
    #     print(person_id, action_id, items, y, data.shape, label.shape)
    #     print(data.dtype)
    #     np.save(save_path+f'{items}-X.npy', data)
    #     np.save(save_path+f'{items}-Y.npy', label)
    #     np.save(save_path+f'{items}-W.npy', np.zeros(data.shape[0]))
    #
    #     items += 1


