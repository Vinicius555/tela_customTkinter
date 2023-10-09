import customtkinter
from func_login import LogIn
from center_window import MyWindow


def login():
    from welcome import welcome
    from cadastro import cadastro
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    janela_login = MyWindow()
    janela_login.center_window(500, 400)

    texto = customtkinter.CTkLabel(janela_login, text="Hello,Friend!")
    texto.pack(padx=50, pady=50)

    email_entry = customtkinter.CTkEntry(
        janela_login, placeholder_text="Email")
    email_entry.pack(padx=10, pady=10)

    password_entry = customtkinter.CTkEntry(
        janela_login, placeholder_text="Passwod", show="*")
    password_entry.pack(padx=10, pady=10)

    def login():
        email = email_entry.get()
        password = password_entry.get()
        result = LogIn.login(
            email, password
        )
        if not email or not password:
            error_label.configure(text="Por favor, preencha todos os campos.")
            return
        if result:
            janela_login.destroy()
            welcome()

        else:
            error_label.configure(text=result)

    login = customtkinter.CTkButton(janela_login, text="Enter", command=login)
    login.pack(padx=10, pady=10)

    def close_login():
        janela_login.destroy()
        cadastro()
    register = customtkinter.CTkButton(
        janela_login, text="Register", command=close_login)
    register.pack(padx=10, pady=10)

    error_label = customtkinter.CTkLabel(
        janela_login, text="", text_color="red")
    error_label.pack(padx=10, pady=10)

    janela_login.resizable(False, False)
    janela_login.mainloop()
