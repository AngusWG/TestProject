# pip install Pillow
from PIL import Image
import os
import shutil


def main(end_with="jfif", to_format="jpg"):
    root = os.path.dirname(os.path.abspath(__file__))
    # root  = %pwd
    print(root)
    old_dir = os.path.join(root, "old")
    if not os.path.exists(old_dir):
        os.makedirs(old_dir)
    count = 0
    for dirs, subdir, files in os.walk(root):
        if old_dir == dirs:
            continue
        for file in files:
            if file[-4:] == end_with:
                file_name = os.path.join(dirs, file)
                img = Image.open(file_name)
                # file ends in .jfif, remove 4 characters2
                print(file_name)
                # add jpg and save
                target = os.path.join(dirs, file[:-4] + "." + to_format)
                img.save(target)
                # mv to new folder
                shutil.move(file_name, os.path.join(old_dir, file))
                # remove
                # os.remove(file_name)


if __name__ == "__main__":
    main()
