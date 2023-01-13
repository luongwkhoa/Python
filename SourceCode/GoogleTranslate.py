from tkinter import *
import tkinter as tk
import pyttsx3
import speech_recognition
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox

Text_Speech = pyttsx3.init()
root = tk.Tk()
root.title('Translate')
root.geometry('900x600')
root.resizable(False, False)

ear = speech_recognition.Recognizer()

def Microphone(): #Nhập từ microphone
    with speech_recognition.Microphone() as mic:
        audio = ear.listen(mic)
    try:
        Text_Input.insert('end', ear.recognize_google(audio,language="vi-VI"))
    except:
        Text_Input.insert('end', "Error! Error, can't hear clearly")

def Speech(): #Phát âm
    Text_Speech.say(Text_Output.get("1.0", "end-1c"))
    Text_Speech.runAndWait()

def ReadFile(): #Đọc file từ tập tin
    Clear()
    f = open("Translate/intPut.txt", encoding= 'utf8')
    readText = f.read()
    f.close()
    Text_Input.insert('end', readText)

def Translate(): #Dịch
    lang_1ength = Text_Input.get("1.0", "end-1c")
    choose = choose_language.get()
    
    if lang_1ength == '':
        messagebox.showerror('Input Error', "Please enter the characters to translate!")
    else:
        Text_Output.delete(1.0, 'end')
        translator = Translator()
        outPut = translator.translate(lang_1ength, dest=choose)
        Text_Output.insert('end', outPut.text)

def Clear(): #Xóa nội dung ở 2 frame
    Text_Input.delete(1.0, 'end')
    Text_Output.delete(1.0, 'end')

frameMain = Frame(root, width= 900, height= 600, relief= GROOVE, borderwidth= 5, bg= '#EEEEEE')
frameMain.place(x = 0, y = 0)
Label(root, text = "Translate", font = ("Segoe-UI 20 bold"), fg = "black", bg = '#7095E4').pack(pady = 10)

#Combobox
autoSL= tk.StringVar()
auto_select = ttk.Combobox(frameMain, width= 27, textvariable= autoSL, state= 'randomly', font= ('verdana', 10, 'bold'))
auto_select['values'] = ('Language detection',)
auto_select.place(x= 140, y= 75)
auto_select.current(0)

language = tk.StringVar()
choose_language = ttk.Combobox(frameMain, width= 27, textvariable= language, state= 'randomly', font= ('verdana', 10, 'bold'))
choose_language['values'] = (
                                'Afrikaans','Albanian','Amharic','Arabic','Armenian','Azerbaijani','Basque','Belarusian','Bengali','Bosnian','Bulgarian',
                                'Catalan','Cebuano','Chichewa','Chinese (simplified)','Chinese (traditional)','Corsican','Croatian','Czech','Danish','Dutch',
                                'English','Esperanto','Estonian','Filipino','Finnish','French','Frisian','Galician','Georgian','German','Greek','Gujarati',
                                'Haitian creole','Hausa','Hawaiian','Hebrew','Hindi','Hmong','Hungarian','Icelandic','Igbo','Indonesian','Irish','Italian','Japanese',
                                'Javanese','Kannada','Kazakh','Khmer','Korean','Kurdish (kurmanji)','Kyrgyz','Lao','Latin','Latvian','Lithuanian','Luxembourgish',
                                'Macedonian','Malagasy','Malay','Malayalam','Maltese','Maori','Marathi','Mongolian','Myanmar (burmese)','Mepali','Norwegian',
                                'Odia','Pashto','Persian','Polish','Portuguese','Punjabi','Romanian','Russian','Samoan','Scots gaelic','Serbian','Sesotho',
                                'Shona','Sindhi','Sinhala','Slovak','Slovenian','Somali','Spanish','Sundanese','Swahili','Swedish','Tajik','Tamil','Telugu',
                                'Thai','Turkish','Ukrainian','Urdu','Uyghur','Uzbek','Vietnamese','Welsh','Xhosa','Yiddish','Yoruba','Zulu',                               
                            )   
choose_language.place(x= 545, y= 75)
choose_language.current(21)

#Button
Text_Input = Text(frameMain, width= 31, height= 16, borderwidth= 0, relief= GROOVE, font= ('verdana', 15))
Text_Input.place(x= 20, y= 110)

Text_Output = Text(frameMain, width= 31, height= 16, borderwidth= 0, relief= GROOVE, font= ('verdana', 15))
Text_Output.place(x= 460, y= 110)

bt_Dich = Button(frameMain, command= Translate, text = "Translate", relief=RAISED, borderwidth=4, font=('verdana', 12, 'bold'), bg = '#3D85C6', fg = 'white', cursor="hand2")
bt_Dich.place(x= 170, y= 539)

bt_Xoa = Button(frameMain, command= Clear, text = "Delete", relief=RAISED, borderwidth=4, font=('verdana', 12, 'bold'), bg = '#3D85C6', fg = 'white', cursor="hand2")
bt_Xoa.place(x= 600, y= 539)

bt_Doc = Button(frameMain, command= Speech, text = "Listening", relief=RAISED, borderwidth=4, font=('verdana', 12, 'bold'), bg = '#3D85C6', fg = 'white', cursor="hand2")
bt_Doc.place(x= 680, y= 539)

bt_DocFile = Button(frameMain, command= ReadFile, text = "Input", relief=RAISED, borderwidth=4, font=('verdana', 12, 'bold'), bg = '#3D85C6', fg = 'white', cursor="hand2")
bt_DocFile.place(x= 10, y= 25)

bt_Microphone = Button(frameMain, command= Microphone, text = "Microphone", relief=RAISED, borderwidth=4, font=('verdana', 12, 'bold'), bg = '#3D85C6', fg = 'white', cursor="hand2")
bt_Microphone.place(x= 10, y= 66)

root.mainloop(); 