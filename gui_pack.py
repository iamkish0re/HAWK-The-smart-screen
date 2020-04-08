import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
import shutil
import folder_gui as fg
from functools import partial

LARGE_FONT= ("Verdana", 12)

password_verify = ""
def gui():
    class SeaofBTCapp(tk.Tk):
        def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)
            container = tk.Frame(self)
            container.pack(side="top", fill="both", expand = True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

            self.frames = {}
            for F in (user_page, Settings, user_details, RemoveFace, add_user_page, image_page, file_page):
                frame = F(container, self)
                self.frames[F] = frame
                frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame(user_page)

        def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()

            
    class user_page(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self,parent)
            label = tk.Label(self, text="Welcome", font=LARGE_FONT)
            label.pack(pady=10,padx=10)
            
            tk.Button(self, text="User", width=15, height=1, command=lambda: controller.show_frame(user_details)).pack()#ADD COMMAND LATER
            tk.Button(self, text="Settings", width=15, height=1, command=lambda: controller.show_frame(Settings)).pack()
            tk.Button(self, text="Quit", width=15, height=1, command= self.quit).pack()
        

    class user_details(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            cur_dir = os.getcwd() + '\\users'
            names = [f for f in os.listdir(cur_dir) if os.path.isfile(os.path.join(cur_dir, f))]
            for name in range(len(names)):
                names[name] = names[name].split(".")[0]

            T = tk.Label(self, height=2, width=30 ,text="Current Users' Faces")
            listbox = tk.Listbox(self)
            T.pack()
            for i in range(len(names)):
                listbox.insert(i+1, names[i])
            listbox.pack()
            

            button2 = tk.Button(self, text="Remove Face", width = 10 , command = lambda:controller.show_frame(RemoveFace))
            button2.pack()
            button3 = tk.Button(self, text="Add Face", width = 10 ,command =lambda: controller.show_frame(add_user_page))
            button3.pack()
            button4 = tk.Button(self, text="Back", width = 10, command = lambda: controller.show_frame(user_page) )
            button4.pack()

    class Settings(tk.Frame):
        
        def save_flag(self):
                flag = os.getcwd() + '\\flag.txt'
                f = open(flag, 'w+')
                f.write(str(self.BRIGHTFLAG.get()) + "\n")
                f.write(str(self.LOCKFLAG.get()) + "\n")
                f.write(str(self.PRIVACYFLAG.get()) + "\n")
                f.close()
                self.quit
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.BRIGHTFLAG = tk.BooleanVar()
            self.PRIVACYFLAG = tk.BooleanVar()
            self.LOCKFLAG = tk.BooleanVar()
            self.BRIGHTFLAG.set(False)
            self.PRIVACYFLAG.set(False)
            self.LOCKFLAG.set(False)
            

            tk.Label(self, text="Select ...").pack(pady=10,padx=10) #grid(row=0, sticky=tk.W)

            brig = tk.Checkbutton(self, text="Brightness", variable= self.BRIGHTFLAG).pack() #grid(row=3, sticky=tk.W)
            pri = tk.Checkbutton(self, text="Privacy Protection", variable= self.PRIVACYFLAG).pack() #grid(row=4, sticky=tk.W)
            loc = tk.Checkbutton(self, text="Auto Lock", variable=self.LOCKFLAG).pack() #grid(row=5, sticky=tk.W)

            button0 = tk.Button(self, text="Back",width = 10, command= lambda: controller.show_frame(user_page))
            button0.pack()

            button1 = tk.Button(self, text="OK", width = 10, command=self.save_flag)
            button1.pack()

    class RemoveFace(tk.Frame):
        
        def delete_user(self):
            #str = self.text.get(1.0, 'end-1c')
            uname = text.get()
            dir = os.getcwd() 
                
            file = dir + "\\users\\" + uname + ".jpg"
            if os.path.exists(file):
                os.remove(file)
                messagebox.showinfo('Success!', 'User Removed!')
            else:
                messagebox.showerror('Error!', 'File not found!')
                #tk.Label(self, text = "User not found")

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="Whom to remove?", font=LARGE_FONT)
            label.pack(pady=10,padx=10)
            self.delete_widgets(controller)

        def delete_widgets(self, controller):
            global uname, text
            uname = tk.StringVar()
            text =  tk.Entry(self)
            text.pack()
            
            button1 = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame(user_details))
            button1.pack()

            button2 = tk.Button(self, text="OK",
                               command=self.delete_user)

            button2.pack()

    class add_user_page(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self,parent)
            label = tk.Label(self, text="Enter Name", font=LARGE_FONT)
            label.pack(pady=10,padx=10)
            tk.Label(self,text = "Your name please!")
            self.labe_create(controller)
        def labe_create(self, controller):
            global name, lab
            name = tk.StringVar()
            lab = tk.Entry(self)
            lab.pack()
            
            
            tk.Button(self, text="Take Picture", width=15, height=1 , command = lambda:controller.show_frame(image_page)).pack()#ADD COMMAND LATER
            tk.Button(self, text="Choose file", width=15, height=1, command = fg.fg).pack()
            tk.Button(self, text="Back", width=15, height=1, command= lambda: controller.show_frame(user_details)).pack()
    
    class file_page(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self,parent)

            tk.Label(self,text = "Choose a pic")
            tk.Button(self, text="OK", command = lambda:controller.show_frame(user_details)).pack

        
    class image_page(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self,parent)
            tk.Label(self,text = "Say cheese!!!")
            tk.Button(self, text="Back", command = lambda:controller.show_frame(user_details)).pack
            
            '''self.snapshot()    
        
        def snapshot(self):
            
            path = os.getcwd() + "\\users"
            filename = newname + ".jpg"
            while newname == " ":
                camera = cv2.VideoCapture(0)
                return_value,image = camera.read()
                gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
                cv2.imshow('image',gray)
                if cv2.waitKey(1)& 0xFF == ord('s'):
                      cv2.imwrite(os.path.join(path ,filename),image)
                      break
            camera.release()
            cv2.destroyAllWindows()'''

    app = SeaofBTCapp()
    app.mainloop()

