#This is a Rovarspraket script..
word=input()
def rovar(word):
    word=list(word)
    letters=('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')
    for string in word:
        if string==string in letters:
            word[word.index(string)]=string+'o'+string
    print(''.join(word))


rovar(word)

s=input()
def trans(s):
     cons='bcdfghjklmnpqrstvwxyz'
     print(''.join(l+'o'+l if l in cons else l for l in s))


trans(s)