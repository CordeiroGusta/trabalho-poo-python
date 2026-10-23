'''
2. Cadastro de alunos
Uma instituição precisa proteger informações acadêmicas. Crie a classe Aluno com __nome, __matricula e __nota.
 * Inicialize os atributos no construtor. X
 * Implemente getters para consultar os dados.
 * Crie um setter para alterar a nota, aceitando apenas valores entre 0 e 10.
 * Cadastre três alunos e apresente seus dados.
Desafio: O que deve acontecer se alguém tentar registrar a nota 15?
'''

class Aluno:
    def __init__(self, nome: str, matricula: int, nota: float) -> None:
        self.__nome = nome
        self.__matricula = matricula
        self.nota = nota  # Aciona o setter e valida a nota inicial

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def matricula(self) -> int:
        return self.__matricula

    @property
    def nota(self) -> float:
        return self.__nota

    @nota.setter
    def nota(self, nova_nota: float) -> None:
        if 0 <= nova_nota <= 10:
            self.__nota = nova_nota
        else:
            raise ValueError("Digite um valor válido entre 0 e 10!")

    def consultar_aluno(self, matricula_aluno: int) -> str:
        if matricula_aluno == self.__matricula:
            return (
                f"Nome do aluno: {self.__nome}\n"
                f"Matrícula: {self.__matricula}\n"
                f"Nota: {self.__nota}"
            )
        return "Cadastro não encontrado"


fulano = Aluno("teste", 110, 9.9)

print(fulano.consultar_aluno(110))
print(fulano.nome)
print(fulano.nota)

try:
    novaNota = float(input("Digite uma nota entre 0 e 10: "))
    fulano.nota = novaNota
    print(fulano.nota)
except ValueError as erro:
    print(f"Erro: {erro}")