import os

os.chdir('..')

DIR_PATH_SEMI = r'semi_processed_files'
DIR_PATH_PROCESSED = r'processed_files'



def delete_temp_files():

    for file in os.listdir(DIR_PATH_SEMI):
        if not file.endswith(".c"):
            continue
        os.remove(os.path.join(DIR_PATH_SEMI, file))

    for file in os.listdir(DIR_PATH_PROCESSED):
        if not file.endswith(".c"):
            continue
        os.remove(os.path.join(DIR_PATH_PROCESSED, file))
