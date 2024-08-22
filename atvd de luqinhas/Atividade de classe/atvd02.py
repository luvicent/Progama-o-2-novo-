class Livro():
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
    def exibir_detalhes(self):
        print(f"Nome do livro: {self.titulo}\nAutor do livro: {self.autor}\nAno de publicação: {self.ano_publicacao}")



livro = Livro('lucas', 'Jorgeword', '10 dezembro 2004')
livro.exibir_detalhes()