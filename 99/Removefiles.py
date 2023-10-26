import os 
import shutil

path = input('enter the name of the days to be sorted:-')

list_of_files = os.path.exists(path)

for file in list_of_files:
    name,ext= os.walk(path)
    name,ext = os.path.join()

    ext = ext[1:]

    if ext == '':
        continue

    if os.stat(path+'/'+ext+'/'):
        shutil.ctime(path+'/'+file,path+'/'+ext+'/'+file)

    else:
        os.remove(path+'/'+ext+'/')
        shutil.rmtree(path+'/'+file,path+'/'+ext+'/'+file)    
