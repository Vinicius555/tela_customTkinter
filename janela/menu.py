import customtkinter
from login import login
from register import cadastro
from center_window import MyWindow
from load_image import load_image

def run_login():
    janela_menu.destroy()
    login()
    

def run_cadastro():
    janela_menu.destroy()
    cadastro()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela_menu = MyWindow()
janela_menu.center_window(600, 400)

load_image(janela_menu, "img\pokemon.jpg", (600, 400))

button_login = customtkinter.CTkButton(
    janela_menu, text="Login", command=lambda: run_login(), border_width=1, fg_color="transparent", corner_radius=2)
button_login.place(x=220, y=250)

button_cadastro = customtkinter.CTkButton(
    janela_menu, text="Register", command=lambda: run_cadastro(), border_width=1, fg_color="transparent", corner_radius=2)
button_cadastro.place(x=220, y=290)

janela_menu.resizable(False, False)
janela_menu.mainloop()
