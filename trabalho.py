#precisamos check da data atualização
#dataAtualização é a mesma que data de quando "puxou os dados"
from datetime import datetime
class Trabalho():
    def __init__ (self, conteudo, nota, titulo):
        self._conteudo = conteudo
        self._nota = nota
        self._titulo = titulo
        self._dataAtualiza = datetime.now()
    
    def get_conteudo(self):
        return self._conteudo
    def set_conteudo(self, conteudo):
        self._conteudo = conteudo
    
    def get_nota(self):
        return self._nota
    def set_nota(self, nota):
        self._nota = nota

    def get_titulo(self):
        return self._titulo
    def set_titulo(self, titulo):
        self._titulo = titulo
    
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
    
    conteudo = property(get_conteudo, set_conteudo)
    nota = property(get_nota, set_nota)
    titulo = property(get_titulo, set_titulo)