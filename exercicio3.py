# 3 Controle de produtos.
# Uma loja precisa controlar preços e quantidades. Crie a classe Produto com __nome, __preco e __quantidade.
# •	Implemente getters ou propriedades para consultar os dados.
# •	Crie setters com validação para preço e quantidade não negativos.
# •	Implemente valor_total_estoque().
# •	Teste uma atualização válida e uma inválida.

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    @property
    def preco(self):
        return self.__preco

    @property
    def nome(self):
        return self.__nome

    @property
    def quantidade(self):
        return self.__quantidade

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco
        else:
            print("Erro: o preço não pode ser negativo!")

    @quantidade.setter
    def quantidade(self, nova_quantidade):
        if nova_quantidade >= 0:
            self.__quantidade = nova_quantidade
        else:
            print("Erro: a quantidade não pode ser negativa!")

    def valor_total_estoque(self):
        return self.__preco * self.__quantidade


# Criando um produto
produto = Produto("Teclado", 100, 5)

# Consultando os dados
print(produto.nome)
print(produto.preco)
print(produto.quantidade)

# Calculando o valor do estoque
print(produto.valor_total_estoque())

# Atualização válida
produto.preco = 120
print(produto.preco)

# Atualização inválida
produto.preco = -50
print(produto.preco)
