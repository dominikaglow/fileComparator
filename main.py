import hashlib
import os
from os import listdir
from os.path import isfile, join


def file_checksum(filepath):
    with open(filepath, 'rb') as f:
        m = hashlib.md5()
        while True:
            data = f.read(8192)
            if not data:
                break
            m.update(data)
    return m.hexdigest()


def checkIfTheSame(dir1, dir2, ext):
    files1 = [join(dir1, f) for f in listdir(dir1) if isfile(join(dir1, f)) and f.endswith(ext)]
    files2 = [join(dir2, f) for f in listdir(dir2) if isfile(join(dir2, f)) and f.endswith(ext)]

    cs1 = []
    cs2 = []
    res = set()
    for file in files1:
        if file.endswith(ext):
            cs1.append(file)

    for file in files2:
        if file.endswith(ext):
            cs2.append(file)

    # print(cs2)

    for f1 in cs1:
        for f2 in cs2:
            if os.path.basename(f1) == os.path.basename(f2):
                if os.path.getsize(f1) != os.path.getsize(f2) or file_checksum(f1) != file_checksum(f2):
                    res.add(os.path.basename(f1))

    for elem in res:
        print(elem)


if __name__ == '__main__':
    d1 = input("Enter name of the first directory: ")
    d2 = input("Enter name of the second directory: ")
    ext = input("Enter file extension (for example .txt): ")
    checkIfTheSame(d1, d2, ext)
