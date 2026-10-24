class Estoque:
    def __init__(self, produto: str, quantidade: int) -> None:
        if quantidade < 0:
            raise ValueError("A quantidade inicial não pode ser negativa!")

        self.__produto = produto
        self.__quantidade = quantidade
        self.__historico = []

        self.__historico.append(
            f"Estoque inicial: {quantidade} unidades"
        )

    @property
    def produto(self) -> str:
        return self.__produto

    @property
    def quantidade(self) -> int:
        return self.__quantidade

    def adicionar_estoque(self, quantidade: int) -> None:
        if quantidade <= 0:
            raise ValueError("A entrada deve ser maior que zero!")

        self.__quantidade += quantidade
        self.__historico.append(
            f"Entrada: +{quantidade} unidades"
        )

    def remover_estoque(self, quantidade: int) -> None:
        if quantidade <= 0:
            raise ValueError("A saída deve ser maior que zero!")

        if quantidade > self.__quantidade:
            raise ValueError("Estoque insuficiente!")

        self.__quantidade -= quantidade
        self.__historico.append(
            f"Saída: -{quantidade} unidades"
        )

    def consultar_historico(self) -> tuple:
        return tuple(self.__historico)


estoque = Estoque("Teclado", 20)

estoque.adicionar_estoque(10)
estoque.remover_estoque(5)

# Consulta
print(f"Produto: {estoque.produto}")
print(f"Quantidade atual: {estoque.quantidade}")

print("\nHistórico de movimentações:")
for movimentacao in estoque.consultar_historico():
    print(movimentacao)
