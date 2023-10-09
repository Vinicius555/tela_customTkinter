import customtkinter


def welcome():
    janela_welcome = customtkinter.CTk()

    janela_welcome.geometry("600x400")

    texto = customtkinter.CTkLabel(
        janela_welcome, text="WELCOME", font=("Arial", 50))
    texto.pack(padx=10, pady=150)

    janela_welcome.resizable(False, False)

    janela_welcome.mainloop()
