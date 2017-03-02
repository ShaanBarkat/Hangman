
#Shaan Barkat

from tkinter import *
def mask(string,exceptions):
    string = string.upper()
    exceptions = exceptions.upper()
    word = ''
    for i in string:
        if i not in exceptions:
            word += '?'
        else:
            word += i
    return word
 

class hangman(Frame):
    def __init__(self,string,parent=None):
        self.rightkeys = ''
        self.wrongkeys = ''
        Frame.__init__(self,parent)
        self.word = string.upper()
        self.answer = Entry(self)
        self.answer.grid(row=0,column=2,columnspan=4)
        maskedstring = mask(self.word,'')
        self.answer.insert(END,mask(self.word,''))
        Label(self,text='Word:').grid(row=0,column=0,columnspan=2)
        self.right = Entry(self)
        self.right.grid(row=1,column=2,columnspan=4)
        Label(self,text='Right:').grid(row=1,column=0,columnspan=2)
        self.wrong = Entry(self)
        self.wrong.grid(row=2,column=2,columnspan=4)
        Label(self,text='Wrong:').grid(row=2,column=0,columnspan=2)
        labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(len(labels)):
            def cmd(key=labels[i]):
                self.click(key)
            b = Button(self,command=cmd,text=labels[i],width=5,height=3)
            b.grid(row=i//6+3,column=i%6)

    def click(self,key):
            if key in self.word:
                if key not in self.rightkeys:
                    self.rightkeys += key
                    self.right.insert(END,key)
                    self.answer.delete(0,END)
                    self.answer.insert(END,mask(self.word,self.rightkeys))
            elif key not in self.word:
                if key not in self.wrongkeys:
                    self.wrongkeys += key
                    self.wrong.insert(END,key)
            if self.answer.get() == self.word:
                messagebox.showinfo('Hangman','You Win!')
            elif len(self.wrong.get()) == 6:
                messagebox.showinfo('Hangman','You Lose!')


