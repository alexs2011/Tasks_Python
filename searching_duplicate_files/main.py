from os import path

import utils

path_name = "D:\Фото"

d = {}

n_files = utils.files_number(path_name)

for i, cur_path in enumerate(utils.traverse_dir(path_name)):
    if path.isfile(cur_path):
        sha1 = utils.sha1_calculate(cur_path)
        d[sha1] = d.setdefault(sha1, [])
        d[sha1].append(cur_path)
    if i % 100 == 0:
        print(f'Processed {i} files from {n_files}')

utils.save_to_file(d)
