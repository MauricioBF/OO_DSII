from datetime import datetime

class Trabalho():
    def __init__ (self, conteudo, nota, titulo):
        self._conteudo = conteudo
        self._nota = nota
        self._titulo = titulo
        self._dataAtualiza = datetime.now()
        self._futuroAutor = []
    
    def get_conteudo(self):
        return self._conteudo
    def set_conteudo(self, conteudo):
        self._conteudo = conteudo
    
    def get_nota(self):
        return self._nota
    def set_nota(self, nota):
        if nota > 0 and nota < 4:
            self._nota = nota
        else:
            raise ValueError

    def get_titulo(self):
        return self._titulo
    def set_titulo(self, titulo):
        self._titulo = titulo

    def get_autor(self):
        return self._autor
    def set_autor(self, autor):
        self._autor = autor

    def get_futuroAutor(self):
        return self._futuroAutor
    def set_futuroAutor(self, futuroAutor):
        self._futuroAutor = futuroAutor
    
    def get_dataAtualiza(self):
        return self._dataAtualiza
    def set_dataAtualiza(self, dataAtualiza):
        self._dataAtualiza = dataAtualiza

    def get_dataEntrega(self):
        return self._dataEntrega
    def set_dataEntrega(self, dataEntrega):
        self._dataEntrega = dataEntrega

    def get_codigo(self):
        return self._codigo
    def set_codigo(self, codigo):
        self._codigo = codigo

    def entregar(self):
        self._dataEntrega = datetime.datetime.now()

    def adicionarAutor(self, obj):
        self._futuroAutor.append(obj)
    
    conteudo = property(get_conteudo, set_conteudo)
    nota = property(get_nota, set_nota)
    titulo = property(get_titulo, set_titulo)
    autor = property(get_autor, set_autor)
    dataEntrega = property(get_dataEntrega, set_dataEntrega)
    dataAtualiza = property(get_dataAtualiza, set_dataAtualiza)
    codigo = property(get_codigo, set_codigo)