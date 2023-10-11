import customtkinter
import os
from PIL import Image


def load_image(janela, imagem_path, size):
    try:
        image = Image.open(imagem_path)
        my_image = customtkinter.CTkImage(dark_image=image, size=size)

        if my_image:
            image_label = customtkinter.CTkLabel(
                janela, image=my_image, text="")
            # Ajuste as coordenadas conforme necessário
            image_label.pack()
        else:
            print("Error ao carregar a imagem.")
    except Exception as err:
        print(f"Error ao carregar imagem de login: {err}")
