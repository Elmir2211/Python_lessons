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
