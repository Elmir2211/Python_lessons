# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

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

