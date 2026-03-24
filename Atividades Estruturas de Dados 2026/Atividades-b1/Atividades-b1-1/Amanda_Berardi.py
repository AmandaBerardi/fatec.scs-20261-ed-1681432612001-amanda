'''
*---------------------------------------------------------*
* Fatec São Caetano do Sul *
* Atividade B1-1 *
* Autor: Amanda Berardi Ferreira *
* Objetivo: Criar um catalogo de filmes, e possibilitar adicionar, buscar, remover e listar os filmes catalogados*
* data: 24/02/2026 *
*---------------------------------------------------------*
'''

catalogo = {}

def adicionar_filme ( id_filme , titulo , diretor ) :
 if id_filme in catalogo :
    print ("Filme já cadastrado")

 else: 

    catalogo[id_filme] = {
    "ID": id_filme,
    "titulo": titulo,
    "diretor": diretor,
    }



def buscar_filme(id_filme):

    if id_filme not in catalogo:
        print("Esse filme não está no catálogo")

    else:
        print("titulo:", catalogo[id_filme]["titulo"])
        print("diretor:", catalogo[id_filme]["diretor"])



def remover_filme ( id_filme ) :    
    if id_filme not in catalogo:
        print("Esse filme não está no catálogo")

    else:
        catalogo.pop(id_filme)
        print("Filme removido")



def listar_todos () :

   if not catalogo :
     print ("O catalogo esta vazio")
   else :
     print ("- - - Listagem de Filmes ---")
     for id_filme , dados in catalogo . items () :
      print ( f"ID: { id_filme } | titulo : { dados ['titulo']} | diretor : { dados ['diretor']}")



# --- Testes de Funcionamento ---

adicionar_filme(1, "Interestelar", "Christopher Nolan")
adicionar_filme(2, "La La Land", "Damien Chazelle")

listar_todos()

buscar_filme(1)

remover_filme(2)

listar_todos()