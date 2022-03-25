import hashlib
import glob
import os


def sha1_calculate(filename: str) -> str:
    sha1 = hashlib.sha1()
    b = bytearray(64 * 1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f_in:
        for n in iter(lambda: f_in.readinto(mv), 0):
            sha1.update(mv[:n])
    return sha1.hexdigest()


def traverse_dir(root_dir: str) -> str:
    for filename in glob.iglob(root_dir + '**/**', recursive=True):
        yield filename


def files_number(root_dir: str) -> int:
    n_files = 0
    for root, dirs, files in os.walk(root_dir, topdown=False):
        n_files += len(files)
    return n_files
