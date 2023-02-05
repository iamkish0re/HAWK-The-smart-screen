import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Home Page")
        self.label.pack(pady=10)

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
        self.label.pack(pady=10)

class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("HAWK")
        self.geometry('800x400')
        # Menu Bar
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        # File Menu
        file_menu = tk.Menu(menu_bar)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Home", command=lambda: self.show_frame(HomePage))
        file_menu.add_command(label="Settings", command=lambda: self.show_frame(SettingsPage))
        file_menu.add_command(label="Register", command=lambda: self.show_frame(RegisterPage))
        file_menu.add_command(label="Login", command=lambda: self.show_frame(LoginPage))

        menu_bar.add_cascade(label="Exit", command=self.quit)

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
