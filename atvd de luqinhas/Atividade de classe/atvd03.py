class Produtos:
    def __init__(self, nome, preco, quantidade, codigo):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.codigo = codigo

    def calcular_total(self):
        total = self.preco * self.quantidade
        print(f"O valor total é: R$ {total}")

    def atualizar_preco(self):
        self.preco = float(input("Qual o novo valor do produto: "))
        print(f"O novo preço do {self.nome} é R$ {self.preco}")
    
    def verificar_disponibilidade(self):
        print(f"No estoque temos {self.quantidade} de {self.nome}")

produto = Produtos("Lucas", "20", 5, "#lucasOmelhor")
produto.calcular_total()
produto.atualizar_preco()
produto.verificar_disponibilidade()