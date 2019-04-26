from serverDAO import serverDao
from autor import Autor
from trabalho import Trabalho
import psycopg2 

class autor_DAO(serverDao):
    def connect(self):
        super().connect()
    
    def save(self, autor):
        if autor.codigo:
            update(autor)
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
            slist = cur.fetchall()
            query = query = 'SELECT "at"."codAutor", "t"."cod", "t"."conteudo", "t"."nota", "t"."dataEntrega", "t"."titulo" FROM "Trabalho" AS "t" INNER JOIN "TrabalhoAutor" AS "at" ON "t"."cod" = "at"."codTrabalho"'
            cur.excute(query)
            atlist = cur.fetchall()
            lista = []
            for e in slist:
                autor = Autor(e[1], e[2])
                autor.cod = e[0]
                tlist = []
                for line in atlist:
                    if line[0] == e[0]:
                        trabalho = Trabalho(line[2], line[3], line[5])
                        trabalho.cod = line[1]
                        if not line[4] is None:
                            trabalho.dataEntrega = line[4]
                        tlist.append(trabalho)
                autor.trabalho = tlist
                lista.append(autor)
            cur.close()
            conn.commit()
            conn.close()
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