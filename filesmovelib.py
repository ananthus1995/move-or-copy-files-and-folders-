import os
import shutil
import time


def move_file(root_source_dir=None, root_destination_dir=None):
    try:
        for src_dir, dirs, files in os.walk(root_source_dir):

            dst_dir = src_dir.replace(root_source_dir, root_destination_dir)
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
                                os.path.splitext(file_)[0] + '_' + str(int(time.time())) + os.path.splitext(file_)[1])
                        temp_src_file = src_dir + '/' + temp_src_filepath
                        # continue
                        # print(temp_src_file)
                        os.rename(src_file, temp_src_file)
                        shutil.copy(temp_src_file, dst_dir)


                        # os.remove(temp_src_file)

                else:
                    shutil.copy(src_file, dst_dir)


    except FileNotFoundError:

        print("File does not exist")


def main(root_source_dir, root_destination_dir):
    move_file(root_source_dir, root_destination_dir)


if __name__ == '__test2__':
    move_file()
