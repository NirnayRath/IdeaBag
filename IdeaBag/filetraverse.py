#traversing the directory..

import os,sys


path="F:/Videos/Hollywood"
path2="C:/Users/nEW u/Videos/Hollywood"

def filing():
    direc = os.listdir(path)
    direc2 = os.listdir(path2)
    for file in direc:
        if file not in direc2:
            print(file)

filing()




