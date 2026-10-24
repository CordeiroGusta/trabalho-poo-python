# 9. Sistema de autenticação
# Uma aplicação precisa autenticar usuários. Crie Usuario com __login e __senha.
# •	Implemente autenticar(login, senha).
# •	Implemente alterar_senha(senha_atual, nova_senha).
# •	Exija a senha atual correta e nova senha com pelo menos oito caracteres.
# •	Não implemente getter para a senha.


class Usuario:
    def __init__(self, login, senha):
        if len(senha) < 8:
            raise ValueError("A senha deve ter pelo menos 8 caracteres.")

        self.__login = login
        self.__senha = senha

    def autenticar(self, login, senha):
        return self.__login == login and self.__senha == senha

    def alterar_senha(self, senha_atual, nova_senha):
        if senha_atual != self.__senha:
            print("Senha atual incorreta.")
            return

        if len(nova_senha) < 8:
            print("A nova senha deve ter pelo menos 8 caracteres.")
            return

        self.__senha = nova_senha
        print("Senha alterada com sucesso!")


# Testes
usuario = Usuario("pedro", "senha123")

print(usuario.autenticar("pedro", "senha123"))
print(usuario.autenticar("pedro", "errada"))

usuario.alterar_senha("senha123", "novasenha")
print(usuario.autenticar("pedro", "novasenha"))

usuario.alterar_senha("errada", "outrasenha")
usuario.alterar_senha("novasenha", "123")
