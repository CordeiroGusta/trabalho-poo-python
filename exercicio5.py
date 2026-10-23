# 5. Sistema de biblioteca
# Uma biblioteca precisa controlar empréstimos. Crie Livro com __titulo, __autor e __disponivel.
#•	Implemente emprestar() e devolver().
#•	Impeça emprestar um livro já emprestado.
#•	Impeça devolver um livro já disponível, informando a situação.
#•	Crie uma propriedade para consultar a disponibilidade.


class Livro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponivel = True

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def disponivel(self):
        return self.__disponivel

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            print(f'O livro "{self.__titulo}" foi emprestado.')
        else:
            print(f'O livro "{self.__titulo}" já está emprestado.')

    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
            print(f'O livro "{self.__titulo}" foi devolvido.')
        else:
            print(f'O livro "{self.__titulo}" já está disponível.')


# Testes
livro1 = Livro("Dom Casmurro", "Machado de Assis")

print("Disponível:", livro1.disponivel)

livro1.emprestar()
print("Disponível:", livro1.disponivel)

livro1.emprestar()  # Tenta emprestar novamente

livro1.devolver()
print("Disponível:", livro1.disponivel)

livro1.devolver()  # Tenta devolver novamente
