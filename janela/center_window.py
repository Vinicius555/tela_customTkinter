import customtkinter as ctk


class MyWindow(ctk.CTk):

    def __init__(self, master=None):
        super().__init__(master)
        self.title("Janela Fixa Centralizada")

        self.resizable(False, False)

        self.center_window(600, 300)

    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry(f'{width}x{height}+{x}+{y}')


if __name__ == "__main__":
    app = MyWindow()
    app.mainloop()
