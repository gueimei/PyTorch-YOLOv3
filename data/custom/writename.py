import os
from os import listdir, getcwd
from os.path import join
if __name__ == '__main__':
    source_folder='/home/PyTorch-YOLOv3/data/custom/images/'
    train_dest='/home/PyTorch-YOLOv3/data/custom/train_name.txt'
    val_dest='/home/PyTorch-YOLOv3/data/custom/val_name.txt'
    file_list=os.listdir(source_folder)
    train_file=open(train_dest,'a')
    val_file=open(val_dest,'a')
    for file_obj in file_list:
        file_path=os.path.join(source_folder,file_obj)
        file_name,file_extend=os.path.splitext(file_obj)
        file_num=int(file_name)
        tmp=file_num%10
        if(tmp==0):
            val_file.write(file_name+'\n')
        else:
            train_file.write(file_name+'\n')
    train_file.close()
val_file.close()
