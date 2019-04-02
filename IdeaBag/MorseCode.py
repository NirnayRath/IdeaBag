#Morse Code generator..
from collections import OrderedDict
i=input("Enter a string:")
a=list(i)
def Morse(i):
    morse=OrderedDict()
    morse['A']='._'
    morse['B']='_...'
    morse['C']='_._.'
    morse['D'] = '_..'
    morse['E'] = '.'
    morse['F'] = '.._.'
    morse['G'] = '__.'
    morse['H'] = '....'
    morse['I'] = '..'
    morse['J'] = '.___'
    morse['K'] = '_._'
    morse['L'] = '._..'
    morse['M'] = '__'
    morse['N'] = '_.'
    morse['O'] = '___'
    morse['P'] = '.__.'
    morse['Q'] = '__._'
    morse['R'] = '._.'
    morse['S'] = '...'
    morse['T'] = '_'
    morse['U'] = '.._'
    morse['V'] = '..._'
    morse['W'] = '.__'
    morse['X'] = '_.._'
    morse['Y'] = '_.__'
    morse['Z'] = '__..'
    morse['1'] = '.____'
    morse['2'] = '..___'
    morse['3'] = '...__'
    morse['4'] = '...._'
    morse['5'] = '.....'
    morse['6'] = '_....'
    morse['7'] = '__...'
    morse['8'] = '___..'
    morse['9'] = '____.'
    morse['0'] = '_____'
    morse[' '] = '  '

    print(''.join(morse[i] if i in morse.keys() else ' ' for i in a))

Morse(i)