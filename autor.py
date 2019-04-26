class Autor():
    def __init__  (self, nome, email):
        self._nome = nome
        self._email = email
    
    def get_nome(self):
        return self._nome
    def set_nome(self, nome):
        self._nome = nome

    def get_email(self):
        return self._email
    def set_email(self, email):
        self._email = email

    def get_codigo(self):
        return self._codigo
    def set_codigo(self, codigo):
        self._codigo = codigo

    nome = property(get_nome, set_nome)
    email = property(get_email, set_email)
    codigo = property(get_codigo, set_codigo)