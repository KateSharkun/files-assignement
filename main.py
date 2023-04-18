__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os 
import shutil


def clean_cache():
    if os.path.exists(r'C:\Users\Admin\Documents\Winc\hello-world\files\cache'):
        shutil.rmtree(r'C:\Users\Admin\Documents\Winc\hello-world\files\cache')
    os.makedirs(r'C:\Users\Admin\Documents\Winc\hello-world\files\cache')


def cache_zip(zip_path: str, cache_path: str):
    zip_path = zip_path.replace('\\', "//" )
    cache_path = cache_path.replace('\\', "//" )
    shutil.unpack_archive(zip_path, cache_path)




def cached_files():
    files_names_dir = [entry.path for entry in os.scandir(r'C:\Users\Admin\Documents\Winc\hello-world\files\cache') if entry.is_file()]
    return files_names_dir



def find_password(files):
    for fpath in files:
        file_text =  open(fpath, 'r')
        f = file_text.readlines()
        for line in f:            
            if 'password' in line:               
                password = line.split(' ')[-1]
                return(password)

        file_text.close()
    













    
 
