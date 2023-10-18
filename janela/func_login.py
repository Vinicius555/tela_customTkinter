from conexao import curso, error
import hashlib

class Login():
    def __init__(self, email, password):
        self.email = email
        self.password = password


class LogIn:
    @staticmethod
    def login(email, password):
        try:
            curso.execute("SELECT * FROM usuarios WHERE email=?", (email,))
            result = curso.fetchone()

            if result:
                stored_password = result[2]
                sha256 = hashlib.sha256()
                password_bytes = password.encode('utf-8')
                sha256.update(password_bytes)
                hashed_password = sha256.hexdigest()

                if hashed_password == stored_password:
                    print("Login efetuado")
                    return True, None
                else:
                    print("Falha no login")
                    return False, "Senha incorreta"
            else:
                print("Falha no login")
                return False, "Email não encontrado"
        except error as er:
            print(f"Falha ao realizar o login: {er}")
