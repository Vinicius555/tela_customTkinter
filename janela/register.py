import customtkinter
from func_cadastro import CreateRegister
from center_window import MyWindow
from load_image import load_image


def cadastro():
    from login import login

    janela_cadastro = MyWindow()
    janela_cadastro.center_window(500, 400)

    load_image(janela_cadastro, "janela/img/register.jpg", (500, 400))

    name_entry = customtkinter.CTkEntry(
        janela_cadastro, placeholder_text="Name", corner_radius=2, fg_color="transparent")
    name_entry.place(x=180, y=100)

    email_entry = customtkinter.CTkEntry(
        janela_cadastro, placeholder_text="Email", corner_radius=2, fg_color="transparent")
    email_entry.place(x=180, y=140)

    password_entry = customtkinter.CTkEntry(
        janela_cadastro, placeholder_text="Password", show="*", corner_radius=2, fg_color="transparent")
    password_entry.place(x=180, y=180)

    confirm_password_entry = customtkinter.CTkEntry(
        janela_cadastro, placeholder_text="Confirm Password", show="*", corner_radius=2, fg_color="transparent")
    confirm_password_entry.place(x=180, y=220)

    error_label = customtkinter.CTkLabel(
        janela_cadastro, text="", text_color="red", corner_radius=2)
    error_label.pack(padx=10, pady=10)

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
            error_label.place(x=180, y=50)

    button = customtkinter.CTkButton(
        janela_cadastro, text="Register", command=register_clicked, corner_radius=2, fg_color="green")
    button.place(x=180, y=280)

    def close_register():
        janela_cadastro.destroy()
        login()
    button_login = customtkinter.CTkButton(
        janela_cadastro, text="Login", command=close_register, corner_radius=2)
    button_login.place(x=180, y=320)

    janela_cadastro.resizable(False, False)
    janela_cadastro.mainloop()


cadastro()
