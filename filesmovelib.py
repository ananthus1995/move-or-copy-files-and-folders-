import os
import shutil
import time

import logging

logger = logging.getLogger(name='move_files')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('filess.log')
stream_handler = logging.StreamHandler()

file_handler.setLevel(logging.INFO)

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def move_file(root_source_dir=None, root_destination_dir=None):
    for src_dir, dirs, files in os.walk(root_source_dir):
        try:
            dst_dir = src_dir.replace(root_source_dir, root_destination_dir)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
                logger.info(f'folder created: {dst_dir}')

            for file_ in files:
                # print(file_)
                src_file = os.path.join(src_dir, file_)
                dst_file = os.path.join(dst_dir, file_)

                if os.path.exists(dst_file):

                    # if os.path.isfile(dst_file)
                    temp_src_files = (
                            os.path.splitext(file_)[0] + '_' + str(int(time.time())) + os.path.splitext(file_)[1])
                    temp_src_filepath = src_dir + '/' + temp_src_files
                    # continue

                    os.rename(src_file, temp_src_filepath)

                    shutil.move(temp_src_filepath, dst_dir)
                    logger.info(f'same file name found:{file_} renamed to {temp_src_files} moved to {dst_dir}')
                    # print("done...")

                else:

                    if shutil.move(src_file, dst_dir):
                        # logger.info(src_file)
                        logger.info(f"file: {file_} moved from {src_dir} to {dst_dir}")
                    else:
                        logger.critical('cannot move')

        except FileNotFoundError as e:
            print(e)
    else:
        print("No new files found")


    # except FileExistsError as error:
    #     print(error)
    #
    # except FileNotFoundError:
    #     logger.critical("File does not exist")


def main(root_source_dir, root_destination_dir):
    move_file(root_source_dir, root_destination_dir)


if __name__ == '__move_files__':
    move_file()
