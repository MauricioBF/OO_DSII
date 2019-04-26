from autor import Autor
from trabalho import Trabalho
from autorDAO import autor_DAO
from trabalhoDAO import trabalho_DAO
from funcoes 
import psycopg2
import datetime

autorDAO = Autor_DAO()
trabalhoDAO = Trabalho_DAO()

print("DAOs inicioados\n\n")


print("Autores:\n")
autorlist(autorDAO.dolist())

print("Trabalhos:\n")
trabalholist(trabalhoDAO.dolist())


autor1 = Autor("Mauricio", "mauricio@gmail.com")
autor2 = Autor("Lucas", "lucas@gmail.com")

trabalho1 = Trabalho("teste de matematica", 2, "matematica")
trabalho2 = Trabalho("teste de portugues", 2, "portugues")
trabalho3 = Trabalho("teste de quimica", 2, "quimica")
trabalho4 = Trabalho("teste de biologia", 2, "biologia")

autorDAO.save(autor1)
autorDAO.save(autor2)

trabalhoDAO.save(trabalho1)
trabalhoDAO.save(trabalho2)
trabalhoDAO.save(trabalho3)
trabalhoDAO.save(trabalho4)

print("2 autores e 4 trabalhos iniciados e salvos\n\n")

print("Autores:\n")
autorlist(autorDAO.dolist())

print("Trabalhos:\n")
trabalholist(trabalhoDAO.dolist())


autor1 = autorDAO.dolist()[0]
autor2 = autorDAO.dolist()[1]

trabalho1 = trabalhoDAO.dolist()[0]
trabalho2 = trabalhoDAO.dolist()[1]
trabalho3 = trabalhoDAO.dolist()[2]
trabalho4 = trabalhoDAO.dolist()[3]

autor1.email = "m@gmail.com"
autor2.nome = "Alan"

trabalho1.titulo = "mat"
trabalho2.nota = 3
trabalho3.conteudo = "prova de quimica"
trabalho4.entregar()

trabalho1.adicionarAutor(autor1)
trabalho2.adicionarAutor(autor2)
trabalho3.adicionarAutor(autor1)
trabalho3.adicionarAutor(autor2)

autorDAO.save(autor1)
autorDAO.save(autor2)

trabalhoDAO.save(trabalho1)
trabalhoDAO.save(trabalho2)
trabalhoDAO.save(trabalho3)
trabalhoDAO.save(trabalho4)

print("2 autores e 4 trabalhos modificados\n\n")

print("Autores:\n")
autorlist(autorDAO.dolist())

print("Trabalhos:\n")
trabalholist(trabalhoDAO.dolist())


autorDAO.delete(autor1)
autorDAO.delete(autor2)

trabalhoDAO.delete(trabalho1)
trabalhoDAO.delete(trabalho2)
trabalhoDAO.delete(trabalho3)
trabalhoDAO.delete(trabalho4)

print("2 autores e 4 trabalhos deletados\n\n")

print("Autores:\n")
autorlist(autorDAO.dolist())

print("Trabalhos:\n")
trabalholist(trabalhoDAO.dolist())