#import modules
from tkinter import *
import os
import folder_gui as fg
import time
import ctypes
import gui_pack as gp

# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.configure(background = "black")
    main_screen.geometry("350x300")
    main_screen.title("Account Login")
    Label(text="HAWK watches you!", bg="blue", width="300", height="2").pack()

    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global password_login_entry
    Label(main_screen, text="Password *").pack()
    password_login_entry = Entry(main_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(main_screen, text="").pack()
    Button(main_screen, text="AUTHENTICATE", width=15, height=1, command = check_password).pack()
    
    main_screen.mainloop()


    
def list_users(text):
    cur_dir = os.getcwd() + '\\User_faces'
    names = [f for f in os.listdir(cur_dir) if os.path.isfile(os.path.join(cur_dir, f))]
    for name in len(names):
        names[name] = name.split(".")[0]
    


# Implementing event on login button 

def check_password():
    file = "pass"
    check_password.pass_attempts
    password1 = password_verify.get()
    password_login_entry.delete(0, END)
    msg = Label(main_screen, text="")
    list_of_files = os.listdir()
    if file in list_of_files:
        file1 = open(file, "r")
        verify = file1.read().splitlines()
        if password1 == 'k':
            main_screen.destroy()
            gp.gui()
            
    check_password.pass_attempts += 1
    if check_password.pass_attempts == 3:
        Label(main_screen, text='Unauthorized login attempt')
        time.sleep(3.0)
        main_screen.destroy()
        ctypes.windll.user32.LockWorkStation()
    else:
        msg.configure(text='Try again. Attempt %i/3' % (check_password.pass_attempts + 1))
        msg.pack()
        
        
check_password.pass_attempts = 0
main_account_screen()