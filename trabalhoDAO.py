from serverDAO import serverDao
from trabalho import Trabalho
from autor import Autor
import psycopg2
import datetime

class trabalho_DAO(serverDao):
    def connect(self):
        super().connect()
    
    def save(self, obj):
        conn = self.connect()
        cur = conn.cursor()
        if hasattr(obj, 'cod'):
            update = 'UPDATE "Trabalho" SET "conteudo" = %s, "nota" = %s, "titulo" = %s, "dataEntrega" = %s WHERE "cod" = %s;'
            if hasattr(obj, 'dataEntrega'):
                cur.execute(update, (obj.conteudo, obj.nota, obj.titulo, obj.dataEntrega, obj.cod))
            else:
                cur.execute(update, (obj.conteudo, obj.nota, obj.titulo, None, obj.cod))
            for e in obj.futuroAutor:
                update = 'INSERT INTO "TrabalhoAutor" VALUES (%s, %s)'
                cur.execute(update, (e.cod, obj.cod))
        else:
            insert = 'INSERT INTO "Trabalho"("conteudo", "nota", "titulo", "dataHoraAtualizacao") VALUES (%s, %s, %s, NOW())'
            cur.execute(insert, (obj.conteudo, obj.nota, obj.titulo))
            insert = 'SELECT * FROM "Trabalho"'
            cur.execute(insert)
            slist = cur.fetchall()
            t = slist[len(slist)-1]
            for e in obj.futuroAutor:
                insert = 'INSERT INTO "TrabalhoAutor" VALUES (%s, %s)'
                cur.execute(insert, (e.cod, t[0]))
        cur.close()
        conn.commit()
        conn.close()

    def dolist(self):
        with connect(self.bd) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM "Trabalho"')
            slist = cur.fetchall()
            select = 'SELECT "at"."codTrabalho", "a"."cod", "a"."nome", "a"."email" FROM "Autor" AS "a" INNER JOIN "TrabalhoAutor" AS "at" ON "a"."cod" = "at"."codAutor"'
            cur.excute(select)
            atlist = cur.fetchall()
            lista = []
            for e in slist:
                trabalho = Trabalho(e[1], e[2], e[4])
                trabalho.cod = e[0]
                for e in slist:
                    trabalho = Trabalho(e[1], e[2], e[4], e[4])
                    trabalho.cod = e[0]
                    if not e[3] is None:
                        trabalho.dataEntrega = e[3]
                    tlist = []
                    for line in atlist:
                        if line[0] == e[0]:
                            autor = Autor(line[2], line[3])
                            autor.cod = line[1]
                            tlist.append(autor)
                    trabalho.autor = tlist
                    lista.append(trabalho)
            cur.close()
            conn.commit()
            conn.close()
            return lista
        
    def delete(self,obj):
        with connect(self.bd) as conn:
            cur = conn.cursor()
            cur.execute('DELETE FROM "Trabalho" WHERE "cod" = %s',[obj.cod])
            cur.close
            conn.commit()
            cur.close()
