class products:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco

    def gtet_id(self):
        return self.id
    
    def get_nome(self):
        return self.nome 
     
    def get_preco(self):
        return self.preco
    
    def set_nome(self, nome):
        self.nome = nome
    
    def set_preco(self, preco):
        self.preco = preco

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Preço: {self.preco:.2f}"
    