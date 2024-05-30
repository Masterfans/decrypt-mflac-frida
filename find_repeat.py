import os
import sys
from pathlib import Path
import shutil


dir_name = "repeat_move"
move_dir = ''

def find_file(dir,filename):
    for file in os.listdir(dir):
        if os.path.isfile(os.path.join(dir,file)):
            name,suffix = os.path.splitext(file)
            if name == filename:
                return file

def search_move_file(removed_dir, file_list_dir):
    for file in os.listdir(file_list_dir):
        name,suffix = os.path.splitext(file)
        find = find_file(removed_dir, name)
        if find is not None:
            print(f"find file: {find}, move: {move_dir}")
            shutil.move(os.path.join(removed_dir,find),move_dir)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f'usage: {sys.argv[0]} 要移动重复文件目录 重复参考目录')
        sys.exit()
    move_dir = sys.argv[1] + "\\" + dir_name

    if not os.path.exists(move_dir):
        os.makedirs(move_dir)

    search_move_file(sys.argv[1],sys.argv[2])
