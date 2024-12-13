class EntradaInvalidaException(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem
        super().__init__(self.mensagem)
        
class CampoNumericoException(EntradaInvalidaException):
    """Exceção para quando um campo que deve ser numérico recebe um valor não numérico"""
    def __init__(self, mensagem="Este campo só aceita números"):
        self.mensagem = mensagem
        super().__init__(self.mensagem)
        
class CampoTextoException(EntradaInvalidaException):
    """Exceção para quando um campo que deve ser textual recebe um valor não textual"""
    def __init__(self, mensagem="Este campo só aceita texto"):
        self.mensagem = mensagem
        super().__init__(self.mensagem)