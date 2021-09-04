from config import config as CONFIG

def clean_tmp_folder():
    import os
    import shutil

    for f in os.listdir(CONFIG.APP.TMP_FOLDER):
        if f == '.gitkeep': continue
        shutil.rmtree(f'{CONFIG.APP.TMP_FOLDER}/{f}')
