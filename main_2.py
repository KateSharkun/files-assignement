
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os 
import shutil

'''

wincpy doesnt accept this code but it still works correct

'''


#Escaping backslashes in windows path


cache = os.path.join(os.getcwd(), 'cache')
data_zip = os.path.join(os.getcwd(), 'data.zip') 

cache = cache.replace('\\', '/')
data_zip = data_zip.replace('\\', '/')



def clean_cache():
    if os.path.exists(cache):
        shutil.rmtree(cache)
    os.makedirs(cache)


def cache_zip(zip_path: str, cache_path: str):
    shutil.unpack_archive(zip_path, cache_path)


def cached_files():
    files_names_dir = [entry.path for entry in os.scandir(cache) if entry.is_file()]
    return files_names_dir


def find_password(files):
    for fpath in files:
        file_text =  open(fpath, 'r')
        f = file_text.readlines()
        for line in f:            
            if 'password' in line:               
                password = line.split(' ')[-1]
                print(password)
                return(password)
            

        file_text.close()
    


        
if __name__ == "__main__":
    clean_cache()   
    cache_zip(data_zip, cache)
    files = cached_files()
    find_password(files)
    
    
        





