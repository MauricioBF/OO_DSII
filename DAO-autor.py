from serverDAO import serverDao
from autor import Autor
import psycopg2 

class autor_DAO(serverDao):
    def connect(self):
        super().connect()
    
    def save(self, autor):
        if autor.codigo:
            autor_DAO.(autor)
        else:
            autor_DAO.inserir(autor)

    def search(self, codigo):
        with connect(self.bd) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM "Autor" WHERE cod=%s',[codigo])
            for linha in cur.fetchall():
                autor = Autor(linha[1],linha[2])
                autor.codigo = linha[0]
                conn.commit()
                cur.close()
            return autor

    def dolist(self):
        with connect(self.bd) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM "Autor"')
            lista = []
            for linha in cur.fetchall():
                autor = Autor(linha[1],linha[2])
                autor.codigo = linha[0]
                lista.append(autor)
                conn.commit()
                cur.close()
            return lista

    def insert(self,autor):
        with connect(self.bd) as conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO "Autor" (nome, email) VALUES (%s,%s) RETURNING cod',[autor.nome,autor.email])
            linhaid = cur.fetchone()[0]
            autor.codigo = linhaid
            conn.commit()
            cur.close()
        
    def delete(self,cod):
        with connect(self.bd) as conn:
            cur = conn.cursor()
            cur.execute('DELETE FROM "Autor" WHERE cod = %s',[codigo])
            conn.commit()
            cur.close()

    def update(self,autor):
        with connect(self.bd) as conn:
            cur = conn.cursor()
            cur.execute('UPDATE "Autor" SET nome = %s,email = %s WHERE cod = %s',[autor.nome,autor.email,autor.codigo])
            conn.commit()
            cur.close()