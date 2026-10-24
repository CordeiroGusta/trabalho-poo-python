# Uma escola precisa calcular médias. Crie Boletim com __aluno e __notas.
# •	Inicialize a lista de notas vazia.
# •	Implemente adicionar_nota(nota), aceitando valores de 0 a 10.
# •	Implemente calcular_media(), tratando a lista vazia.
# •	Implemente verificar_situacao(): aprovado para média >= 7; reprovado caso contrário.


class Boletim:
        def __init__(self, aluno):
        self.__aluno = aluno
        self.__notas = []

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.__notas.append(nota)
            print("Nota adicionada com sucesso!")
        else:
            print("Nota inválida! Digite um valor entre 0 e 10.")

    def calcular_media(self):
        if not self.__notas:
            return 0

        return sum(self.__notas) / len(self.__notas)

    def verificar_situacao(self):
        media = self.calcular_media()

        if media >= 7:
            return "Aprovado"
        else:
            return "Reprovado"


# Testando a classe
boletim = Boletim("Pedro")

boletim.adicionar_nota(8)
boletim.adicionar_nota(7)
boletim.adicionar_nota(9)

print("Média:", boletim.calcular_media())
print("Situação:", boletim.verificar_situacao())
