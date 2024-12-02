class BorrowableMixin:
    def __init__(self):
        self.is_borrowed = False

    def emprestar(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return f"'{self.titulo}' foi emprestado com sucesso!"
        return f"'{self.titulo}' já está emprestado!"

    def devolver(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return f"'{self.titulo}' foi devolvido com sucesso!"
        return f"'{self.titulo}' não estava emprestado!"
    
