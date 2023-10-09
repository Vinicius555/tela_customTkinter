import customtkinter
from login import login
from cadastro import cadastro
from PIL import Image


janela_tela = customtkinter.CTk()
janela_tela.geometry("500x400")

minha_imagem = customtkinter.CTkImage(dark_image=Image.open(".\img\pokemon.jpg"),
                                      size=(600, 400))
image_label = customtkinter.CTkLabel(
    janela_tela, image=minha_imagem, text="")
image_label.pack()

button_login = customtkinter.CTkButton(
    janela_tela, text="Login", command=lambda: login(), border_width=1, fg_color="transparent")
button_login.place(x=195, y=250)

button_cadastro = customtkinter.CTkButton(
    janela_tela, text="Register", command=lambda: cadastro(), border_width=1, fg_color="transparent")
button_cadastro.place(x=195, y=290)


janela_tela.resizable(False, False)
janela_tela.mainloop()
