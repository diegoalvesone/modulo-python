class Produto:

    def __init__(self, id: int, nome: str, preco: float, estoque: int):
        self.id      = id;
        self.nome    = nome;
        self.preco   = preco;
        self.estoque = estoque;

    def adicionar_estoque(self, quantidade: int):
        self.verificar_numero_positivo(quantidade);
        self.estoque: int = self.estoque + quantidade;

    def remover_estoque(self, quantidade):
        self.verificar_numero_positivo(quantidade);
        novo_estoque = self.estoque - quantidade;
        self.verificar_estoque_negativo(novo_estoque);
        self.estoque = self.estoque - quantidade;

    def verificar_numero_positivo(self, valor):
        if valor <= 0:
            raise Exception("O número precisa ser positivo")

    def verificar_estoque_negativo(self, valor):
        if valor < 0:
            raise Exception("O estoque precisa ser maior ou igual a 0");
