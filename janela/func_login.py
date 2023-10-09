from conexao import conn, curso, error


class Login():
    def __init__(self, email, password):
        self.email = email
        self.password = password


class LogIn:
    @staticmethod
    def login(email, password):
        try:
            curso.execute(
                f"SELECT * FROM usuarios WHERE email=? AND password=?", (email, password))
            result = curso.fetchone()
            if result:
                print("Login efetuado")
                return True, None
            else:
                print("Fail")
                return False, ("email inválido!")
        except error as er:
            print(f"Falha ao realizar o login Error:{er}")
