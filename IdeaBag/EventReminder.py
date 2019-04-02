#An Alarm clock you set and it gives you an alert when present time is true..
import time
import winsound
'''pyglet.lib.load_library('avbin')
pyglet.have_avbin=True'''
import os
name=input("Enter your name: ")
print("Your name is ",name)

hh=int(input("Enter the hh you want the alarm.."))
mm=int(input("Enter the mm you want the alarm.."))

print("Hello ",name)
print("You want the alarm to alert you at ",hh,':',mm )
t=hh*3600+mm*60
def alarm(t):
    while True:
        now=time.localtime()
        print(now)
        if now.tm_hour==int(hh)and now.tm_min==int(mm):
            print("Alarm now!!")
            memoryfile=open("E://Python-ATOM//Python//IdeaBag//Coldplay_-_Everglow_Single_Version_-_Official_vide.wav", "rb").read()
            winsound.PlaySound(memoryfile,winsound.SND_MEMORY)
        #sound.play()
            timeout=60-now.tm_sec
            if timeout==0:
                break
            break
            alarm(t)

        else:
            print('no alarm')

    #if nonBlockingRawInput('', timeout) == 'stop':
     #   break
alarm(t)