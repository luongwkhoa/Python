from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import qrcode
import cv2
import numpy as np
from pyzbar.pyzbar import decode #giải mã QR-BarCode
from PIL import Image, ImageTk

root = tk.Tk()
root.title('QRCode Create')
root.geometry('900x550')
root.resizable(False, False)

def CreateQRCode():

    Input_Length = Input.get("1.0", "end-1c")

    if Input_Length == '':
        messagebox.showerror('Input Error', "Please enter the characters!")
    else:
        #Create - L:Low, M:Medium, Q:Quarter, H:High
        qr = qrcode.QRCode(version = 4, error_correction = qrcode.ERROR_CORRECT_M, box_size=5, border=2) #Tạo đối tượng QR
        qr.add_data(Input_Length) #Thêm dữ liệu
        qr.make(fit = True) #Tận dụng khung hình để tạo ra mã QRcode tối ưu không gian trốn

        CreateImage = qr.make_image(fill_Color = 'black', back_color = 'white') #Màu của QRCode
        CreateImage.save('QRCode/MyQRCode.png')#Lưu thành tên MyQRCode.png

        QR_Output = Text(frameMain, width = 250, height = 250, borderwidth= 0, relief= GROOVE, font = ('verdana', 15))
        QR_Output.place(anchor='center',x = 450, y = 385)
        
        ImageShow = ImageTk.PhotoImage(Image.open("QRCode/MyQRCode.png"))
        ImageLabel = ttk.Label(QR_Output, image=ImageShow)
        ImageLabel.image = ImageShow
        ImageLabel.pack()

        Input.delete(1.0, 'end')

def ReadQrCode():
    Input.delete(1.0, 'end')
    #Scan and Read
    Camera = cv2.VideoCapture(0) #Phát hiện camera của máy tính
    while True:
        _, frame = Camera.read()
        Key_pressed = cv2.waitKey(1)
        File_open = open('QRCode/QRCode_logs.txt', 'a') #Mở tập tin Qrcode_logs và cho phép ghi đè

        for code in decode(frame): #Tạo biến code thuộc decode
            art = np.array([code.polygon], np.int32) #Tạo mảng 1 chiều
            art = art.reshape((-1, 1, 2)) #1 dòng, 2 cột (seft, shape, order)
            cv2.polylines(frame, [art], True, (0, 0, 255), 2) #Nối kín các đỉnh với nhau

        cv2.imshow('QRCode Scanner', frame)

        if Key_pressed == 13: #Khi bấm phím ENTER sẽ tiến hành đọc QR
            data = code.data.decode('UTF-8')
            File_open.write(data + '\n')
            Input.insert('end', data)
            Input.insert('end', '\n')
        
        if Key_pressed == 27: #Khi ấn phím ESC thì thoát
            break

    File_open.close()
    Camera.release()
    cv2.destroyAllWindows()

frameMain = Frame(root, width= 910, height= 560, relief= GROOVE, borderwidth= 5, bg= '#EEEEEE')
frameMain.place(x = 0, y = 0)
Label(root, text = "QRCode Create", font = ("Segoe-UI 20 bold"), fg = "black", bg = '#3D85C6').pack(pady = 10)

Input = Text(frameMain, width= 77 , height= 8, borderwidth= 0, relief= GROOVE, font= ('Segoe-UI', 15))
Input.place(x= 20, y= 80)

#Button
bt_Create = Button(frameMain, command= CreateQRCode, text = "Create", relief=RAISED, borderwidth=4, font=('verdana', 12, 'bold'), bg = '#3D85C6', fg = 'white', cursor="hand2")
bt_Create.place(x= 20, y= 40)

bt_Scan = Button(frameMain, command= ReadQrCode, text = "Scan", relief=RAISED, borderwidth=4, font=('verdana', 12, 'bold'), bg = '#3D85C6', fg = 'white', cursor="hand2")
bt_Scan.place(x= 806, y= 40)

root.mainloop()