from tkinter import *
from simplecrypt import encrypt, decrpt
from tkinter import filedialog
import os

root = Tk()
root.geometry("500x,620")
root.config(bg='#ADC698')

file_name_entry = ''
encryption_text_data = ''
decryption_text_data = ''

def saveData():
    global file_name_entry
    global encryption_text_data
    file_name = file_name_entry.get()
    file = open(file_name+".txt", "w")
    data = encryption_text_data.get("1.0",END)
    ciphercode = encrypt('XYZ', data)
    hex_string = ciphercode.hex()
    print(hex_string)
    file.write(hex_string)
    file_name_entry.delete(0, END)
    encryption_text_data.delete(1.0,END)
    messagebox.showinfo("Update","Success")


def startDecryption():
    global file_namme_entry
    global decryption_text_data
    root.destroy()

    decrytion_window = Tk()
    decrytion_window.geometry("500x620")

    decryption_tex_data = Text(decrytion_window,height=20, width=72)
    decryyption_text_data.place(relx=0.5,rely=0.35, anchor=CENTER)


    btn_open_file = Button(decryption_window, text="Choose File..",font = 'Arial Black')
    btn_open_file.place(relx-0.5,rely=0.8, anchor=CENTER)

    decrytion_window.mainloop()

def startEncrytion():
    global file_name_entry
    global encryption_text_data
    root.destory()

    file_name_label = Label(encryption_window, text="File Name: " , font = 'arial 13')
    file_name_entry.place(relx=0.75,rely=0.55,anchor=CENTER)

    encryption_window.mainloop()


heading_label = Label(root, text="Encryption & Decryption" , font = 'arial 13')
heading_label.place(relx=0.3,rely=0.6, anchor=CENTER)

btn_start_encrytion = Button(root, text="Start Encryption" , font = 'arial 13')
btn_start_encryption.place(relx=0.7,rely=0.6,anchor=CENTER)

btn_start_decryption = Button(root, text="Start Decryption" , font = 'arial 13')
btn_start_decryption.place(relx=0.7,rely=0.6,anchor=CENTER)

root.mainloop()
