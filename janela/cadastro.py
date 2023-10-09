import customtkinter
from func_cadastro import CreateRegister
from center_window import MyWindow


def cadastro():
    from login import login

    janela_cadastro = MyWindow()
    janela_cadastro.center_window(500, 400)

    text = customtkinter.CTkLabel(janela_cadastro, text="Welcome Friend!")
    text.pack(padx=20, pady=20)

    name_entry = customtkinter.CTkEntry(
        janela_cadastro, placeholder_text="Name")
    name_entry.pack(padx=10, pady=10)

    email_entry = customtkinter.CTkEntry(
        janela_cadastro, placeholder_text="Email")
    email_entry.pack(padx=10, pady=10)

    password_entry = customtkinter.CTkEntry(
        janela_cadastro, placeholder_text="Password", show="*")
    password_entry.pack(padx=10, pady=10)

    confirm_password_entry = customtkinter.CTkEntry(
        janela_cadastro, placeholder_text="Confirm Password", show="*")
    confirm_password_entry.pack(padx=10, pady=10)

    error_label = customtkinter.CTkLabel(
        janela_cadastro, text="", text_color="red")
    error_label.pack(padx=1, pady=1)

    def register_clicked():
        name = name_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()
        result, error_message = CreateRegister.create_register(
            name, email, password, confirm_password)

        if result:
            janela_cadastro.destroy()
            login()
        else:
            error_label.configure(text=error_message)

    button = customtkinter.CTkButton(
        janela_cadastro, text="Register", command=register_clicked)
    button.pack(padx=10, pady=10)

    def close_register():
        janela_cadastro.destroy()
        login()
    button_login = customtkinter.CTkButton(
        janela_cadastro, text="Login", command=close_register)
    button_login.pack(padx=10, pady=10)

    janela_cadastro.resizable(False, False)
    janela_cadastro.mainloop()
