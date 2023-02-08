import tkinter as tk
from tkinter import messagebox
import credentials as cr

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Home Page")
        self.label.pack(pady=10)
        print("HOME PAGE")

class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Settings Page")
        self.label.pack(pady=10)

class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Register Page")
        self.label.pack(pady=10)

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Login Page")
        self.label.pack()
        self.loginMessage = ""
        self.create_widgets()

    def create_widgets(self):
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self, text="Login", command= lambda: self.verify(self.menu_bar))
        self.login_button.pack()

    def verify(self):
                
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()
        user  = cr.check_user(entered_username, entered_password)
        print(user)
        if len(user) == 1:
            self.controller.show_frame(HomePage)
            messagebox.showinfo("Login Successful", "Welcome " + user[0]['name'], )
            file_menu = tk.Menu(menu_bar)
            menu_bar.add_cascade(label="File", menu=file_menu)
            file_menu.add_command(label="Home", command=lambda: self.controller.show_frame(HomePage))
            file_menu.add_command(label="Settings", command=lambda: self.controller.show_frame(SettingsPage))
            file_menu.add_command(label="Logout", command=lambda: self.controller.show_frame(LoginPage))

            menu_bar.add_cascade(label="Exit", command=self.quit)
            return
        else:
            messagebox.showerror("Login Failed", "Wrong username or password")


class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("HAWK")
        self.geometry('800x400')
        # Menu Bar
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        # File Menu
        file_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        file_menu.add_command(label="Register", command=lambda: self.show_frame(RegisterPage))

        self.menu_bar.add_cascade(label="Exit", command=self.quit)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in [HomePage, SettingsPage, RegisterPage, LoginPage]:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
