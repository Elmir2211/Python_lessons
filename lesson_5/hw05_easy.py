# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import directory.creat_dir as cdir
print(os.listdir())
cdir.mk_dir()
print(os.listdir())
cdir.rm_dir()
print(os.listdir())

# скрипт:
import os
def mk_dir():
    for i in range(9):
        t='dir'+str(i+1)
        dir_path = os.path.join(os.getcwd(), t)
        try:
            os.mkdir(dir_path)
            print(t+': создана папка с таким именем')
        except FileExistsError:
            print(t+': Такая папка уже существует!')

def rm_dir():
    for i in range(9):
        t='dir'+str(i+1)
        dir_path = os.path.join(os.getcwd(), t)
        try:
            os.rmdir(dir_path)
            print(t+': эта папка удалена')
        except FileNotFoundError:
            print(t+': Такого файла нету')

#####################################################################################################################

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.



# скрипт:
def dir_is():
    import os
    lst=os.listdir()
    new_lst=[]
    for i in range(len(lst)):
        dir_path = os.path.join(os.getcwd(), lst[i])
        if os.path.isdir(dir_path)==True:
            new_lst.append(lst[i])
    print(new_lst)

dir_is()

##############################################################################################################################
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

#скрипт
def file_copy():
    import shutil
    import sys
    first_file = sys.argv[0]
    copy_file = first_file + '.backup'
    shutil.copy(first_file, copy_file)
file_copy()