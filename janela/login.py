import customtkinter
from func_login import LogIn
from center_window import MyWindow
from load_image import load_image


def login():
    from welcome import welcome
    from register import cadastro
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    janela_login = MyWindow()
    janela_login.center_window(500, 400)

    load_image(janela_login, "janela/img/login.jpg", (500, 400))

    email_entry = customtkinter.CTkEntry(
        janela_login, placeholder_text="Email", fg_color="transparent", corner_radius=2)
    email_entry.place(x=190, y=150)

    password_entry = customtkinter.CTkEntry(
        janela_login, placeholder_text="Passwod", show="*", corner_radius=2, fg_color="transparent")
    password_entry.place(x=190, y=190)

    def login():
        email = email_entry.get()
        password = password_entry.get()
        result = LogIn.login(
            email, password
        )
        if not email or not password:
            error_label.configure(text="Por favor, preencha todos os campos.")
            error_label.place(x=180, y=100)
            return
        if result:
            janela_login.destroy()
            welcome()

        else:
            error_label.configure(text=result)

    login = customtkinter.CTkButton(
        janela_login, text="Enter", command=login, corner_radius=2, fg_color="green")
    login.place(x=190, y=240)

    def close_login():
        janela_login.destroy()
        cadastro()
    register = customtkinter.CTkButton(
        janela_login, text="Register", command=close_login, corner_radius=2)
    register.place(x=190, y=280)

    error_label = customtkinter.CTkLabel(
        janela_login, text="", text_color="red")
    error_label.pack(padx=10, pady=10)

    janela_login.resizable(False, False)
    janela_login.mainloop()
