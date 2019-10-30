# -*- coding: utf-8 -*-
import os
import time


def get_dispatcher_from_path(file_path):
    for i in os.path.normpath(file_path).split('\\'):
        if "Диспетчер" in i:
            return i.split(' - ')[1]


def get_dispatcher_from_path2(file_path):
    return file_path.partition('Диспетчер')[2].partition(' - ')[2].partition('\\')[0]


def get_dispatcher_from_path3(file_path):
    return file_path.partition('\\')
    # .partition(' - ')[2].partition('\\')[0]


path = "C:\\work\\memo\\Графики ПДО\\Диспетчер-2 - Мудренко Татьяна Батьковна\\22 -ТОВ Авис Зернотрейд\\Екселька.xlsx"

if __name__ == "__main__":
    # t = time.time()
    # for i in range(100000):
    #     x = get_dispatcher_from_path(path)
    # print(time.time()-t)

    # t = time.time()
    # for i in range(100000):
    #     x = get_dispatcher_from_path2(path)
    # print(time.time()-t)

    print(get_dispatcher_from_path3(path))

    # 0.8720500469207764
    # 0.11200642585754395
