# 1. Conta bancária
# Um banco precisa garantir que seus clientes não alterem diretamente o saldo. Crie a classe ContaBancaria com __titular e __saldo.
# •	Inicialize os atributos no construtor e rejeite saldo inicial negativo.
# •	Implemente depositar(valor) e sacar(valor).
# •	Impeça depósitos não positivos e saques maiores que o saldo.
# •	Crie uma propriedade somente leitura para consultar o saldo.
# •	Teste depósitos, saques e operações inválidas.


class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        if saldo_inicial < 0:
            raise ValueError("O saldo inicial não pode ser negativo!")

        self.__titular = titular
        self.__saldo = saldo_inicial

    @property
    def saldo(self):
        return self.__saldo


#=============================DEPÓSITO E SAQUE==================================

    # Função que bloqueia depósitos não positivos.
    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Depósito deve ser positivo")

        self.__saldo = self.__saldo + valor

    # Função que bloqueia saques inválidos ou maiores que o saldo.
    def sacar(self, valor):
        if valor <= 0 or valor > self.__saldo:
            raise ValueError("Saque inválido")

        self.__saldo = self.__saldo - valor

#===============================================================================


# Testando depósitos e saques.
conta = ContaBancaria("Pedro", 500)

print("Saldo inicial:", conta.saldo)

conta.depositar(200)
print("Saldo após depósito:", conta.saldo)

conta.sacar(100)
print("Saldo após saque:", conta.saldo)


# Testando operações inválidas.
try:
    conta.depositar(0)
except ValueError as erro:
    print("Erro:", erro)

try:
    conta.sacar(10000)
except ValueError as erro:
    print("Erro:", erro)


# Testando a propriedade somente leitura.
try:
    conta.saldo = 1000
except AttributeError as erro:
    print("Erro:", erro)


# Testando saldo inicial negativo.
try:
    conta_invalida = ContaBancaria("João", -100)
except ValueError as erro:
    print("Erro:", erro)


# Consultando o saldo final.
print("Saldo final:", conta.saldo)

