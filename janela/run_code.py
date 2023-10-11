import customtkinter
from login import login
from register import cadastro
from center_window import MyWindow
from load_image import load_image


def run_login():
    janela_tela.destroy()
    login()


def run_cadastro():
    janela_tela.destroy()
    cadastro()


janela_tela = MyWindow()
janela_tela.center_window(600, 400)

load_image(janela_tela, "janela\img\pokemon.jpg", (600, 400))

button_login = customtkinter.CTkButton(
    janela_tela, text="Login", command=run_login, border_width=1, fg_color="transparent", corner_radius=2)
button_login.place(x=220, y=250)

button_cadastro = customtkinter.CTkButton(
    janela_tela, text="Register", command=run_cadastro, border_width=1, fg_color="transparent", corner_radius=2)
button_cadastro.place(x=220, y=290)

janela_tela.resizable(False, False)
janela_tela.mainloop()
