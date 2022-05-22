import os
import tarfile


def tardir(path, tar_name):
    tar_handle = tarfile.open(tar_name, "w:gz")
    for root, dirs, files in os.walk(path):
        for file in files:
            tar_handle.add(os.path.join(root, file))
    tar_handle.close()

tardir('/home/sirius/scripts', 'tar.gz')

