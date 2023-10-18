import customtkinter
import os
from PIL import Image


def load_image(janela, imagem_path, size):
    try:
        diretorio_atual = os.path.dirname(__file__)
        caminho_imagem = os.path.join(diretorio_atual,imagem_path)
        image = Image.open(caminho_imagem)
        my_image = customtkinter.CTkImage(dark_image=image, size=size)

        if my_image:
            image_label = customtkinter.CTkLabel(
                janela, image=my_image, text="")
            image_label.pack()
        else:
            print("Error ao carregar a imagem.")
    except Exception as err:
        print(f"Error ao carregar imagem de login: {err}")
