import os

print(os.path.splitext(os.path.basename("C:/Users/nEW u/Music"
                                        "/English/Nirvana/Playlist.txt")))

file=open("C:/Users/nEW u/Music/English/Nirvana/Playlist.txt")
dir={}
for a in file.read().split():
    if a in dir:
        dir[a]=1
    else:
        dir[a]=+1
for k,v in dir.items():
    print(k,v)

file.close()