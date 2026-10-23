"""
4. Cadastro de funcionários
Uma empresa precisa controlar salários. Crie Funcionario com __nome, __cargo e __salario.
Crie métodos de consulta.
Implemente aumentar_salario(percentual).
Rejeite percentuais negativos e salário inicial negativo.
Cadastre dois funcionários e aplique aumentos diferentes.
"""


class Funcionario:
    def __init__(self, nome: str, cargo: str, salario: float) -> None:
        if salario < 0:
            raise ValueError("O salário inicial não pode ser negativo!")

        self.__nome = nome
        self.__cargo = cargo
        self.__salario = salario

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def cargo(self) -> str:
        return self.__cargo

    @property
    def salario(self) -> float:
        return self.__salario

    def aumentar_salario(self, percentual: float) -> None:
        if percentual < 0:
            raise ValueError("O percentual não pode ser negativo!")

        aumento = self.__salario * (percentual / 100)
        self.__salario += aumento

    def consultar_funcionario(self) -> str:
        return (
            f"Nome: {self.__nome}\n"
            f"Cargo: {self.__cargo}\n"
            f"Salário: R$ {self.__salario:.2f}"
        )


funcionario1 = Funcionario("Carlos", "Desenvolvedor", 3000.00)
funcionario2 = Funcionario("Marina", "Analista de Sistemas", 4000.00)

funcionario1.aumentar_salario(10)
funcionario2.aumentar_salario(5)

print(funcionario1.consultar_funcionario())
print("-" * 30)
print(funcionario2.consultar_funcionario())