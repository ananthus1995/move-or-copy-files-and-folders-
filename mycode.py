import os

import shutil
from datetime import datetime
import time

root_src_dir = r'/home/user/ann/myfolder'
root_dst_dir = r'/home/Documents'
now = datetime.now()

try:
    for src_dir, dirs, files in os.walk(root_src_dir):

        dst_dir = src_dir.replace(root_src_dir, root_dst_dir)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

        for file_ in files:
            # print(file_)
            src_file = os.path.join(src_dir, file_)
            # print(src_file)
            dst_file = os.path.join(dst_dir, file_)

            if os.path.exists(dst_file):
                # print(dst_file)

                if os.path.isfile(dst_file):
                    # print("dst_file")

                    temp_src_filepath = (
                                os.path.splitext(file_)[0] + str(int(time.time())) + os.path.splitext(file_)[1])
                    temp_src_file = src_dir + '/' + temp_src_filepath
                    # continue
                    # print(temp_src_file)
                    os.rename(src_file, temp_src_file)

                    shutil.move(temp_src_file, dst_dir)
                    # os.remove(temp_src_file)

            else:
                shutil.move(src_file, dst_dir)

except Exception as e:
    print(e)
