import os
import datetime

base_path = os.path.dirname(__file__)
path_file = os.path.dirname(os.path.dirname(os.path.join(base_path)))
j_path = os.path.join(path_file, "eugene_okulik", "hw_13", "data.txt")


def geners():
    with open(j_path) as file:
        for i in file.readlines():
            lst_line = i.split()
            date_time = f"{lst_line[1]} {lst_line[2]}"
            yield datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f')


gen = geners()
print(next(gen) + datetime.timedelta(days=7))
print(next(gen).strftime("%A"))
print((datetime.datetime.now() - next(gen)).days)
