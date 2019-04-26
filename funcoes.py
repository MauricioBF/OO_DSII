def autorlist(array):
    for e in array:
        print("------")
        if hasattr(e, 'cod'):
            print("Codigo: "+str(e.cod))
        else:
            print("Codigo: Não Definido")
        print("Nome: "+e.nome)
        print("Email: "+e.email)
        print("Trabalhos: ")
        for line in e.trabalho:
            print("   "+line.titulo)
        print("------\n")
def trabalholist(array):
    for e in array:
        print("------")
        if hasattr(e, 'cod'):
            print("Codigo: "+str(e.cod))
        else:
            print("Codigo: Não Definido")
        print("Tiulo: "+e.titulo)
        print("Nota: "+str(e.nota))
        print("Conteudo: "+e.conteudo)
        if hasattr(e, 'dataEntrega'):
            print("Data de Entrega: "+str(e.dataEntrega))
        else:
            print("Data de Entrega: Não entregue")
        print("Autores: ")
        for line in e.autor:
            print("   "+line.nome)
        print("------\n\n")