import PySimpleGUI as sg 
from pathlib import Path
import configparser

def main_window():
    menu_def = [["File", ["Setting", "Theme", "---", "Exit"]],
                ["Help", ["About"]]]
    layout = [
        [sg.MenubarCustom(menu_def, tearoff=False)],
        [sg.Text("Authentication Needed!")],
        [
            sg.Text("Username :", s=16, justification='center'),
            sg.Input(key="-USERNAME-",s=25)],
        [
            sg.Text("Password :", s=16, justification='center'),
            sg.Input(key="-PASSWORD-", s=25)],
        [sg.Button("Authenticate")],
        [sg.Text("Hawk watches you!", justification='center')]
    ]
    title = settings["GUI"]["title"]
    window = sg.Window(title, layout, use_custom_titlebar=True, element_padding=10)

    while True:
        event, values = window.read()
        print(event, values)
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break
        if event == "About":
            sg.popup(title, "Version 1.0",
                     "Hawk, all in one secure space!", grab_anywhere=True)
        elif event == "Authenticate":
            sg.popup_no_titlebar("UNDER DEVELOPMENT!")
        
    window.close()

if __name__ == "__main__":
    CONFIG_PATH = Path.cwd()
    config = configparser.ConfigParser()
    # CHECKS IF CONFIG.INI IS PRESENT, IF NOT CREATES IT WITH DEFAULT SETTINGS!
    if not Path(CONFIG_PATH / 'config.ini').exists():
        config['GUI'] = {'title': 'Hawk', 'font_size': 10, 'font_family': 'consolas'}
        config.write(open('config.ini', 'w'))
            
    settings = sg.UserSettings(
        path=CONFIG_PATH, filename='config.ini', use_config_file=True, convert_bools_and_none=True
    )
    font_family = settings["GUI"]["font_family"]
    font_size = int(settings["GUI"]["font_size"])

    sg.set_options(font=(font_family, font_size))
    main_window()