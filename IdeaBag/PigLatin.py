#This creates Pig Latin form of a normal word...
class pigLatin:
    def __init__(self):
        self.word=str(input("Enter the word: "))
        self.word=list(self.word)
    def Pig(self):
        self.word=self.word[::-1] + ['a', 'y']
        print(''.join(self.word))

call=pigLatin()
call.Pig()
