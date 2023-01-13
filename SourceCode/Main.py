from tkinter import *
from PIL import ImageTk

def Flayppy_Bird():
    import FlappyBird

def Google_Translate():
    import GoogleTranslate

def QRCode():
    import QRCode

root = Tk()
root.title("Menu")
root.geometry('1024x250')
root.resizable(False, False)

background = ImageTk.PhotoImage(file= 'FlappyBird/Img/main_background.jpg')

LBL_Background = Label(root, image=background)
LBL_Background.place(x=0, y=0)

MainFrame = Frame(root, bg='white')
MainFrame.place(x = 135, y= 100)

#Button
BT_FlappyBird = Button(MainFrame,command= Flayppy_Bird , text='Flappy Bird',
                    font=('times new roman', 20, 'bold'), width=15, fg='white', bg='#3D85C6', cursor='hand2')
BT_FlappyBird.grid(row=0, column=1, pady=1, padx=1)

BT_GoogleTranslate = Button(MainFrame, command= Google_Translate, text='Google Translate',
                    font=('times new roman', 20, 'bold'),width=15, fg='white', bg='#3D85C6',cursor='hand2')
BT_GoogleTranslate.grid(row=0, column=2, pady=1, padx=1)

BT_QRCode = Button(MainFrame,command= QRCode, text='QRCode',
                    font=('times new roman', 20, 'bold'), width=15, fg='white', bg='#3D85C6', cursor='hand2')
BT_QRCode.grid(row=0, column=3, pady=1, padx=1)

root.mainloop()