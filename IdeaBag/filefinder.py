

import os,sys
extensions=['exe','io','jpg','jpeg','png','mkv','mp4','mp3','m4a','txt','ini','lnk','db','webm','sync','wma','MP3','srt','zip','avi','fdmdownload','dat','MP4',
            'VOB','idx','sub','rar','smi','nfo','sfv','SRT','android']
search="Limitless.2011.Unrated.1080p.BluRay.H264.AAC-RARBG"
path="C:/Users/nEW u/Videos"

a=list(path.split('/'))
print(a)
scan=os.listdir(path)
def searching(a,path,scan):
    if search in scan:
        print("\n\n(",search ,") is in (",path,")\n\n\n")
        return

    else:
        for q in scan :
            p=q.split('.')
            if p[-1] not in extensions:
                a.append(q)
                path=path+'/'+q
                scan=os.listdir(path)
                print(path)
                searching(a, path, scan)
                a.pop()
                path='/'.join(a)
                print(path," not found here!!!")
            


searching(a,path,scan)